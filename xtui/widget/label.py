from .base import Widget


class Label(Widget):
    def __init__(self, label: str):
        self.__label = label

    def __call__(self, stdscr):
        y, x = stdscr.getyx()
        err = Label.screen_write(stdscr, y, x, self.__label)
        if err is not None:
            print(err)
            return
