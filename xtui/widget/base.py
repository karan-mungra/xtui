from typing import Optional


class Widget:
    @staticmethod
    def screen_write(stdscr, y: int, x: int, s: str) -> Optional[str]:
        try:
            stdscr.addstr(y, x, s)
        except Exception as e:
            return str(e)

    def __init__(self):
        pass

    def __call__(self, stdscr):
        pass
