import os
from datetime import datetime
from pathlib import Path

import constants


def clear_terminal():
    print('Если вы читаете эту надпись, в вашем терминале не работает функция CLEAR\n')
    os.system('cls' if os.name == 'nt' else 'clear')


def save_file(content: str):
    path = Path(constants.DIRECTORY)
    path.mkdir(parents=False, exist_ok=True)

    filename = datetime.now().strftime("%Y.%m.%d-%H.%M.%S") + '.txt'

    file = path / filename

    file.write_text(content)


def read_file(filename: str):
    return Path(f'{constants.DIRECTORY}/{filename}').read_text()


def get_files():
    path = Path(constants.DIRECTORY)
    if path.is_dir():
        return [file.name.rstrip('.txt') for file in path.iterdir()]
