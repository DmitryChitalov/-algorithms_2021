"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции, равные по смыслу, с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
from collections import OrderedDict
from timeit import timeit
from random import randint

test_dict = {i: i for i in range(500)}
test_order_dict = OrderedDict((i, i) for i in range(500))

print(timeit('{i: i for i in range(500)}', globals=globals(), number=1000))
print(timeit('OrderedDict((i, i) for i in range(500))', globals=globals(), number=1000))
print(timeit('test_dict.items()', globals=globals()))
print(timeit('test_order_dict.items()', globals=globals()))
print(timeit('test_dict.get(randint(0,500))', globals=globals()))
print(timeit('test_order_dict.get(randint(0,500))', globals=globals()))
print(timeit('test_dict.values()', globals=globals()))
print(timeit('test_order_dict.values()', globals=globals()))

"""
В общем разницы в скорости между обычным словорем и упорядоченым на Python 3.9 а значит большого смысла 
в использовании упорядоченого словоря нету. Обычный словарь делает тоже самое и с такой же скоростью как упорядоченый
"""