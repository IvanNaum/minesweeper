BOMB = 'B'
EMPTY = 'E'

# symbols for print board
SYMBOLS_STR = {BOMB: 'B', 'flag': 'F', 'close': 'X'}

# constants command
STANDARD_SIZE = 'ST_S'
SELF_SIZE = 'S_S'
LAST_PARTS = 'L_P'

# start commands
COMMANDS = {
    '1': {
        'name': 'Стандартный размер (5x5, 2-5 бомб)',
        'constant_name': STANDARD_SIZE
    },
    '2': {
        'name': 'Свой размер (ввод с клавиатуры)',
        'constant_name': SELF_SIZE
    },
    '3': {
        'name': 'Предыдущие партии',
        'constant_name': LAST_PARTS
    },
}

# board constants
OPEN_CELL = 'open'
FLAG_CELL = 'flag'

WIN = 'W'
LOST = 'L'

DIRECTORY = 'party-history'

ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
digits = '0123456789'
SYMBOLS_FOR_ENCODING = ascii_lowercase + ascii_lowercase.upper() + digits
