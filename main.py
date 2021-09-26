import random

from functions import clear_terminal

import constants
from Board import Board


def main():
    commands = tuple(map(lambda x: f'{x[0]}. {x[1]["name"]}', constants.COMMANDS.items()))
    while True:
        clear_terminal()

        print('Выберите команду (введите цифру)')
        print(*commands, sep='\n', end='\n\n')

        input_command = input().strip()
        command = constants.COMMANDS.get(input_command)
        if command:
            if command['constant_name'] == constants.STANDARD_SIZE:
                board = Board(5, 5, random.randint(2, 5))
                board.play()
            elif command['constant_name'] == constants.SELF_SIZE:
                while True:
                    try:
                        width = int(input('Введите ширину:\t'))
                        if 0 > width > 100:
                            raise TypeError

                        height = int(input('Введите высоту:\t'))
                        if 0 > height > 100:
                            raise TypeError

                        bomb = int(input('Введите кол-во бомб:\t'))
                        if 0 > width > width * height:
                            raise TypeError

                        break
                    except ValueError:
                        print('Вы ввели некорректное значение.\n')
                    except TypeError:
                        print('Вы ввели отрицательное значение.\n')

                board = Board(width, height, bomb)
                board.play()


if __name__ == '__main__':
    main()
