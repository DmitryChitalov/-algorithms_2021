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
from random import randint


def timer(function):
    def wrapped_func(value):
        start_time = time()
        result = function(value)
        print(f'Время, потраченное на операцию: {round(time() - start_time, 3)} сек.')
        return result
    return wrapped_func


@timer
def get_list(number):
    print(f'Наполнение списка {number} элементами.', end=' ')
    result = [el for el in range(number)]
    return result


@timer
def get_dict(number):
    print(f'Наполнение словаря {number} элементами.', end=' ')
    result = {el: el for el in range(number)}
    return result


number_of_elements = 1000000
my_list = get_list(number_of_elements)  # 0.108 сек.
my_dict = get_dict(number_of_elements)  # 0.189 сек.
# Медленнее происходит заполнение словаря из-за создания хешей


@timer
def get_value_from_list(some_list: list):
    print('Получение индекса рандомного числа в списке.', end=' ')
    some_list.index(randint(0, number_of_elements))


@timer
def get_value_from_dict(some_dict: dict):
    print('Поиск рандомного числа по ключу в словаре.', end=' ')
    some_dict.get(randint(0, number_of_elements))


get_value_from_list(my_list)  # 0.02 сек.
get_value_from_dict(my_dict)  # 0.0 сек.
# Поиск в словаре происходит быстрее благодаря хешам, сложность - константная
# В списке сложность поиска элемента - линейная


@timer
def clear_list(some_list: list):
    print('Очищение списка.', end=' ')
    some_list.clear()


@timer
def clear_dict(some_dict: dict):
    print('Очищение словаря.', end=' ')
    some_dict.clear()


clear_list(my_list)  # 0.014 сек.
clear_dict(my_dict)  # 0.018 сек.
# Очищение списка и словаря дают почти одинаковое время
# словарь очищается на десятые доли дольше из-за удаления хешей
