import numpy as np
from typing import Optional


class TwentyFortyEight:
    def __init__(self, initial_state: Optional[np.ndarray], size: int = 4) -> None:
        self.game: np.ndarray = initial_state if initial_state is not None else np.zeros((size, size), dtype=int)

    def __repr__(self) -> str:
        return f'{self.game}\n'

    @property
    def size(self) -> int:
        return self.game.shape[0]

    def merge_cells(self):
        for i in range(self.size):
            for j in range(self.size - 1):
                k = j + 1
                if (self.game[i, j] == self.game[i, k]) and self.game[i, j] != 0:
                    self.game[i, j] *= 2
                    self.game[i, k] = 0
        return self

    def compress_cells(self):
        temp_game = np.zeros((self.size, self.size), dtype=int)
        for i in range(self.size):
            position = 0
            for j in range(self.size):
                if self.game[i, j] != 0:
                    temp_game[i, position] = self.game[i, j]
                    position += 1
        self.game = temp_game
        return self

    def move_left(self) -> None:
        self.compress_cells().merge_cells().compress_cells()

    def move_right(self) -> None:
        self.game = np.fliplr(self.game)
        self.move_left()
        self.game = np.fliplr(self.game)

    def move_up(self) -> None:
        self.game = np.transpose(self.game)
        self.move_left()
        self.game = np.transpose(self.game)

    def move_down(self) -> None:
        self.game = np.transpose(self.game)
        self.game = np.fliplr(self.game)
        self.move_left()
        self.game = np.transpose(self.game)
        self.game = np.fliplr(self.game)


if __name__ == '__main__':
    a = np.array([[0, 2, 4, 4], [2, 2, 4, 2], [0, 2, 4, 0], [2, 2, 4, 4]])

    b = TwentyFortyEight(initial_state=a)
    print(b.game)
    b.move_up()
    print(b.game)
    print('test')
