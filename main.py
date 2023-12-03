import string

from player import Player
from game import Game
from string import digits


def update_board(self):
    bottom = "+-----+-----+-----+"
    print(bottom)
    for i in range(self.board.size):
        print(f'|  {self.board.board[i][0]}  |  {self.board.board[i][1]}  |  {self.board.board[i][2]}  |')
        print(bottom)


def show_menu(menu):
    print('-' * 20)

    for i in range(len(menu)):
        print(f'[{i}] - {menu[i]}')

    print('-' * 20)

def start_new_game():
    game = Game()
    while not game.is_over():
        print_board(game)
        while not game.turn(get_next_turn(game)):
            print("Клетка занята, повторите ввод")

    if game.draw:
        print("Ничья")

    if game.victory:
        players[game.current_player].wins += 1
        print('-' * 20)
        print(f'Победа {players[game.current_player]}')
        print('-' * 20)


def get_next_turn(game):
    correct = False
    while not correct:
        try:
            print(f'Ходит игрок {players[game.current_player]}')
            result = list(filter(lambda x: x in string.digits,
                                 input(f'Введите номер строки [1-{game.board.size}] '
                                       f'и номер солбца[1-{game.board.size}] через пробел: ')))
            result = [int(x) - 1 for x in result]
            if all(0 <= int(x) < game.board.size for x in result) and len(result) == 2:
                correct = True
            else:
                raise ValueError
        except:
            print("Неправильный ввод, повторите")
    return result

def print_board(game):
    row_separator = "+-----+-----+-----+"
    print(row_separator)
    for i in range(game.board.size):
        print('|', end='')
        for c in range(game.board.size):
            print(f'  {game.board.board[i][c]}  |', end='')
        print()
        print(row_separator)


def get_new_name(old_name):
    result = input(f'Введите новое имя для {old_name} или нажмите ввод чтобы оставить прежним: ')
    if len(result) != 0:
        return result
    return old_name


if __name__ == '__main__':
    players = [Player("Игрок 1", 'X'), Player("Игрок 2", 'O')]
    menu_items = ['начать игру', f'Изменить {players[0].name}', f'Изменить {players[1].name}', 'выход']

    exit_menu_flag = False
    while not exit_menu_flag:
        show_menu(menu_items)
        result = int(list(filter(lambda x: x in digits,
                                 input('Введите номер пункта меню: ')))[0])
        if result in range(len(menu_items)):
            if result == 0:
                start_new_game()
            elif result == 1:
                players[0].name = get_new_name(players[0].name)
            elif result == 2:
                players[1].name = get_new_name(players[1].name)
            else:
                exit_menu_flag = True
        else:
            print("Неправильный ввод, повторите")















