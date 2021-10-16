"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
from collections import OrderedDict
from timeit import timeit

a = OrderedDict()
b = {}
b_full = {i: i ** 2 for i in range(1000)}
a_full = OrderedDict({i: i ** 2 for i in range(1000)})


def fill_dict(dic):
    for i in range(100):
        dic[i] = i ** 2
        return dic


def get_el(dic):
    for i in range(100):
        d = dic[i]


print('Заполнение словарей')
print(timeit('fill_dict(b)', globals=globals()))
print(timeit('fill_dict(a)', globals=globals()))

print('Получение элементов')
print(timeit('get_el(b_full)', globals=globals()))
print(timeit('get_el(a_full)', globals=globals()))

"""
Словари работают почти идентично. Смысла использовать OrderedDict особого не имеет, т.к. его преимущество - 
упорядоченность по добавлению уже имеет и обычный словарь. Его можно использовать для спеуифических задач.
"""
