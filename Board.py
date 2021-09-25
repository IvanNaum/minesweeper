import random

import constants
from Cell import Cell


class Board(object):
    def __init__(self, width, height, bombs):
        self.width: int = width
        self.height: int = height
        self.bombs: int = bombs

        self.board: list = [[Cell() for _ in range(self.width)] for _ in
                            range(self.height)]

    def generate_board(self, touch_coordinates):
        for i in range(self.bombs):

            while True:
                x, y = random.randrange(0, self.width), random.randrange(0, self.height)

                if self.board[y][x].is_bomb() or (x, y) == touch_coordinates:
                    continue
                else:
                    self.board[y][x].set_bomb()
                    break

    def print_board(self):
        print(' ' * 3, *(i for i in range(self.width)), sep=' | ', end=' |\n')
        print('-' * (4 * self.width + 5))

        for y in range(self.height):
            print(f'{y}  ', *self.board[y], sep=' | ', end=' |\n')

        print()

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

    def play(self):
        self.print_board()
        x, y, action = self.read_command()
        self.generate_board((x, y))

        if action == constants.OPEN_CELL:
            self.board[y][x].open()
        elif action == constants.FLAG_CELL:
            self.board[y][x].set_flag()

        while True:
            self.print_board()
            x, y, action = self.read_command()

            if action == constants.OPEN_CELL:
                self.board[y][x].open()
            elif action == constants.FLAG_CELL:
                self.board[y][x].set_flag()


if __name__ == '__main__':
    Board(5, 5, 5).play()
