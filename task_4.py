"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
from collections import OrderedDict
from timeit import timeit


def create_dct():
    dct = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10}
    return dct


def create_odct():
    odct = OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5),
                    ('f', 6), ('g', 7), ('h', 8), ('i', 9), ('j', 10)])
    return odct


dct = create_dct()
odct = create_odct()


def iterate(dict):
    for key, value in dict.items():
        print(key, "->", value)


print("Замеры времени для функций создания обычного и упорядоченного словарей: ")
dct_time = timeit("create_dct()", globals=globals(), number=100)
print(f"Dict: {dct_time}")
odct_time = timeit("create_odct()", globals=globals(), number=100)
print(f"OrderedDict: {odct_time}")

print("Замеры времени для функции values обычного и упорядоченного словарей: ")
dct_time = timeit("dct.values()", globals=globals(), number=100)
print(f"Dict: {dct_time}")
odct_time = timeit("odct.values()", globals=globals(), number=100)
print(f"OrderedDict: {odct_time}")

print("Замеры времени для функции keys обычного и упорядоченного словарей: ")
dct_time = timeit("dct.keys()", globals=globals(), number=100)
print(f"Dict: {dct_time}")
odct_time = timeit("odct.keys()", globals=globals(), number=100)
print(f"OrderedDict: {odct_time}")

print("Замеры времени для функции update обычного и упорядоченного словарей: ")
dct_time = timeit("dct.update({3: 5})", globals=globals(), number=100)
print(f"Dict: {dct_time}")
odct_time = timeit("odct.update({3: 5})", globals=globals(), number=100)
print(f"OrderedDict: {odct_time}")

print("Замеры времени для функции items обычного и упорядоченного словарей: ")
dct_time = timeit("dct.items()", globals=globals(), number=100)
print(f"Dict: {dct_time}")
odct_time = timeit("odct.items()", globals=globals(), number=100)
print(f"OrderedDict: {odct_time}")

print("Замеры времени для итерации элементов обычного и упорядоченного словарей: ")
dct_time = timeit("iterate(dct)", globals=globals(), number=100)
print(f"Dict: {dct_time}")
odct_time = timeit("iterate(odct)", globals=globals(), number=100)
print(f"OrderedDict: {odct_time}")

"""
Замеры времени для функций создания обычного и упорядоченного словарей: 
Dict: 5.360000000000087e-05
OrderedDict: 0.00023019999999999985

Замеры времени для функции values обычного и упорядоченного словарей: 
Dict: 8.899999999999186e-06
OrderedDict: 1.0200000000001874e-05

Замеры времени для функции keys обычного и упорядоченного словарей: 
Dict: 8.099999999996998e-06
OrderedDict: 8.700000000000374e-06

Замеры времени для функции update обычного и упорядоченного словарей: 
Dict: 1.4800000000002311e-05
OrderedDict: 2.8300000000001935e-05
Замеры времени для функции items обычного и упорядоченного словарей: 
Dict: 4.9999999999980616e-06
OrderedDict: 5.100000000000937e-06

Замеры времени для итерации элементов обычного и упорядоченного словарей: 
Dict: 0.012615599999999998
OrderedDict: 0.015033499999999998

Обычный словарь заполняется быстрее упорядосенного, да и все рассмотренные функции занимают меньше времени выполнения.
Таким образом, использовать OrderedDict в 3.6 и более поздних версиях использовать особо смысла нет
"""