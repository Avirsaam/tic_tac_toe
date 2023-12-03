from player import Player

class Board():
    def __init__(self, size=3):
        self.size = size
        self.board = [[' ' for i in range(size)] for j in range(size)]

    def set_cell(self, x, y, symbol):
        self.board[x][y] = symbol

    def cell_is_empty(self,x,y):
        return self.board[x][y] == ' '

    def __all_are_the_same(self, l):
        if l[0] != ' ' and all(x == l[0] for x in l):
            return True
        return False

    def empty_cell_is_available(self):
        for col in self.board:
            if ' ' in col:
                return True
        return False

    def is_victory_condition(self):

        for r in range(self.size):
            row = []
            for col in self.board:
                row.append(col[r])

            if self.__all_are_the_same(row):
                return True

        for col in self.board:
            if self.__all_are_the_same(col):
                return True

        diag = []
        for i in range(self.size):
            diag.append(self.board[i][i])

        if self.__all_are_the_same(diag):
            return True

        revers_diag = []
        for i in range(self.size):
            revers_diag.append(self.board[i][self.size - 1 - i])

        if self.__all_are_the_same(revers_diag):
            return True

        return False

board = Board()
board.board[0][2] = 'O'
board.board[1][1] = 'X'
board.board[2][0] = 'X'
