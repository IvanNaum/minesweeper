BOMB = 'B'
EMPTY = 'E'

# symbols for print board
SYMBOLS_STR = {BOMB: 'B', 'flag': 'F', 'close': 'X'}

# constants command
STANDARD_SIZE = 'ST_S'
SELF_SIZE = 'S_S'

# start commands
COMMANDS = {
    '1': {
        'name': 'Стандартный размер (5x5, 2-5 бомб)',
        'constant_name': STANDARD_SIZE
    },
    '2': {
        'name': 'Свой размер (ввод с клавиатуры)',
        'constant_name': SELF_SIZE

    }
}

# board constants
OPEN_CELL = 'open'
FLAG_CELL = 'flag'

WIN = 'W'
LOST = 'L'
