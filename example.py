from xtui.container import VStack
from xtui.window import Window


stack = VStack(spacing=1)
stack.bind_model([str(i) for i in range(0, 10)])
Window(stack).present()
