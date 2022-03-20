import numpy as np
from rich import print

from .logic import TwentyFortyEight
from .enums import MoveType

a = np.array([[0, 2, 4, 4], [2, 2, 4, 2], [0, 2, 4, 0], [2, 2, 4, 4]], dtype=int)
b = TwentyFortyEight(initial_state=a)
print(f"initial state:\n{b}")

for _ in range(100):
    b.make_move(MoveType.DOWN)
    print(f"Move down result:\n{b}")
    b.make_move(MoveType.RIGHT)
    print(f"Result of move left:\n{b}")
