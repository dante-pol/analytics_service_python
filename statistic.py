import numpy as np
import graphics
import json


def statistic_main(path: str) -> None:
    """
    Основная функция, состоящая из небольших функций по обработке данных.
    Если данных для анализа недостаточно, то возвращает None
    :param path: Строка, где указан пусть к файлу
    :return: None
    """
    data_sum_playtime = None
    data_avg_lvl = None
    data_perc_win = None

    data_list = read_file(path)
    if data_list:
        data_array = make_array(data_list)
        data_sum_playtime = summary_playtime(data_array)
        data_avg_lvl = avg_lvl_playtime(data_array)
        data_perc_win = perc_win_players(data_array)

    send_result_to_graphics(data_sum_playtime, data_avg_lvl, data_perc_win)

    return None


def send_result_to_graphics(sum_time: np.array, avg_time: np.array, rating: np.array) -> None:
    '''
    Функция-передатчик результатов вычислений в модуль построения графиков
    :param sum_time: суммарный плейтайм по всем игрокам
    :param avg_time: средний плейтайм по уровням
    :param rating: процент успешно прошедних игроков
    :return: передает результаты в модуль построения графиков
    '''
    graphics.players_times(sum_time)
    graphics.playtime(avg_time)
    graphics.rating_shares(rating)


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


def summary_playtime(data_array: np.array) -> np.array:
    '''
    Считает общий плейтайм для каждого игрока
    :param data_array: массив данных в формате ndarray
    :return: общий плейтайм в формате int
    '''
    result = []
    for i in range(1, len(data_array), 1):
        result.append([data_array[i][0], np.sum(data_array[::, 1::])])

    return np.array(result)


def avg_lvl_playtime(data_array: np.array) ->np.array:
    '''
    Считает средний плейтайм за каждый уровень по всем игрокам
    :param data_array: массив данных в формате ndarray
    :return: стреднее арифметическое в формате float
    '''
    result = []
    count_lvl = len(data_array[0] - 1)
    for i in range(1, count_lvl, 1):
        result.append([i, np.sum(data_array[::, [i]]) / count_lvl])

    return np.array(result)


def perc_win_players(data_array: np.array) -> np.array:
    '''
    Считает, сколько в среднем игроков успешно прошли данный уровень, выражается в %
    :param data_array: массив данных в формате ndarray
    :return: процент игроков в формате float
    '''
    result = []
    count_lvl = len(data_array[0] - 1)
    for i in range(1, count_lvl, 1):
        result.append([i, (np.sum(data_array[::, [i]]) / count_lvl) / len(data_array) * 100])

    return np.array(result)


