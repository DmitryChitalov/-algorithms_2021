"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
from timeit import timeit
from collections import OrderedDict


def input_dct_1(n):  # Сложность O(n)
    dct1 = dict()
    for i in range(n):
        dct1[i] = i
    return dct1


def input_odct_1(n):  # Сложность O(n)
    odct1 = OrderedDict()
    for i in range(n):
        odct1[i] = i
    return odct1


def input_dct_2():  # Сложность O(n^2)
    dct2 = dict()
    for i in dct1:
        for j in dct1:
            dct2[i+j] = i+j
    return dct2


def input_odct_2():  # Сложность O(n^2)
    odct2 = OrderedDict()
    for i in dct1:
        for j in dct1:
            odct2[i+j] = i+j
    return odct2

num = 100
dct1 = input_dct_1(num)
odct1 = input_odct_1(num)

print(timeit("input_dct_1(num)", globals=globals(), number=10000))      # 0.147797131
print(timeit("input_odct_1(num)", globals=globals(), number=10000))     # 0.27464789300000003
print(timeit("input_dct_2()", globals=globals(), number=100))           # 0.20988789400000007
print(timeit("input_odct_2()", globals=globals(), number=100))          # 0.253133638

# Обычный словарь заполняется быстрее, чем OrderedDict, при различных вариантах сложности алгоритма.


def dct1_insert(key, val):     # Сложность O(1)
    dct1[key] = val
    return


def odct1_insert(key, val):     # Сложность O(1)
    odct1[key] = val
    return


def dct1_get(key):              # Сложность O(1)
    return dct1[key]


def odct1_get(key):              # Сложность O(1)
    return odct1[key]


def dct1_get2(key):             # Сложность O(1)
    return dct1.get(key)


def odct1_get2(key):             # Сложность O(1)
    return odct1.get(key)


def dct1_get_key(val):          # Сложность O(n)
    for k, v in dct1.items():
        if val == v:
            return k


def odct1_get_key(val):          # Сложность O(n)
    for k, v in odct1.items():
        if val == v:
            return k


k = 50
v = 'value'

print(timeit("dct1_insert(k, v)", globals=globals(), number=1000000))      # 0.22633136900000006
print(timeit("odct1_insert(k, v)", globals=globals(), number=1000000))     # 0.25070216099999987
print(timeit("dct1_get(k)", globals=globals(), number=1000000))            # 0.15764106499999997
print(timeit("odct1_get(k)", globals=globals(), number=1000000))           # 0.161125784
print(timeit("dct1_get2(k)", globals=globals(), number=1000000))           # 0.18737898200000003
print(timeit("odct1_get2(k)", globals=globals(), number=1000000))          # 0.2070865209999999
print(timeit("dct1_get_key(v)", globals=globals(), number=100000))         # 0.38950718800000006
print(timeit("odct1_get_key(v)", globals=globals(), number=100000))        # 0.646991485

# Все операции с обычным словарем выполняются быстрее, чем аналогичные операции с OrderedDict.
# Cмысла исп-ть OrderedDict в Python 3.6 и более поздних версиях НЕТ.