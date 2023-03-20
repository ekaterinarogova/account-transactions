import json
import datetime

def load_data(filename):
    """
    Загружает данные из файла json
    :param filename: файл json
    :return: список данных
    """
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

def sort_data(data):
    """
    Сортирует данные по дате и статусу операции.
    :param data: список данных
    :return: сортированный список по дате выполненных операций
    """
    sort_by_date = sorted(data, key=lambda x: datetime.datetime.strptime(x['date'], '%Y-%m-%dT%H:%M:%S.%f'), reverse=True)
    executed_oper = []
    for i in sort_by_date:
        if i['state'] == 'EXECUTED':
            executed_oper.append(i)

    return executed_oper


def pick_latest(data):
    """
    Выводит последние 5 выполненных операций из списка данных
    :param data: список операций
    :return: список последних 5 операций
    """
    latest_oper = []
    for i in range(5):
        latest_oper.append(data[i])

    return latest_oper

