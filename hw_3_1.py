"""
Задание 1.

Реализуйте свои пользовательские функции, в которых реализуйте:

a) заполнение списка и словаря программно,
   сделайте замеры и сделайте выводы, что выполняется быстрее и почему
b) выполните набор операций и со списком, и со словарем,
   сделайте замеры и сделайте выводы, что и где выполняется быстрее и почему

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор для подсчета времени работы ваших пользовательских функций
И примените ее к своим функциям!
"""

import time


def time_func(func):
    def g(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        stop_time = time.time()
        return result, stop_time - start_time
    return g


@time_func
def create_list(n):
    test_list = [i for i in range(n)]
    return test_list


@time_func
def create_dict(n):
    test_dict = {i: i for i in range(n)}
    return test_dict


@time_func
def add_to_list(test_list, a):
    test_list.append(a)
    return test_list


@time_func
def add_to_dict(test_dict, key, val):
    test_dict.update({key: val})


@time_func
def list_search_el(test_list, a):
    for el in test_list:
        if el == a:
            return el


@time_func
def dict_search_key(test_dict, key):
    return test_dict[key]


@time_func
def dict_search_val(test_dict, a):
    for val in test_dict.values():
        if val == a:
            return val


n = 10000000
test_list = create_list(n)[0]
test_dict = create_dict(n)[0]

print(f'Создать список: {create_list(n)[1]}')
print(f'Создать словарь: {create_dict(n)[1]}')
# Словарь создается дольше, т е для каждого ключа считается хэш
print(f'Добавить элемент в список: {add_to_list(test_list, 11)[1]}')
print(f'Добавить элемент в словарь {add_to_dict(test_dict, -10, 100)[1]}')
# Скорость одинаковая и предельно высокая
print(f'Поиск элемента в списке: {list_search_el(test_list, n - 1)[1]}')
print(f'Поиск  ключа в словаре: {dict_search_key(test_dict, n - 1)[1]}')
print(f'Поиск значения в словаре: {dict_search_val(test_dict, n - 1)[1]}')
# Поиск в словаре по ключу быстрее поиска в списке, т к словарь - хэш таблица
# поиск по значению в словаре дольше чем поиск по списку, т к нужно вычеслять хэш для всех ключей,
# и только после этого сравнивать значения
