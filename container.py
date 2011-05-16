import util
from window import Window

class Container(object):
    '''This is the base class for the various containers
    (Display, Screen, Tag, Column, Stack)'''

    def __init__(self, **kwargs):
        self.cur    = kwargs.get("cur",     0)
        self.items  = kwargs.get("items",   [])

    def move_win_num(self, number):
        "Moves the current window to nth screen"

        if self.cur is not None:
            try:
                # Guard against IndexError
                self.items[number]

                win = self.take_cur_win()
                if win is not None:
                    self.items[number].add_win(win)
            except IndexError:
                util.debug("Attempted to move window to non-existent container")

    def item(self):
        try:
            return self.items[self.cur]
        except (TypeError, IndexError):
            return None

    def select_num(self, number):
        if util.between2(number, len(self.items)):
            self.cur = number
        else:
            util.debug("Out of range")

    def take_cur_win(self):
        item = self.item()
        return item.take_cur_win()

    def add_win(self, win):
        item = self.item()
        return item.add_win(win)

    def __repr__(self):
        return "C:%s:[%s]" % (
            self.cur,
            ", ".join(map(str, self.items))
        )
