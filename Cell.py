import constants


class Cell(object):
    def __init__(self):
        self.type = constants.EMPTY

        self.is_open = False
        self.flag = False
        self.number = 0

    def open(self):
        if not self.flag:
            self.is_open = True

    def set_flag(self):
        if not self.is_open:
            self.flag = not self.flag

    def set_bomb(self):
        self.type = constants.BOMB

    def is_bomb(self):
        return self.type == constants.BOMB

    def __str__(self):
        if self.is_open:
            if self.type == constants.BOMB:
                return constants.SYMBOLS_STR[constants.BOMB]
            if self.type == constants.EMPTY:
                return str(self.number) if self.number > 0 else ' '

        elif not self.is_open:
            if self.flag:
                return constants.SYMBOLS_STR['flag']

            return constants.SYMBOLS_STR['close']
