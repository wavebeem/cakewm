import util
from conf import conf

class Master(object):
    def __init__(self):
        self.master = 0

    def inc_master(self, inc):
        if conf.wrap:   func = util.wrap
        else:           func = util.clamp2

        self.master = func(self.master + inc, self.n_items())

    def next_master(self): self.inc_master(+1)
    def prev_master(self): self.inc_master(-1)
    def  fix_master(self): self.inc_master( 0)
