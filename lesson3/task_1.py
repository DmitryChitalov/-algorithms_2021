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
from random import randint
import time

lst = []
dct = {}


def time_of_function(function):
    def wrapped(*args):
        start_time = time.time()
        res = function(*args)
        print(time.time() - start_time)
        return res
    return wrapped



def comp_lst(range_count):
    for el in range(range_count):
        lst.append(randint(1, 100))


@time_of_function
def comp_dct(range_count):
    for el in range(range_count):
        key = f"key{randint(1, 100)}"
        dct[key] = randint(1, 100)


@time_of_function
def lst_op(sum_el):
    for i in range(len(lst)):
        lst[i] += sum_el


@time_of_function
def dct_op(sum_el):
    for key, value in dct.items():
        dct[key] += sum_el


print("Время работы заполнения списка: ")
comp_lst(1000000)
print("Время работы заполнения словаря: ")
comp_dct(1000000)
print("Время работы операций со списком: ")
lst_op(10)
print("Время работы операций со словарем: ")
dct_op(10)

# Создание словаря выполняется медленнее, чем списка, но поиск происходит в разы быстрее
# Все из-за того, что словари индексируются по ключам