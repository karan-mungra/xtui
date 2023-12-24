from ._stack_container import StackContainer

class HStack(StackContainer):
    def __init__(self, spacing: int):
        super().__init__(spacing)

    def __call__(self, stdscr):
        y, x = stdscr.getyx()

        for child in self.model:
            y1, _ = stdscr.getyx()

            if y != y1: y = y1
            last_line_length = 0

            for line in child.splitlines():
                err = HStack.screen_write(stdscr, y, x, line)
                if err is not None:
                    print(err)
                    return

                last_line_length = len(line)
                y += 1

            x += self._spacing + last_line_length
