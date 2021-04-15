"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции, равные по смыслу, с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""


from collections import OrderedDict
from timeit import timeit


def update_dict(dct):
    dct.update({'100': 101})


def update_dict_ord(dct):
    dct.update({'100': 101})


def search_dict(dct):
    dct.get('333')


def search_dict_ord(dct):
    dct.get('333')


def pop_dict(dct):
    dct.popitem()


def pop_dict_ord(dct):
    dct.popitem()


"""
********** ДОБАВЛЕНИЕ ЭЛЕМЕНТА **********
dict: 0.174605033
ord_dict: 0.29533230499999996
********** ПОИСК ЭЛЕМЕНТА **********
dict: 0.090954708
ord_dict: 0.09200897600000002
********** УДАЛЕНИЕ ЭЛЕМЕНТА POPITEM() **********
dict: 0.00024943599999982524
ord_dict: 0.0007464839999999917


Вывод:
OrderedDict уступает обычному словарю, по всем показателям скорость больше у встроенного словаря,
так что нет смысла его использовать, только если нужно использовать python ниже 3.6
"""


if __name__ == '__main__':
    now_dict = {str(i): i for i in range(10000)}
    order_dict = OrderedDict(now_dict)
    print(f'********** ДОБАВЛЕНИЕ ЭЛЕМЕНТА **********')
    print(f'dict: {timeit("update_dict(now_dict)", globals=globals(), number=1000000)}')
    print(f'ord_dict: {timeit("update_dict_ord(order_dict)", globals=globals(), number=1000000)}')
    print(f'********** ПОИСК ЭЛЕМЕНТА **********')
    print(f'dict: {timeit("search_dict(now_dict)", globals=globals(), number=1000000)}')
    print(f'ord_dict: {timeit("search_dict_ord(order_dict)", globals=globals(), number=1000000)}')
    print(f'********** УДАЛЕНИЕ ЭЛЕМЕНТА POPITEM() **********')
    now_dict_1 = {str(i): i for i in range(1000000)}
    order_dict_1 = OrderedDict([(str(i), i) for i in range(1000000)])
    print(f'dict: {timeit("pop_dict(now_dict_1)", globals=globals(), number=1000)}')
    print(f'ord_dict: {timeit("pop_dict_ord(order_dict_1)", globals=globals(), number=1000)}')
