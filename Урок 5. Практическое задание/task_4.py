"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции, равные по смыслу, с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
from collections import OrderedDict
from timeit import timeit


def new_dict(n):
    return {i: i for i in range(n)}


def new_ord_dict(n):
    return OrderedDict([(i, i) for i in range(n)])


n = 100

test_dict = new_dict(n)
test_or_dict = new_ord_dict(n)

print('Создание словарей:')
print(timeit("new_dict(n)", globals=globals(), number=1000))
print(timeit("new_ord_dict(n)", globals=globals(), number=1000))
print('\n' + '-' * 20 + '\n')
print('Взятие значений:')
print(timeit("test_dict.values", globals=globals(), number=1000))
print(timeit("test_or_dict.values", globals=globals(), number=1000))
print('\n' + '-' * 20 + '\n')
print('Взятие ключей:')
print(timeit("test_dict.keys", globals=globals(), number=1000))
print(timeit("test_or_dict.keys", globals=globals(), number=1000))

# Создание обычного славаря происходит быстрее.
# Что касается взятия ключа и значения, то у обычного словаря происходит быстрее, но не значительно.
# Следовательно OrderedDict не нужен.