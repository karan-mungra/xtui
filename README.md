# Xtui

- A python tui library formed on top of curses.
- This library is still under heavy development.
- Given below example uses a Vertical Stack Container to show a list of Labels. Then the stack is set as the child for the window. Finally the window is displayed.
```python
from xtui.container import VStack
from xtui.widget import Label
from xtui.window import Window


stack = VStack(spacing=2)
stack.bind_model([Label(f"{i}") for i in range(0, 10)])
Window(stack).present()
```
!["Output of the above code"](./assests/output.png "Output of the above code")