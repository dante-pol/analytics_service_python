import os
import time


def search_file() -> list[str]:
    """
    извлекаем файлы из папки players
    """

    lst = os.listdir(path='players')
    return lst


def generator(lst: list):
    """
    распаковывает файлы и отправляет их на парсинг
    """
    pass


def parsing(lst: list[list]):
    """
    парсит данные и передает их на запись
    """
    pass


def save_data():
    """
    записывает данные для отправки
    """
    pass


def push():
    """
    отправляет данные для дальнейшей работы
    """
    pass


def main():
    """
    главная функция
    """
    pass