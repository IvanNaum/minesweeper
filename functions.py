import os


def clear_terminal():
    print('Если вы читаете эту надпись, в вашем терминале не работает функция CLEAR\n')
    os.system('cls' if os.name == 'nt' else 'clear')
