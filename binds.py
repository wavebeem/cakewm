import util
import itertools
from window import Window
from ratio  import Ratio

class Binds(object):
    "A binds object is used for making keybinds"

    def __init__(self, **kwargs):
        self._display = kwargs["display"]

    def has_fullscreen(self):
        tag = self.tag()
        return tag.fullscreen

    def display(self):
        return self._display

    def screen(self):
        screen = self.display().item()
        return screen

    def tag(self):
        screen = self.screen()
        tag    = screen.item()
        return tag

    def col(self):
        tag = self.tag()
        col = tag.item()
        return col

    def stack(self):
        col   = self.col()
        stack = col.item()
        return stack

    def do_do(thing, cmd, **kwargs):
        fs_guard = kwargs.get("fs_guard", True)
        args     = kwargs.get("args", ())
        def inner(self, thing=thing, fs_guard=fs_guard, cmd=cmd):
            if fs_guard and self.has_fullscreen():
                return
            try:
                thing = getattr(self, thing)()
            except Exception as e:
                util.errors(
                    "tried doing #<%s instance>.%s()" % (type(self).__name__, thing),
                    "this is the instance: %s" % repr(thing),
                    str(e)
                )
            if thing is not None:
                try:
                    getattr(thing, cmd)(*args)
                except Exception as e:
                    util.errors(
                        "tried doing #<%s instance>.%s(%s)" % (type(thing).__name__, cmd, ", ".join(args)),
                        str(e)
                    )

        return inner

    # Display binds
    move_win_screen_next = do_do("display", "move_win_screen_next")
    move_win_screen_prev = do_do("display", "move_win_screen_prev")
    select_screen_next   = do_do("display", "select_screen_next")
    select_screen_prev   = do_do("display", "select_screen_prev")
    swap_tags_next       = do_do("display", "swap_tags_next")
    swap_tags_prev       = do_do("display", "swap_tags_prev")

    # Screen binds
    move_win_tag_next = do_do("screen", "move_win_tag_next")
    move_win_tag_prev = do_do("screen", "move_win_tag_prev")
    move_win_tag_1    = do_do("screen", "move_win_tag_num", args=[0])
    move_win_tag_2    = do_do("screen", "move_win_tag_num", args=[1])
    move_win_tag_3    = do_do("screen", "move_win_tag_num", args=[2])
    move_win_tag_4    = do_do("screen", "move_win_tag_num", args=[3])
    move_win_tag_5    = do_do("screen", "move_win_tag_num", args=[4])
    move_win_tag_6    = do_do("screen", "move_win_tag_num", args=[5])
    move_win_tag_7    = do_do("screen", "move_win_tag_num", args=[6])
    move_win_tag_8    = do_do("screen", "move_win_tag_num", args=[7])
    move_win_tag_9    = do_do("screen", "move_win_tag_num", args=[8])
    select_tag_next   = do_do("screen", "select_tag_next",  fs_guard=False)
    select_tag_prev   = do_do("screen", "select_tag_prev",  fs_guard=False)
    select_tag_1      = do_do("screen", "select_tag_num", args=[0], fs_guard=False)
    select_tag_2      = do_do("screen", "select_tag_num", args=[1], fs_guard=False)
    select_tag_3      = do_do("screen", "select_tag_num", args=[2], fs_guard=False)
    select_tag_4      = do_do("screen", "select_tag_num", args=[3], fs_guard=False)
    select_tag_5      = do_do("screen", "select_tag_num", args=[4], fs_guard=False)
    select_tag_6      = do_do("screen", "select_tag_num", args=[5], fs_guard=False)
    select_tag_7      = do_do("screen", "select_tag_num", args=[6], fs_guard=False)
    select_tag_8      = do_do("screen", "select_tag_num", args=[7], fs_guard=False)
    select_tag_9      = do_do("screen", "select_tag_num", args=[8], fs_guard=False)

    # Tag binds
    column_magic_next    = do_do("tag", "item_magic_next")
    column_magic_prev    = do_do("tag", "item_magic_prev")
    toggle_fullscreen    = do_do("tag", "toggle_fullscreen", fs_guard=False)
    close_win            = do_do("tag", "close_win", fs_guard=False)
    move_win_col_next    = do_do("tag", "move_win_col_next")
    move_win_col_prev    = do_do("tag", "move_win_col_prev")
    tag_master_prev      = do_do("tag", "prev_master")
    tag_master_next      = do_do("tag", "next_master")
    select_col_next      = do_do("tag", "select_col_next")
    select_col_prev      = do_do("tag", "select_col_prev")
    inc_tag_ratio        = do_do("tag", "inc_tag_ratio")
    dec_tag_ratio        = do_do("tag", "dec_tag_ratio")
    toggle_bar           = do_do("tag", "toggle_bar", fs_guard=False)
    complement_tag_ratio = do_do("tag", "complement_tag_ratio")

    # Column binds
    stack_magic_next     = do_do("col", "item_magic_next")
    stack_magic_prev     = do_do("col", "item_magic_prev")
    col_master_prev      = do_do("col", "prev_master")
    col_master_next      = do_do("col", "next_master")
    move_win_stack_next  = do_do("col", "move_win_stack_next")
    move_win_stack_prev  = do_do("col", "move_win_stack_prev")
    select_stack_next    = do_do("col", "select_stack_next")
    select_stack_prev    = do_do("col", "select_stack_prev")
    inc_col_ratio        = do_do("col", "inc_col_ratio")
    dec_col_ratio        = do_do("col", "dec_col_ratio")
    complement_col_ratio = do_do("col", "complement_col_ratio")

    # Stack binds
    select_win_next = do_do("stack", "select_win_next")
    select_win_prev = do_do("stack", "select_win_prev")
    move_win_next   = do_do("stack", "move_win_next")
    move_win_prev   = do_do("stack", "move_win_prev")
    add_win         = do_do("stack", "add_win")
