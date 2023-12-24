from xtui.container import VStack, HStack
from xtui.widget import Label
from xtui.window import Window


stack = VStack(spacing=2)
for i in range(0, 10):
    hstack = HStack(spacing=2)
    hstack.bind_model([Label(":)") for _ in range(0, 10)])
    stack.append(hstack)

Window(stack).present()
