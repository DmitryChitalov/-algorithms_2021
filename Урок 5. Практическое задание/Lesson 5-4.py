"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции, равные по смыслу, с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
from timeit import timeit
from collections import OrderedDict as OrdDict


def filling_dict(num):
    a = dict()
    for i in range(num):
        a[str(i)] = i
    return a


def filling_ord_dict(num):
    a = OrdDict()
    for i in range(num):
        a[str(i)] = i
    return a


def update_dict(dict_1, dict_2):
    dict_1.update(dict_2)


def update_ord_dict(dict_1, dict_2):
    dict_1.update(dict_2)


def pop_item_dict(dict_1):
    for i in range(len(dict_1)):
        a = dict_1.popitem()


def pop_item_ord_dict(ord_dict_1):
    for i in range(len(ord_dict_1)):
        a = ord_dict_1.popitem()


def sorting_dict(dict_1):
    a = sorted(dict_1.items(), key=lambda item: item[1])
    return a


def sorting_ord_dict(ord_dict_1):
    a = sorted(ord_dict_1.items(), key=lambda item: item[1])
    return a


print('---------------')
print('Чтобы было наглядно понятно какие операции производятся с my_dict и с my_ord_dict представляю:')
my_dict = filling_dict(10)
my_ord_dict = filling_ord_dict(10)
print(my_dict)
print(my_ord_dict)
print('---------------')
my_dict_2 = filling_dict(15)
my_ord_dict_2 = filling_ord_dict(15)
update_dict(my_dict, my_dict_2)
update_ord_dict(my_ord_dict, my_ord_dict_2)
print(my_dict)
print(my_ord_dict)
print('---------------')
print(pop_item_dict(my_dict))
print(pop_item_ord_dict(my_ord_dict))
print('---------------')
print(sorting_dict(my_dict_2))
print(sorting_ord_dict(my_ord_dict_2))
print('---------------')
print('А теперь произведём замеры с объектами кратно больше, поэтому выводить тысячи цифр мы не будем,'
      ' а только результаты замеров:')
print('---------------')
print(
    timeit(
        'filling_dict(1000)',
        setup='from __main__ import filling_dict',
        number=10000))
print(
    timeit(
        'filling_ord_dict(1000)',
        setup='from __main__ import filling_ord_dict',
        number=10000))
print('В случае с заполнением словарей коллекий OrderedDict оказывается медленнее')
my_dict = filling_dict(1000)
my_ord_dict = filling_ord_dict(1000)
my_dict_2 = filling_dict(1500)
my_ord_dict_2 = filling_ord_dict(1500)
print('---------------')
print(
    timeit(
        'update_dict(my_dict, my_dict_2)',
        globals=globals(),
        number=10000))
print(
    timeit(
        'update_ord_dict(my_ord_dict, my_ord_dict_2)',
        globals=globals(),
        number=10000))
print('Здесь мы видим, что результат работы коллекции OrderedDict сильно хуже')
print('---------------')
print(
    timeit(
        'pop_item_dict(my_dict)',
        globals=globals(),
        number=10000))
print(
    timeit(
        'pop_item_ord_dict(my_ord_dict)',
        globals=globals(),
        number=10000))
print('Здесь результат коллекции тоже не опарвдывает себя')
print('---------------')
print(
    timeit(
        'sorting_dict(my_dict_2)',
        globals=globals(),
        number=10000))
print(
    timeit(
        'sorting_ord_dict(my_ord_dict_2)',
        globals=globals(),
        number=10000))
print('В последнем замере также, из чего делаем вывод, что исползование данной коллекции не имеет смысла в версиях Python 3.6 и выше')
print('---------------')
