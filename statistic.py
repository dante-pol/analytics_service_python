import numpy as np

# Нам присылают файл parsing.txt


def statistic_main(path: str) -> str:
    """
    Основная функция, состоящая из микро-сервисов по обработке данных
    :param path: Строка, где указан пусть к файлу
    :return: Массив данных типа ndarray, записанный в файл. Возвращает путь к файлу
    """
    pass

def read_file(path: str) -> list:
    '''
    Микро-сервис, который считывает информацию с файла
    :param path: Строка, где указан пусть к файлу
    :return: Список с данными
    '''
    pass



def convert_str_to_list(data: str) -> list:
    """
    Микро-сервис, который конвертирует строку с данными в список данных
    :param data: датасет в формате строки
    :return:датасет в формате списка
    """
    pass


def make_array(data: list) -> list:
    '''
    Из списка через numpy конвертируем ndarray
    :param data: список данных в формате list
    :return: массив данных в формате ndarray
    '''


def check_valid(data: list) -> bool:
    '''
    Микро-сервис, осуществляющий проверку на валидность данных в текущем списке
    :param data: список данных в формате list
    :return: True, если елементов больше 10, и False, если меньше
    '''


def summary_playtime(dataset: list) -> int:
    '''
    Считает общий плейтайм для каждого игрока
    :param dataset: массив данных в формате ndarray
    :return: общий плейтайм в формате int
    '''


def avg_lvl_playtime(dataset: list) ->float:
    '''
    Считает средний плейтайм за каждый уровень по всем игрокам
    :param dataset: массив данных в формате ndarray
    :return: стреднее арифметическое в формате float
    '''


def perc_win_players(dataset: list) ->float:
    '''
    Считает, сколько в среднем игроков успешно прошли данный уровень, выражается в %
    :param dataset: массив данных в формате ndarray
    :return: процент игроков в формате float
    '''