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


test_dict = dict((int(n), int(n)) for n in range(1000000))
test_list = list((int(n)) for n in range(1000000))


def time_check(func):
    def wrapper(n):
        start = time.time()
        func(n)
        end = time.time()
        return end - start
    return wrapper


@time_check
def list_filling(input_list):
    list1 = []
    for i in input_list:
        list1.append(i)
    return list1


@time_check
def dict_filling(input_dict):
    dict1 = {}
    for key, value in input_dict.items():
        dict1[key] = value
    return dict1


@time_check
def list_search(input_list):
    input_list.index(500000)


@time_check
def dict_search(input_dict):
    input_dict.get(500000, 0)


@time_check
def list_clear(input_list):
    return input_list.clear()


@time_check
def dict_clear(input_dict):
    return input_dict.clear()


print(list_filling(test_list))  # 0.04064822196960449
print(dict_filling(test_dict))  # 0.08363580703735352 Словарь заполняется почти в два раза дольше
print(list_search(test_list))  # 0.004428863525390625
print(dict_search(test_dict))  # 2.6226043701171875e-06 ~(0,00000262)
# Поиск по словарю происходит гораздо быстрее благодаря использованию хеша
print(list_clear(test_list))  # 0.009126424789428711
print(dict_clear(test_dict))  # 0.008687973022460938 И словарь список отчищаются с примерно равной скоростью
