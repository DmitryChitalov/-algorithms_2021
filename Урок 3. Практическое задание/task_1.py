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
import random


def measure_function(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        delta = end_time - start_time
        print(delta)
    return wrapper


@measure_function
def fill_list():
    test_list = []
    for iterator in range(10000000): # добавляем к списку миллион рандомных элементов
        test_list.append(random.choice((0, 999)))
    print("List has been filled")


@measure_function
def fill_dict():
    test_dict = {}
    for iterator in range(10000000): # добавляем к списку миллион рандомных элементов
        test_dict[iterator] = random.choice((0, 999))
    print("Dict has been filled")


fill_list()
fill_dict()
