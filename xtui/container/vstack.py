from ._stack_container import StackContainer


class VStack(StackContainer):
    def __init__(self, spacing: int):
        super().__init__(spacing)

    def __call__(self, stdscr):
        y, x = stdscr.getyx()

        for child in self.model:
            stdscr.move(y, x)
            child(stdscr)
            y1, _ = stdscr.getyx()
            y = y1 + self._StackContainer__spacing
