"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""

# Использовать orderedDict является менее трудозатратным, но не сильно, когда мы заполняем словарь.
# В случае вытаскивания элементов orderedDict показывет неоднозначный ответ. Поэтому оценить сложно, но считаю, что без него лучше обходиться в версиях 3.6 и выше.
# Есть смысл использоваться в версиях 3.6 и раньше. Сейчас словари упорядоченны.

from collections import OrderedDict
from timeit import timeit

dct = {}
dct_2 = {}


def dct_filling():
    for el in range(10000):
        dct[el+1] = el
    return dct

dct_filling()

def dct_2_filling():
    for el in range(10000):
        dct_2[el + 1] = el
    return OrderedDict(dct_2)


dct_2_filling()

print(timeit("dct_filling", globals=globals()))
print(timeit("dct_2_filling", globals=globals()))

def get_el_dct(dct):
    for k, v in dct.items():
        return k, v


def get_el_dct_2(dct_2):
    for k, v in dct_2.items():
        return OrderedDict(k, v)




print('ЭЛЕМЕНТЫ')
print(timeit("get_el_dct", globals=globals()))
print(timeit("get_el_dct_2", globals=globals()))




