"""
Задание 2.*
Предложить еще какие-либо варианты (механизмы, подходы, библиотеки, идеи)
для оптимизации памяти и
доказать!!! (наглядно, кодом) их эффективность (на примере профилировщика)
"""
from memory_profiler import profile, memory_usage
from timeit import default_timer
from pympler import asizeof
import random
import pickle
import json


def time_profiler(fun):
    def wrapper(*args, **kwargs):
        start_memory = memory_usage()[0]
        start_time = default_timer()
        result = fun(*args, **kwargs)
        res_memory = memory_usage()[0] - start_memory
        res_time = default_timer() - start_time
        print(f'Время: {res_time} Память: {res_memory}')
        return result

    return wrapper


@time_profiler
def test_pickle(to_data):
    with open('data.pickle', 'wb') as f:
        pickle.dump(to_data, f)

    with open('data.pickle', 'rb') as fl:
        data_pickle = pickle.load(fl)
    return data_pickle


@time_profiler
def test_json(to_data):
    with open('to_data.json', 'w', encoding='utf-8') as f:
        json.dump(to_data, f)

    with open('to_data.json', 'r', encoding='utf-8') as fl:
        data_json = json.load(fl)
    return data_json


@time_profiler
def test_txt(to_data):
    with open('to_data.txt', 'w', encoding='utf-8') as f:
        for key, value in to_data.items():
            f.write(f'{key}, {value}\n')

    with open('to_data.txt', 'r', encoding='utf-8') as fl:
        to_data = fl.readlines()
    return to_data


data = {'User_1': {'Orders': ['iPhone 11', 'Laptop Lenovo', 'Mouse 4tech', 'Monitor loc']},
        'User_2': {'Orders': ['Samsung', 'test']},
        'User_3': {'Orders': ['Xiaomi', 'check_123', 'kyocera']},
        'User_4': {'Orders': ['Dell', 'deck_pro']},
        'User_5': {'Orders': ['HDMI HUB', 'recorder', 'micro']}
        }

print(f'Размер Pickle: {asizeof.asizeof(test_pickle(data))}')
print('=' * 50)
print(f'Размер JSON: {asizeof.asizeof(test_json(data))}')
print('=' * 50)
print(f'Размер Txt: {asizeof.asizeof(test_txt(data))}')
"""
Результат:
Время: 0.10838720000000002 Память: 0.01171875
Размер Pickle: 3176
==================================================
Время: 0.10906450000000001 Память: 0.0078125
Размер JSON: 3016
==================================================
Время: 0.10895309999999991 Память: 0.0
Размер Txt: 656

Использование специализированных библиотек для работы с данными позволяет оптимизировать работу с точки зрения
памяти и процессорного времени, а также удобства дальнейшей обработки данных.
Но, стоит внимательно относиться к выбору в зависимости от конктретной задачи, иначе можно получить
обратный эффект.
"""
