import os
import time
import statistic

def search_file() -> list[str]:
    """
    извлекаем файлы из папки players
    """
    lst = os.listdir(path='players')
    return lst


def generator(lst):
    """
    распаковывает файлы и отправляет их на парсинг
    """
    for el in lst:
        with open(f'players/{el}', 'r') as file:
            data = file.read()
        yield data


def parsing(lst):
    """
    парсит данные и передает их на запись
    """
    data_list = []
    for el in generator(lst):
        data = el.split('\n')
        playtime_list = parsing_playtime_list(data[2].split(" "))
        rating_list = parsing_rating_list(data[3].split(" "))
        data_list.append([playtime_list, rating_list])
    return data_list


def parsing_playtime_list(lst: list) -> list:
    for ind, data in enumerate(lst):
        if int(data) > 60:
            lst[ind] = 50
        if int(data) < 25:
            lst[ind] = 30
    return lst


def parsing_rating_list(lst: list) -> list:
    for ind, data in enumerate(lst):
        if data not in ['1', '2', '3']:
            lst[ind] = None
    return lst


def save_data_into_json():
    """
    записывает данные для отправки
    """
    import json
    data = get_data_for_save()
    dictionary = get_dictionary()
    dictionary.update(data)
    file = open('file.json', 'w')
    json.dump(dictionary, file, indent=4)
    return dictionary


def get_data_for_save():
    lst_key = search_file()
    lst_value = parsing(lst_key)
    dictionary = {}
    for key, value in zip(lst_key, lst_value):
        dictionary[key.rstrip('.txt')] = value
    return dictionary


def get_dictionary():
    import json
    file = open('file.json', 'r')
    dictionary = json.load(file)
    return dictionary


def push():
    """
    отправляет данные для дальнейшей работы
    """
    file = save_data_into_json()
    print(file)
    statistic.statistic_main(file)


def main():
    """
    главная функция
    """
    while True:
        time.sleep(30)
        push()

main()