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


fill_in_list(1_000_000)
# print(ls_values)
fill_in_dict(1_000_000)


# print(ls_values)

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


get_ls_element_by_index(ls_values, 10_000)


@timer_func
def get_dict_val_by_key(dictionary: dict, key: str):
    """
    Получает значение по ключу
    Сложность O(1)
    0.0000 сек. для N = 1 млн.
    """
    return dictionary[key]


get_dict_val_by_key(dict_values, "key0000101")


@timer_func
def del_ls_element_by_ind(ls: list, ind: int = -1):
    """
    Удаляет значение
    Сложность O(N) для ind = 0   (за 0.0010 сек. для N = 1 млн.)
    Сложность O(1) для ind = -1  (за 0.0000 сек. для N = 1 млн.)
    """
    ls.pop(ind)


del_ls_element_by_ind(ls_values, 0)


@timer_func
def del_dict_key(dictionary: dict, key: str):
    """
    Удаляет значение по ключу
    Сложность O(1)
    0.0000 сек. для N = 1 млн.
    """
    dictionary.pop(key)


del_dict_key(dict_values, 'key0000010')


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


insert_element_to_list(ls_values, 0)
