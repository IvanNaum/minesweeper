import random

import constants
import functions
from Board import Board, decode


def main():
    commands = tuple(map(lambda x: f'{x[0]}. {x[1]["name"]}', constants.COMMANDS.items()))
    while True:
        functions.clear_terminal()

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
            elif command['constant_name'] == constants.LAST_PARTS:
                files = functions.get_files()
                while True:
                    print('Выберите нужную партию:')
                    for i, name in enumerate(files):
                        print(f'{i + 1}. {name}')
                    try:
                        input_file = int(input())
                        if not 0 < input_file <= len(files):
                            raise ValueError
                        break
                    except ValueError:
                        functions.clear_terminal()
                        print('Вы ввели некорректное значение.\n')
                    except TypeError:
                        functions.clear_terminal()
                        print('Вы ввели отрицательное значение.\n')

                board = decode(functions.read_file(files[input_file - 1] + '.txt'))
                board.play()


if __name__ == '__main__':
    main()
