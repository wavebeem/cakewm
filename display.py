from util import *

class Display(object):
    "A display manages screens"

    def __init__(self, **kwargs):
        self.cur     = kwargs.get("cur",     None)
        self.screens = kwargs.get("screens", [])

    def move_win_screen_num(self, number):
        "Moves the current window to nth screen"

        if self.cur is not None:
            try:
                win = self.take_cur_win()
                if win is not None:
                    self.screens[self.cur].add_window(win)
            except IndexError:
                debug("Attempted to move window to non-existent screen")

    def swap_tags_num(self, number):
        "Swap the current tags on the current and nth screen"

        try:
            this_screen = self.screens[self.cur]
            that_screen = self.screens[number  ]

            if (this_screen is not None and
                that_screen is not None):
                this_tag_num = this_screen.cur
                that_tag_num = that_screen.cur

                if (this_tag_num is not None and
                    that_tag_num is not None):
                    this_screen[this_tag_num] = that_tag
                    that_screen[that_tag_num] = this_tag
        except IndexError:
            debug("Screen out of range")
