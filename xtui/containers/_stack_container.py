from typing import Optional

class StackContainer:
    @staticmethod
    def screen_write(stdscr, y: int, x: int, s: str) -> Optional[str]:
        try:
            stdscr.addstr(y, x, s)
        except Exception as e:
            return str(e)

    def __init__(self, spacing: int):
        self._spacing = spacing
        self.model: list[str] = []

    def bind_model(self, model: list[str]):
        self.model = model

    def append(self, s: str):
        self.model.append(s)

    def __call__(self, stdscr):
        pass