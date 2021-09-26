import random
import sys
from time import sleep

import constants
import functions
from Cell import Cell
from functions import clear_terminal


class Board(object):
    def __init__(self, width, height, bombs, is_decode=False):

        # check and change recursion size
        sys.setrecursionlimit(width * height + 10)

        self.width: int = width
        self.height: int = height
        self.bombs: int = bombs

        # for viewing in the terminal
        self.view_bomb = bombs

        self.is_decode = is_decode

        self.board: list = [[Cell() for _ in range(self.width)] for _ in
                            range(self.height)]

        self.result = None

    def generate_board(self, touch_coordinates):
        for _ in range(self.bombs):

            while True:
                x, y = random.randrange(0, self.width), random.randrange(0, self.height)

                if self.board[y][x].is_bomb() or (x, y) == touch_coordinates:
                    continue
                else:
                    # add number around bomb
                    self.board[y][x].set_bomb()
                    for i in range(x - 1, x + 2):
                        if not 0 <= i < self.width:
                            continue

                        for j in range(y - 1, y + 2):
                            if not 0 <= j < self.height or (i, j) == (x, y):
                                continue

                            if not self.board[j][i].is_bomb():
                                self.board[j][i].add_number()

                    break
        self.save()

    def print_board(self):
        print('Бомб осталось:', self.view_bomb)
        print()
        print(' ' * 3, *(str(i).center(3) for i in range(self.width)), sep=' | ', end=' |\n')
        print()
        print(' ' * 4 + '-' * (6 * self.width + 1))

        for y in range(self.height):
            print(str(y).ljust(3), *map(lambda x: str(x).center(3), self.board[y]), sep=' | ',
                  end=' |\n')
            print('-' * (6 * self.width + 5))

        print()

    def check_win(self):
        if self.result:
            return

        for i in range(self.width):
            for j in range(self.height):
                if (self.board[j][i].is_empty() or self.board[j][i].is_number()) and \
                        self.board[j][i].is_close():
                    return

        self.result = constants.WIN

    def read_command(self):
        while True:
            try:
                print('Введите комманду в формате <X Y ACTION>')
                print('ACTION либо open, либо Flag')
                x, y, action = input().split()

                action = action.lower()
                x, y = int(x), int(y)

                if 0 <= x < self.width and 0 <= y < self.height \
                        and action in (constants.OPEN_CELL, constants.FLAG_CELL):
                    return x, y, action
                else:
                    print('Вы ввели некорректную комманду\n')
                    continue

            # в случае неправильного ввода
            except Exception:
                print('Вы ввели некорректную комманду\n')
                continue

    def open_all(self):
        for i in range(self.width):
            for j in range(self.height):
                self.board[j][i].forced_open()

    def open_empty(self, x, y):  # recursive function
        self.board[y][x].open()

        for i in range(x - 1, x + 2):
            if not 0 <= i < self.width:
                continue

            for j in range(y - 1, y + 2):
                if not 0 <= j < self.height or (i, j) == (x, y):
                    continue

                if self.board[j][i].is_close() \
                        and self.board[j][i].is_empty() \
                        or self.board[y][x].is_empty() and self.board[j][i].is_number() \
                        and not self.board[j][i].is_flag():
                    self.open_empty(i, j)

    def open(self, x, y):
        if not self.result:
            if self.board[y][x].open():
                if self.board[y][x].is_bomb():
                    self.result = constants.LOST
                    self.open_all()

                elif self.board[y][x].is_empty():
                    self.open_empty(x, y)
            else:
                print('Невозможно открыть эту клетку')

    def set_flag(self, x, y):
        if self.board[y][x].set_flag():
            self.view_bomb += -1 if self.board[y][x].is_flag() else 1

    def save(self):
        symbols = list(constants.SYMBOLS_FOR_ENCODING)
        random.shuffle(symbols)

        empty_symbol, bomb_symbol, enter_symbol = symbols[:3]

        content = enter_symbol.join([''.join([bomb_symbol if j.is_bomb() else empty_symbol
                                              for j in i]) for i in self.board])
        content = f'{content}{empty_symbol}{bomb_symbol}{enter_symbol}'

        functions.save_file(content)

    def play(self):

        # generate new board and first action, if data from the file
        if not self.is_decode:
            clear_terminal()

            self.print_board()
            x, y, action = self.read_command()

            # first generation, (x, y) not is bomb
            self.generate_board((x, y))

            if action == constants.OPEN_CELL:
                self.open(x, y)
            elif action == constants.FLAG_CELL:
                self.set_flag(x, y)

        # infinity loop for the game
        while True:
            clear_terminal()

            self.check_win()

            self.print_board()

            if not self.result:
                x, y, action = self.read_command()

                if action == constants.OPEN_CELL:
                    self.open(x, y)
                elif action == constants.FLAG_CELL:
                    self.set_flag(x, y)

            elif self.result:
                if self.result == constants.WIN:
                    print('Вы победили!!!\n\n')
                elif self.result == constants.LOST:
                    print('Вы проиграли.\n\n')

                print('Через 5 секунд вы перейдете в гланое меню')

                sleep(5)

                return


def decode(content):
    empty_symbol, bomb_symbol, enter_symbol = content[-3:]
    content = content[:-3]
    bombs = content.count(bomb_symbol)
    content = content.split(enter_symbol)

    width, height = len(content[0]), len(content)

    board = Board(width, height, bombs, is_decode=True)

    for i in range(width):
        for j in range(height):
            if content[j][i] == bomb_symbol:
                board.board[j][i].set_bomb()

                for x in range(i - 1, i + 2):
                    if not 0 <= x < width:
                        continue

                    for y in range(j - 1, j + 2):
                        if not 0 <= y < height or (x, y) == (i, j):
                            continue

                        if not board.board[y][x].is_bomb():
                            board.board[y][x].add_number()

    return board


if __name__ == '__main__':
    # debug run
    decode('77777X77777X77777X77777X777777aX')
