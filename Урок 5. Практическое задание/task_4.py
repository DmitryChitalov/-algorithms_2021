"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
from collections import OrderedDict
import timeit
my_dict = {}
my_orderDict = OrderedDict()


def dt_add():
    for i in range(100000):
        my_dict[i] = 0


def ordt_add():
    for i in range(100000):
        my_orderDict[i] = 0


print('dt_add()',timeit.timeit("dt_add()", globals=globals(), number=1))
## от 0.0062449 до 0.0087699
print('ordt_add()',timeit.timeit("ordt_add()", globals=globals(), number=1))
## от 0.0103488 до 0.0134169
print()


def dict_iter():
    for i in range(100000):
        if i in my_dict:
            my_dict[i] = 1


def ordt_iter():
    for i in range(100000):
        if i in my_orderDict:
            my_orderDict[i] = 1


print('dict_iter()',timeit.timeit("dict_iter()", globals=globals(), number=1))
## от 0.006945 до 0.007752
print('ordt_iter()',timeit.timeit("ordt_iter()", globals=globals(), number=1))
## от 0.0098105 до 0.0102406
print()


def dict_sh():
    return my_dict[50000]


def ordt_sh():
    return my_orderDict[50000]


print('dict_sh()',timeit.timeit("dict_sh()", globals=globals(), number=10000))
## от 0.006047 до 0.006747
print('ordt_sh()',timeit.timeit("ordt_sh()", globals=globals(), number=10000))
## от 0.006116 до 0.006751
print()


def dict_popitem():
    return my_dict.popitem()


def ordt_popitem():
    return my_orderDict.popitem()


print('dict_popitem()',timeit.timeit("dict_popitem()", globals=globals(), number=100000))
## от 0.008401 до 0.009586
print('ordt_popitem()',timeit.timeit("ordt_popitem()", globals=globals(), number=100000))
## от 0.013714 до 0.0164534

"""
В среднем все операции с стандартным объекта dict выполняются немного быстрее, чем с объектом OrderDict.
Однако разница не является уж сликом большой. С учетом того, что в текущей версии питон, объект dict
запоминает порядок вставки элемента, основное преимущество OrderDict перед ним практически пропадает.
Единственные интереснные оссобенности OrderDict это перемещение определенного элемента по ключу в начало, либо в конец
порядка ключей, и удаление не только последнего добавленого ключа, но и первого добаленного, аналогов у этих
методов у объекта dict нет.
А благодоря этим методам объект OrderDict получает полный функционал дека. Мне кажется, с практической точки зрения, 
в этом есть интересная особенность, в каких-то случаях OrderDict может заменить, например, deque. Все зависит от задачи,
которая стоит перед нами.
В большинстве же повседневных случаев использования функционала dict вполне достаточно, и методы OrderDict
излишни.
"""
