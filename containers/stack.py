import util
from util import *
from container      import Container
from window         import Window
from focusable      import Focusable
from floatingrect   import FloatingRect
from conf           import conf

import pypixel

import const

class Stack(Container, Focusable, FloatingRect):
    "A stack manages windows"

    NAME = "Stk"

    def __init__(self, **kwargs):
        super(Stack, self).__init__(**kwargs)
        FloatingRect.__init__(self)

    def num_win(self):
        return self.n_wins()

    @property
    def windows(self):
        return self.items

    def cur_win_title(self):
        return self._with_item(lambda item: item.title())

    def cur_win(self):  return self.cur
    def tot_wins(self): return self.n_wins()

    n_wins = Container.n_items

    def _select_win(self, direction):
        if self.cur is not None:
            if conf.wrap:   func = util.wrap
            else:           func = util.clamp2
            self.cur = func(self.cur + direction.num, self.n_items())

    def select_win_next(self): self._select_win(const.NEXT)
    def select_win_prev(self): self._select_win(const.PREV)

    def _move_win(self, direction):
        if self.cur is not None:
            try:
                index = util.clamp2(self.cur + direction.num, self.n_items())
                util.swap(self.windows, self.cur, index)
                self.cur = index
            except IndexError:
                util.debug("Bad index for moving window")

    def move_win_next(self): self._move_win(const.NEXT)
    def move_win_prev(self): self._move_win(const.PREV)

    def close_win(self):
        if self.cur is not None:
            try:
                del self.windows[self.cur]
                self.cur = util.clamp2(self.cur - 1, self.n_items())
                if self.windows == []:
                    self.cur = None
            except IndexError:
                util.debug("Bad index removing window from stack")

    def add_win(self, win=None):
        win = win or Window()
        if self.cur is not None:
            self.windows.insert(self.cur, win)
        elif self.cur is None and self.windows == []:
            self.windows.append(win)
            self.cur = 0
        else:
            util.debug("Cannot add_win: sef.cur is None")

    def take_cur_win(self):
        win = self.item()
        self.close_win()
        return win

    def draw(self, **kwargs):
        hint  = kwargs.get("hint", "tblr")
        color = conf.stack_unfocused_color
        light = conf.stack_unfocused_highlight
        dark  = conf.stack_unfocused_shadow

        if self.focused:
            color = conf.stack_focused_color
            light = conf.stack_focused_highlight
            dark  = conf.stack_focused_shadow

        x = self.x
        y = self.y
        w = self.w
        h = self.h

        left  = x
        right = x + w - 1
        top   = y
        bot   = y + h - 1

        pypixel.rectangle(color, self.rect)

        # Draw light edge
        if "t" in hint: pypixel.line(light, (left, top), (right, top)) # top
        if "l" in hint: pypixel.line(light, (left, top), (left,  bot)) # left

        # Draw dark edge
        if "r" in hint: pypixel.line(dark, (right, bot), (right, top)) # right
        if "b" in hint: pypixel.line(dark, (right, bot), (left,  bot)) # bottom

        item = self.item()
        if item is not None:
            item.draw()

    def focus(self):
        super(Stack, self).focus()

        item = self.item()
        if item is not None:
            item.focus()

    def unfocus(self):
        super(Stack, self).unfocus()

        item = self.item()
        if item is not None:
            item.unfocus()

    def organize(self):
        # Try to use sane values for padding
        pad = util.clamp(conf.stack_padding, 0, 100)
        for i, win in enumerate(self.windows):
           win.x = self.x + pad
           win.y = self.y + pad

           win.w = self.w - pad - pad
           win.h = self.h - pad - pad
