from ._stack_container import StackContainer

class VStack(StackContainer):
    def __init__(self, spacing: int):
        super().__init__(spacing)

    def __call__(self, stdscr):
        y, x = stdscr.getyx()

        for child in self.model:
            err = VStack.screen_write(stdscr, y, x, child)
            if err is not None:
                print(err)
                return

            y += self._StackContainer__spacing + len(child.splitlines())