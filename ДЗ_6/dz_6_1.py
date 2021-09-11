"""Профилировка затрат памяти"""
import json
from random import randint

import memory_profiler
from memory_profiler import profile
from numpy import array
from pympler import asizeof


def decorator(func):
    def wrapper(*args, **kwargs):
        mem_1 = memory_profiler.memory_usage()
        res = func(*args, **kwargs)
        mem_2 = memory_profiler.memory_usage()
        mem_diff = mem_2[0] - mem_1[0]
        return res, mem_diff

    return wrapper


# ls_values = []
# dict_values = {}

@decorator
def fill_in_list(len_of_seq: int):
    """
    Заполнение списка случайными числами и строками
    Сложность O(N)
    1.3358 сек. для N = 1 млн.
    """
    ls_values = []
    for i in range(len_of_seq):
        rand = randint(32, 127)
        # выбираем либо число в диапазоне [32;127] либо случайную строку дл. в 5 сиволов
        ls_values.append(chr(rand) * 5 if randint(0, 1) else rand)
    return ls_values

@decorator
def fill_in_list2(len_of_seq: int):

    return array([chr(randint(32, 127)) * 5 if randint(0, 1) else randint(32, 127)
                  for _ in range(len_of_seq)])

@decorator
def fill_in_list3(len_of_seq: int):
    ls_values3 = []
    for i in range(len_of_seq):
        rand = randint(32, 127)
        # выбираем либо число в диапазоне [32;127] либо случайную строку дл. в 5 сиволов
        ls_values3.append(chr(rand) * 5 if randint(0, 1) else rand)
    yield ls_values3


@decorator
def fill_in_dict(len_of_seq: int):
    """
    Заполнение словаря случайными числами и строками
    Сложность O(N)
    2.1423 сек. для N = 1 млн.
    """
    dict_values ={}

    for i in range(len_of_seq):
        rand = randint(32, 127)
        # выбираем либо число в диапазоне [32;127] либо случайную строку дл. в 5 сиволов
        dict_values[f'key{i :07d}'] = chr(rand) * 5 if randint(0, 1) else rand
    return dict_values

@decorator
def fill_in_dict2(len_of_seq: int):
        dict_vals = {f'key{i :07d}': chr(randint(32, 127)) * 5 if randint(0, 1) else randint(32, 127)
                for i in range(len_of_seq)}
        return json.dumps(dict_vals)

@decorator
def fill_in_dict3(len_of_seq: int):
        dict_vals = {f'key{i :07d}': chr(randint(32, 127)) * 5 if randint(0, 1) else randint(32, 127)
                for i in range(len_of_seq)}
        yield dict_vals

# Получение четных чисел
@decorator
def evens(nums):
    return [i for i in range(nums) if i % 2 == 0]

@decorator
def evens2(nums):
    return array([i for i in range(nums) if i % 2 == 0])


@decorator
def evens3(nums):
    yield [i for i in range(nums) if i % 2 == 0]

if __name__ == "__main__":
    res, mem_diff = fill_in_list(100000)
    print(f"Выполнение заняло {mem_diff} Mib")

    res, mem_diff = fill_in_list2(100000)
    print(f"Выполнение заняло {mem_diff} Mib")

    res, mem_diff = fill_in_list3(100000)
    print(f"Выполнение заняло {mem_diff} Mib")
    """
    Выполнение заняло 4.578125 Mib
    
    Выполнение заняло 3.90625 Mib
    Модифицированная функция fill_in_list2 оптимизирована.
    Потребление памяти уменьшилось за счет использования numpay.
    
    Выполнение заняло 0.0 Mib 
    Модифицированная функция fill_in_list3 оптимизирована. 
    Потребление памяти практически не заметно. 
    Это произошло за счет использования генераторов
    """

    res, mem_diff = fill_in_dict(100000)
    print(f"Выполнение заняло {mem_diff} Mib")
    print(asizeof.asizeof(res))

    res, mem_diff = fill_in_dict2(100000)
    print(f"Выполнение заняло {mem_diff} Mib")
    print(asizeof.asizeof(res))

    res, mem_diff = fill_in_dict3(100000)
    print(f"Выполнение заняло {mem_diff} Mib")
    print(asizeof.asizeof(res))
    """
    Функция fill_in_dict - не оптимизирована.
    Выполнение заняло 14.3203125 Mib
    14442456
    
    Функция fill_in_dict2 оптимизирована с помощью json -модуля.
    Т.к. json занимает меньше памяти, результаты на лицо.
    Выполнение заняло 3.10546875 Mib
    2084024
    
    Функция fill_in_dict3 оптимизирована, также с помощью генератора.
    Т.е. мы получаем данные в процессе вычисления. Результаты:
    Выполнение заняло 0.0 Mib
    440
    """
    res, mem_diff = evens(100000)
    print(f"Выполнение заняло {mem_diff} Mib")
    print(asizeof.asizeof(res))

    res, mem_diff = evens2(100000)
    print(f"Выполнение заняло {mem_diff} Mib")
    print(asizeof.asizeof(res))

    res, mem_diff = evens3(100000)
    print(f"Выполнение заняло {mem_diff} Mib")
    print(asizeof.asizeof(res))

    """
    Функция evens - не оптимизирована.
    Выполнение заняло 14.3203125 Mib
    14442456

    Функция evens2 оптимизирована с помощью numpy -модуля.
    Мы видим что библиотека крайне эффективна. И дает экономию 
    памяти почти в 5 раз. 
    Выполнение заняло 3.10546875 Mib
    2084024

    Функция evens3 оптимизирована, также с помощью генератора.
    Т.е. мы получаем данные в процессе вычисления. Результаты:
    Выполнение заняло 0.0 Mib
    432
    """

