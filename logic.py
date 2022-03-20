from typing import Optional

import numpy as np

from .enums import GameStates, MoveType


class TwentyFortyEight:
    def __init__(self, initial_state: Optional[np.ndarray] = None, size: int = 4) -> None:
        self._num_turns = 0
        if initial_state is not None:
            self.game = initial_state
        else:
            self.game = np.zeros((size, size), dtype=int)
            self.add_new_tile()
        self._game_state = GameStates.can_play

    @property
    def size(self) -> int:
        return self.game.shape[0]

    @property
    def num_turns(self) -> int:
        return self._num_turns

    @property
    def game_state(self) -> GameStates:
        return self._game_state

    @game_state.setter
    def game_state(self, value: GameStates) -> None:
        self._game_state = value

    def add_new_tile(self) -> None:
        remaining_zeros = np.argwhere(self.game == 0)
        random_idx_row, random_idx_col = remaining_zeros[np.random.randint(remaining_zeros.shape[0], size=1)][0]
        self.game[random_idx_row, random_idx_col] = 2

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

    def make_move(self, move_type: MoveType) -> None:
        match move_type:
            case MoveType.LEFT:
                self.move_left()
            case MoveType.RIGHT:
                self.game = np.fliplr(self.game)
                self.move_left()
                self.game = np.fliplr(self.game)
            case MoveType.UP:
                self.game = np.transpose(self.game)
                self.move_left()
                self.game = np.transpose(self.game)
            case MoveType.DOWN:
                self.game = np.transpose(self.game)
                self.game = np.fliplr(self.game)
                self.move_left()
                self.game = np.fliplr(self.game)
                self.game = np.transpose(self.game)

        # increment move counter now that a move has been made
        self._num_turns += 1

        # check if we can still play and add a tile
        if 0 in self.game:
            self.add_new_tile()

        # check for any win states
        elif 2048 in self.game:
            self.game_state = GameStates.won

        # elif self.can_move_be_made():
        #     pass

        else:
            self.game_state = GameStates.lost
            raise NotImplementedError()

    def can_move_be_made(self) -> bool:
        return False

    def __str__(self) -> str:
        return f"""
Game Board:
 {np.array_str(self.game)[1:-1]}
Game State: {self.game_state.value}
Number of Turns: {self.num_turns}
"""
