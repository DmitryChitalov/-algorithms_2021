"""
Задание 1.

Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 3-5 ваших РАЗНЫХ скриптов!
(хотя бы 3 разных для получения оценки отл).
На каждый скрипт вы должны сделать как минимум по две реализации.

Можно взять задачи с курса Основ
или с текущего курса Алгоритмов

Результаты профилирования добавьте в виде комментариев к коду.
Обязательно сделайте аналитику (что с памятью в ваших скриптах, в чем ваша оптимизация и т.д.)

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО

Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!
"""

from timeit import default_timer
from memory_profiler import memory_usage, profile
import json
from pympler import asizeof


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


@profile
@time_profiler
def dict_insert(n):
    items = {}
    for i in range(1, n):
        items.update({i: i + 5})
    return items


@profile
@time_profiler
def list_insert(n):
    items = []
    for i in range(1, n):
        items.append(i)
    return items


@profile
@time_profiler
def set_insert(n):
    items = {i for i in range(1, n)}
    return items


dict_insert(500000)
list_insert(500000)
set_insert(500000)
"""
Результат:
Время: 0.18954399999999996 Память: 50.9453125
Время: 0.1386041 Память: 19.67578125
Время: 0.12596970000000007 Память: 30.2421875

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    30     19.3 MiB     19.3 MiB           1       def wrapper(*args, **kwargs):
    31     19.3 MiB      0.0 MiB           1           start_memory = memory_usage()[0]
    32     19.3 MiB      0.0 MiB           1           start_time = default_timer()
    33     70.2 MiB     50.9 MiB           1           result = fun(*args, **kwargs)
    34     70.2 MiB      0.0 MiB           1           res_memory = memory_usage()[0] - start_memory
    35     70.2 MiB      0.0 MiB           1           res_time = default_timer() - start_time
    36     70.2 MiB      0.0 MiB           1           print(f'Время: {res_time} Память: {res_memory}')
    37     70.2 MiB      0.0 MiB           1           return result

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    30     19.7 MiB     19.7 MiB           1       def wrapper(*args, **kwargs):
    31     19.7 MiB      0.0 MiB           1           start_memory = memory_usage()[0]
    32     19.7 MiB      0.0 MiB           1           start_time = default_timer()
    33     39.4 MiB     19.6 MiB           1           result = fun(*args, **kwargs)
    34     39.4 MiB      0.0 MiB           1           res_memory = memory_usage()[0] - start_memory
    35     39.4 MiB      0.0 MiB           1           res_time = default_timer() - start_time
    36     39.4 MiB      0.0 MiB           1           print(f'Время: {res_time} Память: {res_memory}')
    37     39.4 MiB      0.0 MiB           1           return result
    
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    30     20.5 MiB     20.5 MiB           1       def wrapper(*args, **kwargs):
    31     20.5 MiB      0.0 MiB           1           start_memory = memory_usage()[0]
    32     20.5 MiB      0.0 MiB           1           start_time = default_timer()
    33     50.7 MiB     30.2 MiB           1           result = fun(*args, **kwargs)
    34     50.7 MiB      0.0 MiB           1           res_memory = memory_usage()[0] - start_memory
    35     50.7 MiB      0.0 MiB           1           res_time = default_timer() - start_time
    36     50.7 MiB      0.0 MiB           1           print(f'Время: {res_time} Память: {res_memory}')
    37     50.7 MiB      0.0 MiB           1           return result
    
Использование списка с элементами наиболее оптимально по использованию памяти, однако по скорости выполнения
списковое включение немного быстрее.
"""
print('=+=' * 50)


@profile
@time_profiler
def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


@profile
@time_profiler
def func_2(nums):
    new_arr = [num for num in range(len(nums)) if nums[num] % 2 == 0]
    return new_arr


list_for_fun = [i for i in range(1, 1000000)]
func_1(list_for_fun)
func_2(list_for_fun)
"""
Результат:
Время: 1.2966885 Память: 19.296875
Время: 0.6111095999999998 Память: 19.1171875

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    30     58.0 MiB     58.0 MiB           1       def wrapper(*args, **kwargs):
    31     58.0 MiB      0.0 MiB           1           start_memory = memory_usage()[0]
    32     58.0 MiB      0.0 MiB           1           start_time = default_timer()
    33     77.3 MiB     19.3 MiB           1           result = fun(*args, **kwargs)
    34     77.3 MiB      0.0 MiB           1           res_memory = memory_usage()[0] - start_memory
    35     77.3 MiB      0.0 MiB           1           res_time = default_timer() - start_time
    36     77.3 MiB      0.0 MiB           1           print(f'Время: {res_time} Память: {res_memory}')
    37     77.3 MiB      0.0 MiB           1           return result
    
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    30     58.2 MiB     58.2 MiB           1       def wrapper(*args, **kwargs):
    31     58.2 MiB      0.0 MiB           1           start_memory = memory_usage()[0]
    32     58.2 MiB      0.0 MiB           1           start_time = default_timer()
    33     77.3 MiB     19.1 MiB           1           result = fun(*args, **kwargs)
    34     77.3 MiB      0.0 MiB           1           res_memory = memory_usage()[0] - start_memory
    35     77.3 MiB      0.0 MiB           1           res_time = default_timer() - start_time
    36     77.3 MiB      0.0 MiB           1           print(f'Время: {res_time} Память: {res_memory}')
    37     77.3 MiB      0.0 MiB           1           return result
    
Использование спискового включения дает преимущество по использованию процессорного времени, однако по 
количеству памяти результаты идентитичный, на уровне погрешности.
"""
print('-=-' * 50)

data = {'User_1': {'Orders': ['iPhone 11', 'Laptop Lenovo', 'Mouse 4tech', 'Monitor loc']},
        'User_2': {'Orders': ['Samsung', 'test']},
        'User_3': {'Orders': ['Xiaomi', 'check_123', 'kyocera']},
        'User_4': {'Orders': ['Dell', 'deck_pro']},
        'User_5': {'Orders': ['HDMI HUB', 'recorder', 'micro']}
        }

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f)

user_to_search = 'User_5'


@time_profiler
@profile
def json_search(user, order):
    with open('data.json', 'r', encoding='utf-8') as file:
        data_for_search = json.load(file)
        if data_for_search[user]['Orders'] == order:
            return f'True, {order}'


@time_profiler
@profile
def dict_search(user, data_for_search, order):
    if data_for_search[user]['Orders'] == order:
        return f'True, {order}'


json_search(user_to_search, 'recorder')
dict_search(user_to_search, data, 'recorder')
print(f'JSON: {asizeof.asizeof(json.dumps(data))}')
print(f'DICT: {asizeof.asizeof(data)}')
"""
Результаты:
Время: 0.1572978 Память: 0.36328125
Время: 0.10903960000000001 Память: 0.0

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   182     69.6 MiB     69.6 MiB           1   @time_profiler
   183                                         @profile
   184                                         def json_search(user, order):
   185     69.7 MiB      0.0 MiB           1       with open('data.json', 'r', encoding='utf-8') as file:
   186     69.7 MiB      0.0 MiB           1           data_for_search = json.load(file)
   187     69.7 MiB      0.0 MiB           1           if data_for_search[user]['Orders'] == order:
   188                                                     return f'True, {order}'
   
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   191     69.7 MiB     69.7 MiB           1   @time_profiler
   192                                         @profile
   193                                         def dict_search(user, data_for_search, order):
   194     69.7 MiB      0.0 MiB           1       if data_for_search[user]['Orders'] == order:
   195                                                 return f'True, {order}'
   
JSON: 336
DICT: 3080

Представленные 2 функции имеют схожий алгоритм, потребление процессорного времени и памяти находится
на уровне погрешности в целом идентично, однако json файл в несколько раз меньше чем обычный словарь
"""
