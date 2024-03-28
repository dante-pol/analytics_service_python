import numpy as np
import graphics
import json


def statistic_main(path: str) -> str:
    """
    Основная функция, состоящая из микро-сервисов по обработке данных
    :param path: Строка, где указан пусть к файлу
    :return: Массив данных типа ndarray, записанный в файл. Возвращает путь к файлу
    """
    data_list = read_file(path)
    data_array = make_array(data_list)
    data_sum_playtime = summary_playtime(data_array)
    graphics.players_times(data_sum_playtime)
    data_avg_lvl = avg_lvl_playtime(data_array)
    graphics.playtime(data_avg_lvl)
    data_perc_win = perc_win_players(data_array)
    graphics.rating_shares(data_perc_win)


    return data_list


def read_file(path: str) -> list:
    '''
    Микро-сервис, который считывает информацию с файла
    :param path: Строка, где указан пусть к файлу
    :return: Список с данными
    '''

    with open(path, 'r', encoding='utf8') as file:
        reader = json.load(file)
    data_list = convert_str_to_list(reader) # отсюда отредактировать работу с json
    return data_list


def convert_str_to_list(data: str) -> list:
    """
    Микро-сервис, который конвертирует строку с данными в список данных
    :param data: датасет в формате строки
    :return:датасет в формате списка
    """
    data_list = data.split('\n')
    for elem in data_list:
        elem = elem.split(',')
    return data_list


def make_array(data: list) -> np.array:
    '''
    Из списка через numpy конвертируем ndarray
    :param data: список данных в формате list
    :return: массив данных в формате ndarray
    '''

    array = np.array(data)
    return array


def check_valid(data: list) -> bool:
    '''
    Микро-сервис, осуществляющий проверку на валидность данных в текущем списке
    :param data: список данных в формате list
    :return: True, если елементов больше 10, и False, если меньше
    '''

    is_valid = True
    if len(data) < 10:
        is_valid = False
    return is_valid


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


graphics.players_times(data)