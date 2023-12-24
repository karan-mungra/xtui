from curses import wrapper

class Window:
    def __init__(self, child):
        self.child = child

    def __call(self, stdscr):
        stdscr.clear()
        self.child(stdscr)
        stdscr.refresh()
        stdscr.getkey()

    def present(self):
        wrapper(self.__call)