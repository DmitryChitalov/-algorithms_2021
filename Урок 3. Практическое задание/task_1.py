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
import time
import random


def timing(method):
    def timed(*args, **kwargs):
        start = time.monotonic()
        result = method(*args, **kwargs)
        print(f'Время выполнения функции "{method.__doc__}": {round((time.monotonic() - start) * 1000, 2)} мс')
        return result
    return timed


@timing
def fill_list():
    """заполнение списка"""
    my_list = [random.randint(1, 1000) for i in range(10000000)]
    return my_list


@timing
def fill_dict():
    """заполнение словаря"""
    my_dict = {i: random.randint(1, 1000) for i in range(10000000)}
    return my_dict


@timing
def search_list(source_list, num):
    """поиск в списке"""
    return num in source_list


@timing
def search_dict(source_dict, num):
    """поиск в словаре"""
    return num in source_dict


# выполним поиск заведомо несуществующих элементов
print(search_list(fill_list(), -1))
print(search_dict(fill_dict(), -1))

# Словарь заполняется дольше. Но поиск в словаре производится практически мгновенно
