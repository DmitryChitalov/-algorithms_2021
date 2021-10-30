"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""

import collections
import timeit
# создание и заполнение
def create_dict():
    classic_dict = {i: i for i in range(10000)}
    return classic_dict

# получение элемента
def operation_dict(dct):

    for x in range(1000):  #  операция удаления
        dct.pop(x)
    for n in range(1000):  # операция замены
        dct[n] = 'papipu'



def create_order_dict():
    order_dict = collections.OrderedDict([(i, i) for i in range(10000)])
    return order_dict

def elem_order(dct):

    for x in range(1000):  # операция удаления
        dct.pop(x)
    for n in range(1000):  # операция замены
        dct[n] = 'papipu'

print(
    timeit.timeit(
        "create_dict()",
        globals=globals(),
        number=1000), f' - замеры создания и заполнения обычного словаря')

print(
    timeit.timeit(
        "operation_dict(create_dict())",
        globals=globals(),
        number=1000), f' - замеры операций с обычным словарем')
print('-' * 20)
print(
    timeit.timeit(
        "create_order_dict()",
        globals=globals(),
        number=1000), f' - замеры создания и заполнения OrderedDict словаря')

print(
    timeit.timeit(
        "elem_order(create_order_dict())",
        globals=globals(),
        number=1000), f' - замеры операций с OrderedDict словарем')

"""
0.9223849000409245  - замеры создания и заполнения обычного словаря
1.0662487999652512  - замеры операций с обычным словарем
--------------------
2.1408683000481687  - замеры создания и заполнения OrderedDict словаря
2.9615783999906853  - замеры операций с OrderedDict словарем
"""
"""
В версиях питона начиная от 3.6 и выше смысла использовать OrderedDict нету
потому что он работает медленнее. На значениях с которыми я проверял словарь он оказался медленее в два раза
также создание классического списка выглядит намного лаконичнее
"""