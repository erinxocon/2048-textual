from enum import Enum


class GameStates(Enum):
    can_play = "More moves remain"
    won = "You Won!"
    lost = "You Lost!"


class MoveType(Enum):
    LEFT = 0
    RIGHT = 1
    UP = 2
    DOWN = 3
