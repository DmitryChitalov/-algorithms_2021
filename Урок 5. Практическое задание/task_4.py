from timeit import timeit
from collections import OrderedDict
"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции, равные по смыслу, с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""


my_dict = {i: i for i in range(1000)}

ord_dict = OrderedDict(my_dict)

print('ord_dict values:', timeit('ord_dict.values', globals=globals(), number=1000))
print('dict values', timeit('my_dict.values', globals=globals(), number=1000))
print('ord_dict keys:', timeit('ord_dict.keys', globals=globals(), number=1000))
print('dict keys:', timeit('my_dict.keys', globals=globals(), number=1000))
print('ord_dict pop:', timeit('ord_dict.popitem()', globals=globals(), number=1000))
print('dict pop:', timeit('my_dict.popitem()', globals=globals(), number=1000))
print('ord_dict get:', timeit('ord_dict.get(500)', globals=globals(), number=1000))
print('dict get:', timeit('my_dict.get(500)', globals=globals(), number=1000))

"""
В целом по времени обычный словарь работает быстрее, из приведенных операций, обычный словарь выигрывает,а значит
 использование Orderdict в современном мире не имеет смысла.
"""

