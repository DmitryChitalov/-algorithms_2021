"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции, равные по смыслу, с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
from collections import OrderedDict

from timeit import timeit


def func_d_1(test_dict):
    test_dict.get(2)


def func_d_2(test_dict):
    test_dict.items()


def func_d_3(test_dict):
    test_dict.popitem()


def func_d_4(test_dict):
    test_dict.setdefault(4, 'Four')


def func_d_5(test_dict):
    test_dict.values()


def func_od_1(test_ord_dict):
    test_ord_dict.get(2)


def func_od_2(test_ord_dict):
    test_ord_dict.items()


def func_od_3(test_ord_dict):
    test_ord_dict.popitem()


def func_od_4(test_ord_dict):
    test_ord_dict.setdefault(4, 'Four')


def func_od_5(test_ord_dict):
    test_ord_dict.values()


testing_dict = {a: a ** 2 for a in range(10010)}
testing_ord_dict = OrderedDict(testing_dict)
print('Метод get в dict: ', timeit("func_d_1(testing_dict)", number=10000, globals=globals()))
print('Метод get в OrderDict: ', timeit("func_od_1(testing_ord_dict)", number=10000, globals=globals()))

print('Метод items в dict: ', timeit("func_d_2(testing_dict)", number=10000, globals=globals()))
print('Метод items в OrderDict: ', timeit("func_od_2(testing_ord_dict)", number=10000, globals=globals()))

print('Метод popitem в dict: ', timeit("func_d_3(testing_dict)", number=10000, globals=globals()))
print('Метод popitem в OrderDict: ', timeit("func_od_3(testing_ord_dict)", number=10000, globals=globals()))

print('Метод setdefault в dict: ', timeit("func_d_4(testing_dict)", number=10000, globals=globals()))
print('Метод setdefault в OrderDict: ', timeit("func_od_4(testing_ord_dict)", number=10000, globals=globals()))

print('Метод values в dict: ', timeit("func_d_5(testing_dict)", number=10000, globals=globals()))
print('Метод values в OrderDict: ', timeit("func_od_5(testing_ord_dict)", number=10000, globals=globals()))

# Вывод: в целом dict и OrderDict в версии 3.8.6 одинаковы.
# Только метод popitem показывает некоторую разницу, dict (0.0016) быстрее OrderDict (0.0026)
# Смысл использования OrderDict в версиях 3.6 и выше есть, но мной пока не изучен =) буду ждать работы с .csv
