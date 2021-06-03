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


def time_decor(func):
    def user_func(num):
        start = time()
        result = func(num)
        print(f'Время операции: {time() - start} сек.')
        return result

    return user_func


@time_decor
def filling_list(number):
    result = [el for el in range(number)]
    return result


@time_decor
def filling_dict(number):
    result = {el: el for el in range(number)}
    return result


numbers = 100000000
my_list = filling_list(numbers)
my_dict = filling_dict(numbers)


# Чуть медленне идет заполнение словаря так как идет заполнение хеш таблицы

@time_decor
def clear_list(some_list: list):
    some_list.clear()


@time_decor
def clear_dict(some_dict: dict):
    some_dict.clear()


clear_list(my_list)
clear_dict(my_dict)


# Чуть быстрее, но не значительно происходит очищение в списке.

@time_decor
def copy_list(some_list):
    new_list = some_list.copy()
    return new_list


@time_decor
def copy_dict(some_dict):
    new_dict = some_dict.copy()
    return new_dict


copy_list(my_list)
copy_dict(my_dict)

# В обоих случаях опарация копирования происходит мнгновенно
