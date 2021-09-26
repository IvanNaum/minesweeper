import constants
import random
import sys
from time import sleep
from Cell import Cell
from functions import clear_terminal


class Board(object):
    def __init__(self, width, height, bombs):
        # check and change recursion size
        sys.setrecursionlimit(width * height - bombs + 10)

        self.width: int = width
        self.height: int = height
        self.bombs: int = bombs

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

    def print_board(self):
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
                        or self.board[y][x].is_empty() and self.board[j][i].is_number():
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

    def play(self):
        clear_terminal()

        self.print_board()
        x, y, action = self.read_command()

        # first generation, (x, y) not is bomb
        self.generate_board((x, y))

        if action == constants.OPEN_CELL:
            self.open(x, y)
        elif action == constants.FLAG_CELL:
            self.board[y][x].set_flag()

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
                    self.board[y][x].set_flag()
            elif self.result:
                if self.result == constants.WIN:
                    print('Вы победили!!!\n\n')
                elif self.result == constants.LOST:
                    print('Вы проиграли.\n\n')

                print('Через 5 секунд вы перейдете в гланое меню')

                sleep(5)

                return


if __name__ == '__main__':
    # debug run
    Board(5, 5, 4).play()
