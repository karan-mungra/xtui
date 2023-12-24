from ._stack_container import StackContainer


class HStack(StackContainer):
    def __init__(self, spacing: int):
        super().__init__(spacing)

    def __call__(self, stdscr):
        y, x = stdscr.getyx()

        for child in self.model:
            stdscr.move(y, x)
            child(stdscr)
            _, x1 = stdscr.getyx()
            x = x1 + self._StackContainer__spacing
