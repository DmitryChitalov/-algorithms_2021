"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции, равные по смыслу, с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
from collections import OrderedDict
from timeit import timeit


def create_dict():
    return {str(i): i for i in range(1000)}


def create_ordered_dict():
    return OrderedDict({str(i): i for i in range(1000)})


test1 = create_dict()
test2 = create_ordered_dict()

print('Dict: ' + str(timeit("create_dict()", globals=globals(), number=10000)))
print('OrderedDict: ' + str(timeit("create_ordered_dict()", globals=globals(), number=10000)))
print(f'создание словарей - OrderedDict в два раза медленней\n')

print('Dict: ' + str(timeit("test1.popitem", globals=globals(), number=10000)))
print('OrderedDict: ' + str(timeit("test2.popitem", globals=globals(), number=10000)))
print(f'Удаление из словарей пары, в конце. Практически одинаково. Dict быстрее \n')

print('Dict: ' + str(timeit("test1.values", globals=globals(), number=10000)))
print('OrderedDict: ' + str(timeit("test2.values", globals=globals(), number=10000)))
print(f'Возвращение значений из словарей.  Практически одинаково. Dict быстрее\n')

print('Dict: ' + str(timeit("test1.keys", globals=globals(), number=10000)))
print('OrderedDict: ' + str(timeit("test2.keys", globals=globals(), number=10000)))
print(f'Возвращение ключей из словарей.  Практически одинаково. Dict быстрее\n')

print(f'В Python 3.6 и более поздних версиях нет смысла использовать OrderedDict')
