from pypixel import *

from container  import *
from stacks     import *
from util       import *

class Columns(Container):

    SHORT_CLASS = "Cols"

    def organize(self):
        '''Place windows appropriately'''

        for i, stacks in self.each():
            for j, stack in stacks.each():
                for k, window in stack.each():
                    col_w   = WIDTH  / len(self.items)
                    stack_h = HEIGHT / len(stacks.items)

                    window.x = i * col_w
                    window.y = j * stack_h

                    window.w = col_w
                    window.h = stack_h

    def go_stack_next(self): self.items[self.cur].go_next()
    def go_stack_prev(self): self.items[self.cur].go_prev()

    def go_win_next(self): self.items[self.cur].go_win_next()
    def go_win_prev(self): self.items[self.cur].go_win_prev()

    def _move_win_col(self, a):
        stacks  = self      .get_cur_item()
        stack   = stacks    .get_cur_item()
        nstacks = self      ._get_item(a)
        nstack  = nstacks   .get_cur_item()
        win     = stack     .remove_cur_item()
        nstack._make_new(win, -1)
        stack._go(a)

    def move_win_col_next(self): self._move_win_col(+1); self._go(+1)
    def move_win_col_prev(self): self._move_win_col(-1); self._go(-1)

    def _make_win_col(self, a):
        stacks  = self      .get_cur_item()
        stack   = stacks    .get_cur_item()
        win     = stack     .remove_cur_item()

        nstacks = Stacks(cur=0, items=[Stack(cur=0, items=[win])])
        self._make_new(nstacks, a)
        stack._go(a)

    def make_win_col_next(self): self._make_win_col(+1)
    def make_win_col_prev(self): self._make_win_col(-1)
