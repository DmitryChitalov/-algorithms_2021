"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции, равные по смыслу, с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
from collections import OrderedDict
from timeit import timeit


def create_dict(n):
    return {i: i for i in range(n)}


def create_ord_dict(n):
    return OrderedDict([(i, i) for i in range(n)])


n = 1000

test_dict = create_dict(n)
test_or_dict = create_ord_dict(n)

print(timeit("create_dict(n)", globals=globals(), number=10000))
print(timeit("create_ord_dict(n)", globals=globals(), number=10000))
print('---------------------------------------------')
print(timeit("test_dict.popitem", globals=globals(), number=10000))
print(timeit("test_or_dict.popitem", globals=globals(), number=10000))
print('---------------------------------------------')
print(timeit("test_dict.values", globals=globals(), number=10000))
print(timeit("test_or_dict.values", globals=globals(), number=10000))
print('---------------------------------------------')
print(timeit("test_dict.keys", globals=globals(), number=10000))
print(timeit("test_or_dict.keys", globals=globals(), number=10000))

# создание обычного словаря идет быстрее
# операции взятия ключа и значения происходят быстрее для обычного словаря, но не существенно
# ordereddict не нужен, он хуже оптимизировани. Возможно, он может пригодиться, если необходимо в одном проекте испльзовать разные версии питона
