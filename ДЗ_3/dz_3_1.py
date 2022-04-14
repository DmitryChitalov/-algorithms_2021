from random import randint
from time import time


def timer_func(func):
    """
    Декоратор - таймер выполнения
    """

    def wrap_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'Функция {func.__name__!r} выполнена за {(t2 - t1):.4f} сек.')
        return result

    return wrap_func


ls_values = []
dict_values = {}


@timer_func
def fill_in_list(len_of_seq: int):
    """
    Заполнение списка случайными числами и строками
    Сложность O(N)
    1.3358 сек. для N = 1 млн.
    """

    for i in range(len_of_seq):
        rand = randint(32, 127)
        # выбираем либо число в диапазоне [32;127] либо случайную строку дл. в 5 сиволов
        ls_values.append(chr(rand) * 5 if randint(0, 1) else rand)


@timer_func
def fill_in_dict(len_of_seq: int):
    """
    Заполнение словаря случайными числами и строками
    Сложность O(N)
    2.1423 сек. для N = 1 млн.
    """
    for i in range(len_of_seq):
        rand = randint(32, 127)
        # выбираем либо число в диапазоне [32;127] либо случайную строку дл. в 5 сиволов
        dict_values[f'key{i :07d}'] = chr(rand) * 5 if randint(0, 1) else rand


@timer_func
def get_ls_element_by_index(ls: list, ind: int):
    """
    Получает элемент списка по индексу
    Сложность O(1)
    0.0000 сек. для N = 1 млн.
    """
    if ind > len(ls) - 1:
        ind = -1
    return ls[ind]


@timer_func
def get_dict_val_by_key(dictionary: dict, key: str):
    """
    Получает значение по ключу
    Сложность O(1)
    0.0000 сек. для N = 1 млн.
    """
    return dictionary[key]


@timer_func
def del_ls_element_by_ind(ls: list, ind: int = -1):
    """
    Удаляет значение
    Сложность O(N) для ind = 0   (за 0.0010 сек. для N = 1 млн.)
    Сложность O(1) для ind = -1  (за 0.0000 сек. для N = 1 млн.)
    """
    ls.pop(ind)


@timer_func
def del_dict_key(dictionary: dict, key: str):
    """
    Удаляет значение по ключу
    Сложность O(1)
    0.0000 сек. для N = 1 млн.
    """
    dictionary.pop(key)


@timer_func
def insert_element_to_list(ls: list, ind: int):
    """
    вставка элемента в словарь
    Сложность O(N)
    Сложность O(1) при ind=len(ls)
    0.0010 сек. для N = 1 млн.
    0.0000 сек. для N = 1 млн. при ind=len(ls)
    """
    rand = randint(32, 127)
    ls.insert(ind, chr(rand) * 5 if randint(0, 1) else rand)


DURATION = 1_000_000
fill_in_list(DURATION)
fill_in_dict(DURATION)
"""
Вывод: Заполнение списка присходит быстрее при одинаковой сложности O(N),
т.к. словарь тратит время на создание и управлением хэшами 
"""

get_ls_element_by_index(ls_values, 0)
get_dict_val_by_key(dict_values, "key0000101")
"""
Вывод: Получение элемента как для словаря таки и для списка 
происходит одинаково быстро, при одинаковой сложности O(N).
т.к. список получает значение по индексу, а словарь имеет хэш-таблицу
в которой ключи находяться в хэшируемом виде, а хэш своего рода индекс. 
"""

del_ls_element_by_ind(ls_values, 0)
del_ls_element_by_ind(ls_values, -1)
del_dict_key(dict_values, 'key0000010')
"""
Вывод: Удаление элементов в словаре и в списке последнего элемента 
происходит за равное количество времени, очень быстро, сложность O(1).
Однако удаление элементов в начале списка замедляется. Удаление самого первого
элемента дает сложность O(N)
"""

insert_element_to_list(ls_values, 0)
"""
Вывод: Вставка элементов в список имеет сложность O(N), 
о чем счвидетельствует замеренное время выполнения. 
Это связано с динамическим перестроением массивов составляющих список.
"""
