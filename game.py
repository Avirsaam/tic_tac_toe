from board import Board
from player import Player
from random import choice
from random import randint

class Game:
    def __init__(self,symbols = ['X', 'O'], board_size = 3):
        self.board = Board(board_size)
        self.symbols = symbols
        self.current_player = randint(0,1)
        self.draw = False
        self.victory = False

    def turn(self, position):
        if not self.board.cell_is_empty(position[0], position[1]):
            return False

        self.board.set_cell(position[0], position[1], self.symbols[self.current_player])

        if self.board.is_victory_condition():
            self.victory = True

        elif  not self.board.empty_cell_is_available():
            self.draw = True

        else:
            if self.current_player == 0:
                self.current_player = 1
            else:
                self.current_player = 0

        return True

    def is_over(self):
        return self.victory or self.draw



