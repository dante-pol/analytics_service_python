import numpy as np
import graphics
import json


def statistic_main(path: str) -> str: # дописать, что возвращает
    """
    Основная функция, состоящая из небольших функций по обработке данных.
    Если данных для анализа недостаточно, то возвращает None
    :param path: Строка, где указан пусть к файлу
    :return: Массив данных типа ndarray, записанный в файл. Возвращает путь к файлу
    """
    data_list = read_file(path)
    if not data_list:
        return None

    data_sum_playtime = None
    data_avg_lvl = None
    data_perc_win = None

    data_array = make_array(data_list)
    data_sum_playtime = summary_playtime(data_array)
    graphics.players_times(data_sum_playtime)           # в модуль graphics передается массив np.array
    data_avg_lvl = avg_lvl_playtime(data_array)
    graphics.playtime(data_avg_lvl)                     # в модуль graphics передается массив np.array
    data_perc_win = perc_win_players(data_array)
    graphics.rating_shares(data_perc_win)               # в модуль graphics передается массив np.array


    return data_list


def read_file(path: str):
    '''
    Функция, которая считывает информацию с файла в формате json
    :param path: Строка, где указан пусть к файлу
    :return: Список с данными
    '''

    with open(path, 'r', encoding='utf8') as file:
        data = json.load(file)

    if not check_valid(data):
        return None

    data_list = convert_dict_to_list(data)

    return data_list


def convert_dict_to_list(data: dict) -> list:
    """
    Функция, который конвертирует словарь с данными в список данных
    :param data: датасет в формате словаря
    :return:датасет в формате списка
    """
    data_list = []
    for key, value in data:
        data_list.append([key, value])
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
    Функция, осуществляющая проверку на валидность данных в текущем списке
    :param data: список данных в формате list
    :return: True, если елементов больше 10, и False, если меньше
    '''

    is_valid = True
    if len(data) < 10:
        is_valid = False
    return is_valid


def summary_playtime(data_array: np.array) -> int:
    '''
    Считает общий плейтайм для каждого игрока
    :param data_array: массив данных в формате ndarray
    :return: общий плейтайм в формате int
    '''


def avg_lvl_playtime(data_array: np.array) ->float:
    '''
    Считает средний плейтайм за каждый уровень по всем игрокам
    :param data_array: массив данных в формате ndarray
    :return: стреднее арифметическое в формате float
    '''


def perc_win_players(data_array: np.array) ->float:
    '''
    Считает, сколько в среднем игроков успешно прошли данный уровень, выражается в %
    :param data_array: массив данных в формате ndarray
    :return: процент игроков в формате float
    '''


