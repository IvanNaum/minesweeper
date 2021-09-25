import random

import constants
from Board import Board


def main():
    commands = tuple(map(lambda x: f'{x[0]}. {x[1]["name"]}', constants.COMMANDS.items()))
    while True:
        print('Выберите команду (введите цифру)')
        print(*commands, sep='\n')

        input_command = input().strip()
        command = constants.COMMANDS.get(input_command)
        if command:
            if command['constant_name'] == constants.STANDARD_SIZE:
                board = Board(5, 5, random.randint(2, 5))
                board.play()
            elif command['constant_name'] == constants.SELF_SIZE:
                ...




if __name__ == '__main__':
    main()
