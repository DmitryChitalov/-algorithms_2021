"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции, равные по смыслу, с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?

ОТВЕТ: После замеров на сортировку и удаление, OrderedDict показал результаты значительно хуже,
чем обычные методы словаря. Более поздних версиях чем 3.5, не вижу смылса использовать OrderedDict,
возможно если только нужно передвинуть ключ в конец или начало через метод move_to_end(key, last=True).
Простая сортировка словаря:
 0.8763189
Сортировка OrderedDict словаря:
 1.4240598
Удаление первого элемента словаря OrderedDict:
 1.6525793999999996
Простое удаление элемента словаря:
 0.1693252000000003

"""
from collections import OrderedDict
from timeit import timeit

reg_dict = {'d': 4, 'b': 2, 'c': 3, 'e': 5, 'a': 1}
order_dict = {'d': 4, 'b': 2, 'c': 3, 'e': 5, 'a': 1}


def sort_dict():
    new_dict = sorted(reg_dict.items(), key=lambda t: t[1])
    return new_dict


sort_dict()


def sort_order():
    new_order = OrderedDict(sorted(order_dict.items(), key=lambda t: t[1]))
    return new_order


sort_order()


def popitem_order():
    new_order = OrderedDict(sorted(order_dict.items(), key=lambda t: t[1]))
    new_order.popitem(last=True)
    return new_order


popitem_order()


def pop_dict():
    for key, value in reg_dict.items():
        return reg_dict.pop(key, value)


pop_dict()

print(f"Простая сортировка словаря:\n {timeit('sort_dict()', globals=globals())}")
print(f"Сортировка OrderedDict словаря:\n {timeit('sort_order()', globals=globals())}")
print(f"Удаление первого элемента словаря OrderedDict:\n {timeit('popitem_order()', globals=globals())}")
print(f"Простое удаление первого элемента словаря:\n {timeit('pop_dict()', globals=globals())}")
