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

import memory_profiler
from numpy import array
from pympler import asizeof
from timeit import default_timer
from collections import OrderedDict


def decor(func):
    def wrapper(*args, **kwargs):
        memory_start = memory_profiler.memory_usage()    # начало замера памяти
        time_start = default_timer()    # начало замера времени
        func(*args, **kwargs)    # начало замера функции (к которым декоратор применяется)
        time_diff = default_timer() - time_start    # окончание замера времени
        memory_end = memory_profiler.memory_usage()    # окончание замера памяти
        mem_diff = memory_end[0] - memory_start[0]
        return f'Выполнение заняло памяти: {mem_diff} MiB \n' \
               f'И времени: {time_diff} \n'

    return wrapper

# скрипт 1
# ДЗ-4, задание 3 (из имеющегося числа сформировать обратное число)
# взят свой вариант (по ТЗ), не преподавателя


# изменим немного условия
# предположим у нас имеется список большой длины
enter_number_1 = [i for i in range(10000)]


@decor
def revers_1():    # вариант без изменений. Выполнение заняло памяти: 1.5515625 MiB, времени: 1.5075537000011536
    new_list = []
    num_position = 1
    for i in str(enter_number_1):
        new_list.insert(-num_position, i)
        num_position = num_position + 1
    # print(asizeof.asizeof(new_list))
    return new_list    # 500744


@decor
def revers_2():    # изменённый вариант. Выполнение заняло памяти: 0.0 MiB, времени: 0.003859500000544358
    new_list_1 = reversed([i for i in str(enter_number_1)])
    # print(asizeof.asizeof(new_list))
    return new_list_1     # 500792


print(revers_1())
print(revers_2())


"""в функция revers_2: вместо цикла использован генератор и одновременно функция reversed.
размер списков: примерно одинаков;
время выполнения: 0.003859500000544358 против 1.5075537000011536 у исходной;
память: 0.0 МБ против 1.5515625 МБ у исходной функции.
Итог: удалось снизить использование памяти (плюс сильно ускорить функцию)"""

# скрипт 2
# ДЗ-3, задание 1. (заполнение списка и словаря программно, выполниние набора операций и со списком, и со словарем)
# порядок следования: сначала пример, затем его улучшенная часть

first_list = []
first_list_1 = []
first_dictionary = {}
first_dictionary_1 = {}
second_list = []
second_list_1 = []
second_dictionary = {}
second_dictionary_1 = {}
number_operations = 1000000


@decor    # начальный пример (создание списка)
def append_list(lst, x):    # Выполнение заняло памяти: 38.32421875 MiB, И времени: 0.12531329999910668
    for i in range(x):
        lst.append(i)
    # print(asizeof.asizeof(lst))
    # print('время заполнения списка - ')
    return lst    # размер 40448720 байт


@decor    # изменённая версия (создание списка)
def append_list_1(lst_1, x):    # Выполнение заняло памяти: 0.63671875 MiB, И времени: 0.10525219999544788
    lst_1 = lst_1 + ([i for i in range(x)])    # использование генератора помогает ускорить создание массива
    # print(asizeof.asizeof(lst_1))
    # print('время заполнения списка - ')
    return lst_1    # размер 40000048 байт


print(append_list(first_list, number_operations))    # начальный пример
print(append_list_1(first_list_1, number_operations))    # изменённая версия

"""
функция append_list_1: использован генератор списков.
время выполнения: примерно одинаковое с изначальной функцией (append_list);
размер спика: стал меньше - 40000048 против 40448720 байт;
память: использование стало не более 1 МБ сверх выделенного,
против 38 МБ у изначальной функции.
Итог: в данном случае мы добились уменьшения потребления памяти при выполнении функции
"""


@decor    # начальный пример (создание словаря)
def append_dictionary(dictionary, x):    # Выполнение заняло памяти: 70.65234375 MiB, И времени: 0.14390649998676963
    for i in range(x):
        dictionary[i] = i
    # print('время заполнения словаря - ')
    # print(asizeof.asizeof(dictionary))
    return dictionary    # размер 73943128


@decor    # изменённая версия (создание словаря)
def append_dictionary_1(dictionary_1, x):    # Выполнение заняло памяти: 1.8828125 MiB, И времени: 0.2801746999994066
    # dictionary_1[(i for i in range(x))] = ({i for i in range(x)})
    dictionary_1 = array({i: i * i for i in range(x)})
    # print('время заполнения словаря - ')
    # print(asizeof.asizeof(dictionary_1))
    return dictionary_1    # размер 112


print(append_dictionary(first_dictionary, number_operations))    # начальный пример
print(append_dictionary_1(first_dictionary_1, number_operations))    # изменённая версия

"""функция append_dictionary_1: использован LC и модуль array:
время: увеличилось примерно на 10-20% относительно исходной функции; 
размер: словарь - 112 байт против 73943128 у исходной функции;
память: не более 2 МБ сверх выделенного системой против 70 МБ у исходной функции.
Итог: удалось добиться уменьшения использования памяти"""


@decor    # начальный пример (копирование списка)
def operations_list(lst):    # Выполнение заняло памяти: 7.6484375 MiB, И времени: 0.11844799999380484
    for i in lst:
        second_list.append(i)
    # print('время копирования списка - ')
    # print(asizeof.asizeof(second_list))
    return second_list    # размер 40448720 байт


@decor    # изменённая версия (копирование списка)
def operations_list_1(lst, s_list):    # Выполнение заняло памяти: 0.00390625 MiB, И времени: 0.07205769998836331
    s_list = s_list + ([i for i in lst])
    # print('время копирования списка - ')
    # print(asizeof.asizeof(s_list))
    return s_list    # размер 40000048 байт


print(operations_list(first_list))    # начальный пример
print(operations_list_1(first_list, second_list_1))    # изменённая версия

"""функция operations_list_1: вместо цикла использован генератор.
время: примерно в полтора раза быстрее - 0.07205 против 0.11844 у исходной функции;
размер: список - 40000048 байт против 40448720 в исходной функции;
память: используется примено 0.00390625 МБ против 7.6484375 MБ у исходной.
Итог: уменьшение использования памяти удалось достигнуть."""


@decor    # начальный пример (копирование словаря)
def operations_dictionary(dictionary):    # Выполнение заняло памяти: 40.34375 MiB, И времени: 0.2272960999980569
    for i in dictionary:
        second_dictionary[i] = dictionary[i]
    # print('время копирования словаря - ')
    # print(asizeof.asizeof(second_dictionary))
    return second_dictionary    # размер 73943128


@decor    # изменённая версия (копирование словаря)
def operations_dictionary_1(dictionary, s_dict):    # Выполнение заняло памяти: 0.01171875 MiB,
                                                    # И времени: 0.19256659999882686
    s_dict = array({i: i for i in dictionary})
    # print('время копирования словаря - ')
    # print(asizeof.asizeof(s_dict))
    return s_dict    # размер 112


print(operations_dictionary(first_dictionary))    # начальный пример
print(operations_dictionary_1(first_dictionary, second_dictionary_1))    # изменённая версия

"""функция operations_dictionary_1: использован генератор и модуль array.
время: чуть быстрее исходного - примерно на 10%;
размер: словарь - 112 байт против 73943128 у исходной функции;
память: 0.01171875 МБ против 40.34375 МБ у исходной функции.
Итог: удалось снизить потребление памяти при выполнении функции."""

# скрипт 3
# ДЗ-5, задание 4
# Поработайте с обычным словарем и OrderedDict.
# Выполните операции, равные по смыслу, с каждым из объектов и сделайте замеры

dictionary_list = {}
dictionary_list_1 = {}
ordered_dict_list = OrderedDict({})
ordered_dict_list_1 = OrderedDict({})
number_fill = 1000000


# неизменённый вариант
@decor
def fill_dictionary():    # заполнение словаря - заняло памяти: 1.08203125 MiB, времени 0.30951810000260593
    dictionary_list = {i: i * i for i in range(number_fill)}
    # print(asizeof.asizeof(dictionary_list))
    return dictionary_list    # 105942584


@decor
def fill_ordered_dict():    # заполнение OrderedDict - заняло памяти: 0.3125 MiB, времени: 0.28294610000011744
    ordered_dict_list = {i: i * i for i in range(number_fill)}
    # print(asizeof.asizeof(ordered_dict_list))
    return ordered_dict_list    # 105942584


print(fill_dictionary(), '\n', fill_ordered_dict())


# изменённый вариант

@decor
def fill_dictionary_1():    # заполнение словаря Выполнение заняло памяти: -0.25390625 MiB
                            # И времени: 0.2785031999992498
    dictionary_list_1 = array({i: i * i for i in range(number_fill)})
    # print(asizeof.asizeof(dictionary_list_1))
    return dictionary_list_1    # 100408, после array 112


@decor
def fill_ordered_dict_1():    # заполнение словаря OrderedDict Выполнение заняло памяти: 0.0 MiB
                              # И времени: 0.29854389999673003
    ordered_dict_list_1 = array({i: i * i for i in range(number_fill)})
    # print(asizeof.asizeof(ordered_dict_list_1))
    return ordered_dict_list_1    # 100408, после array 112


print(fill_dictionary_1(), '\n', fill_ordered_dict_1())

"""функция fill_dictionary_1 и fill_ordered_dict_1: использован модуль array.
Время: примерно одинаковое;
размер: словарь - 112 байт против 105942584 у исходных функций;
память: не выходит за пределы, выделенные в системе.
Итог: удалось добиться некоторого сокращения использования памяти."""

