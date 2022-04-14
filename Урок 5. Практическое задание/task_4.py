"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
from collections import OrderedDict
from timeit import timeit


# Создание словаря
def fill_dict():
    return {el: el for el in range(500)}


# Создание упорядоченного словаря
def fill_ord_dict():
    return OrderedDict([(el, el) for el in range(500)])


# Изменение словарей (синтаксис одинаковый для обоих видов)
def change(dct):
    for i in dct:
        dct[i] += 1
    return dct


# Извлечение элементов словаря (синтаксис одинаковый для обоих видов)
def extract(dct):
    for k, v in dct.items():
        pass
    return dct


# Очистка словаря (синтаксис одинаковый для обоих видов)
def clear(dct):
    dct.clear()
    return dct


test_dict = fill_dict()
test_ord_dict = fill_ord_dict()

print('Создание и наполнение словаря', timeit('fill_dict()', globals=globals(), number=10000))
print('Создание и наполнение упорядоченного словаря', timeit('fill_ord_dict()', globals=globals(), number=10000))

print('Изменение словаря', timeit('change(test_dict)', globals=globals(), number=10000))
print('Изменение упорядоченного словаря', timeit('change(test_ord_dict)', globals=globals(), number=10000))

print('Извлечение элементов словаря', timeit('extract(test_dict)', globals=globals(), number=10000))
print('Извлечение элементов упорядоченного словаря', timeit('extract(test_ord_dict)', globals=globals(), number=10000))

print('Очистка словаря', timeit('clear(test_dict)', globals=globals(), number=10000))
print('Очистка упорядоченного словаря', timeit('clear(test_ord_dict)', globals=globals(), number=10000))

# Результаты
# Создание и наполнение словаря 0.2402801
# Создание и наполнение упорядоченного словаря 0.6582808
# Изменение словаря 0.34129030000000005
# Изменение упорядоченного словаря 0.4889540000000001
# Извлечение элементов словаря 0.08896839999999995
# Извлечение элементов упорядоченного словаря 0.1822341999999999
# Очистка словаря 0.0007787999999999684
# Очистка упорядоченного словаря 0.0009348000000000134
# Вывод: исходя из замеров, очевидно, что в версиях питоне выше 3.5 смысла использовать OrderedDict нет,
# т.к. эта коллекция не имеет большего функционала по сравнению с обычными словарями, но работает медленнее
