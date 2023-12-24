from xtui.widget import Widget


class StackContainer(Widget):
    def __init__(self, spacing: int):
        self.__spacing = spacing
        self.model: list[Widget] = []

    def bind_model(self, model: list[Widget]):
        self.model = model

    def append(self, s: Widget):
        self.model.append(s)
