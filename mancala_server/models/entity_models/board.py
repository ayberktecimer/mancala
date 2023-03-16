"""This module contains the Board class."""
from static.constants import BOARD_LIST


class Board:
    """This class represents the board of the game."""

    def __init__(self) -> None:
        self.board_list = self.generate_board()

    def generate_board(self):
        """This method generates the board."""
        # deep copy the board list
        return BOARD_LIST.copy()
