from xtui.container import VStack
from xtui.widget import Label
from xtui.window import Window


stack = VStack(spacing=2)
stack.bind_model([Label(f"{i}") for i in range(0, 10)])
Window(stack).present()
