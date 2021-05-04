"""
Задание 1.

Реализуйте свои пользовательские функции, в которых реализуйте:

a) заполнение списка и словаря,
   сделайте замеры и сделайте выводы, что выполняется быстрее и почему
b) выполните набор операций и со списком, и со словарем,
   сделайте замеры и сделайте выводы, что и где выполняется быстрее и почему

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор для подсчета времени работы ваших пользовательских функций
И примените ее к своим функциям!

Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.
"""
from time import time


def time_measure(func):
    def inner(*args, **kwargs):
        start = time()
        res = func(*args, **kwargs)
        end = time()
        print(f'time executing {func.__name__} - {end - start}')
        return res

    return inner


@time_measure
def fill_list() -> list:
    return [i for i in range(1000000)]


@time_measure
def fill_dict() -> dict:
    return {i: i for i in range(1000000)}


@time_measure
def list_append(lst: list):
    for i in range(1000000, 2000000):
        lst.append(1)


@time_measure
def list_remove(lst: list):
    for i in range(1000000):
        lst.pop(-1)


@time_measure
def list_get(lst: list):
    for i in range(1000000):
        el = lst[i]


@time_measure
def dict_add(dct: dict):
    for i in range(1000000, 2000000):
        dct[i] = i


@time_measure
def dict_remove(dct: dict):
    for i in range(1000000, 2000000):
        del dct[i]


@time_measure
def dict_get(dct: dict):
    for i in range(1000000):
        el = dct[i]


if __name__ == '__main__':
    lst = fill_list()
    dct = fill_dict()
    list_append(lst)
    list_remove(lst)
    list_get(lst)
    dict_add(dct)
    dict_remove(dct)
    dict_get(dct)


# time executing fill_list - 0.0658261775970459 - заполнение list происходит быстрей
# time executing fill_dict - 0.11584591865539551

# time executing list_append - 0.08405804634094238 - добавление элментов в list быстрей
# time executing list_remove - 0.14641618728637695 - удаление элемента из list по индексу медленей
# time executing list_get - 0.04831886291503906 - получение элемента по индексу быстрей
# time executing dict_add - 0.11618924140930176
# time executing dict_remove - 0.07872819900512695
# time executing dict_get - 0.06160378456115723
