"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
from collections import OrderedDict
from timeit import timeit


# Создаем и наполняем
def fill_dict():
    return {elems: elems for elems in range(500)}


# Создаем и наполняем
def fill_ord_dict():
    return OrderedDict([(elems, elems) for elems in range(500)])


# Изменение (функция одна, т.к. синтаксис одинаковый)
def change_dict(temp):
    for i in temp:
        temp[i] += 1
    return temp


# Достаем все значения и ничего не делаем, просто переберём
def my_items(temp):
    for k, v in temp.items():
        pass
    return temp


# Очистка (функция одна, т.к. синтаксис одинаковый)
def clear_dict(temp):
    temp.clear()
    return temp


my_dict = fill_dict()
my_ord_dict = fill_ord_dict()

print('fill_dict', timeit('fill_dict()', globals=globals(), number=10000))
print('fill_ord_dict', timeit('fill_ord_dict()', globals=globals(), number=10000))

print('change_dict', timeit('change_dict(my_dict)', globals=globals(), number=10000))
print('change_ord_dict', timeit('change_dict(my_ord_dict)', globals=globals(), number=10000))

print('my_items', timeit('my_items(my_dict)', globals=globals(), number=10000))
print('my_items_ord_dict', timeit('my_items(my_ord_dict)', globals=globals(), number=10000))

print('clear_dict', timeit('clear_dict(my_dict)', globals=globals(), number=10000))
print('clear_ord_dict', timeit('clear_dict(my_ord_dict)', globals=globals(), number=10000))


"""
fill_dict 0.1991009
fill_ord_dict 0.5648474

change_dict 0.3125918
change_ord_dict 0.41678419999999994

my_items 0.07876620000000001
my_items_ord_dict 0.16786279999999998

clear_dict 0.0008247999999999589
clear_ord_dict 0.0008292999999999218

Во всех замерах OrderedDict показал себя хуже по скорости, после того как словари 
стали упорядоченные после версии 3.6, единственноый плюс это метод move_to_end(key, last=True), 
но думаю это можно при желании реализовать иным способом, не жертвуя скоростью.
"""