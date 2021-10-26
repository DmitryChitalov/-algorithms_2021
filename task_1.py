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

from time import time


def check_speed(func):
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print(f'{func.__name__}\n'
              f' {end - start}')
        return result

    return wrapper


@check_speed
def filling_dct(n):
    test_dct = dict()
    for el in range(n):
        test_dct[el] = el
    return test_dct


@check_speed
def filling_lst(n):
    test_lst = []
    for el in range(n):
        test_lst.append(el)
    return test_lst


dictionary = filling_dct(5 * 10 ** 6)
list_test = filling_lst(5 * 10 ** 6)
"""
filling_dct
0.8806960582733154
filling_lst
0.4499058723449707
Cловарь заполняется медленнее, так как словарь посторен на хеш-таблицах -> затрачивается время на вычисления хеша.
"""


@check_speed
def dct_pop(test_dct):
    for i in range(1000):
        test_dct.pop(i)


@check_speed
def lst_pop(test_lst):
    for i in range(1000):
        test_lst.pop(i)


dct_pop(dictionary)
lst_pop(list_test)
"""
dct_pop
 0.0
lst_pop
 7.584824800491333
 Если рассматривать случай удаления элементов, то работа со словарем проходит за очень малый промежуток времени,
 в то время как список даже с весьма небольшим количеством элементов справляется медленно. 
 Это связано с быстрым доступам по ключам в словарях.
"""