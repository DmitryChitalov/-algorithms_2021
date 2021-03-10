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

from random import randrange
from string import ascii_letters
from time import time


lst = []
dct = {}


def timer(func):
    def wrapper(*arg):
        start = time()
        func(*arg)
        end = time()
        print(f'Время выполнения {end - start}')
    return wrapper


def letter_generator(length=5):
    letter = ''
    for i in range(length):
        letter += ascii_letters[randrange(0, 52)]
    return letter


@timer
def list_comp_gen(length):
    fill_list = [letter_generator() for i in range(length)]
    # print(fill_list)


@timer
def dict_comp_gen(length):
    fill_dict = {randrange(0, 100): letter_generator() for _ in range(length)}
    # print(fill_dict)


@timer
def fill_empty_list(length):
    for i in range(length):
        lst.append(i)
    return lst


@timer
def fill_empty_dict(length):
    for i in range(length):
        dct[i] = i*2


@timer
def list_mult():
    for i in range(len(lst)):
        lst[i] *= 5


@timer
def list_pop():
    for i in range(len(lst)):
        lst.pop()


@timer
def dict_mult():
    for k, v in dct.items():
        dct[k] = v * 5


@timer
def dict_pop():
    for i in range(len(dct)):
        dct.pop(i)


# Генерация list comprehension и dictionary comprehension
# list_comp_gen(1000000)
# dict_comp_gen(1000000)
# Генерация списка и словаря циклом
fill_empty_list(1000000)
fill_empty_dict(1000000)
# Операции над списком
list_mult()
list_pop()
# Операции над словарем
dict_mult()
dict_pop()

"""
* - - *
Создание списка и словаря включениями с использованием генерации слов, однако списковое включение справилось быстрее
Время выполнения 5.461132287979126
Время выполнения 6.168671607971191
* - - *
Создание списка и словаря через цикл и снова лидирует список
Время выполнения 0.11043477058410645
Время выполнения 0.1809244155883789
* - - *
Операции со списком, первое это умножение чисел, второе это удаление последнего элемента с его возрватом
Время выполнения 0.11310195922851562
Время выполнения 0.0877532958984375
* - - *
Операции со словарем, первое это умножение чисел, второе это удаление последнего элемента с его возрватом
Время выполнения 0.12529706954956055
Время выполнения 0.13315820693969727
* - - *
Итог: в некоторых операциях словарь должен был опережать по скороспи исполнения список, но возможно из-за
неправильной реализации получились такие результаты, ставящие под сомнение эффективность словарей перед списком.
В идеале словарь работает быстрее списка, если вопрос идет о работе с индексами.
"""
