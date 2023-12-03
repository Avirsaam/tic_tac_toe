class Player:
    def __init__(self, name, symbol):
        self.symbol = symbol
        self.wins = 0
        self.name = name

    def won(self):
        self.wins += 1

    def __str__(self):
        return self.name + ' [' + self.symbol + ']'


