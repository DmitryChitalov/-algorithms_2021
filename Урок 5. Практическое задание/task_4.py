"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции, равные по смыслу, с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
from timeit import timeit
from collections import OrderedDict

test_dict = {i: i for i in range(1000)}
test_order_dict = OrderedDict(test_dict)

# get
print("get")
print(f'{timeit("test_dict.get(999)", globals=globals(), number=100000)} - dict')
print(f'{timeit("test_order_dict.get(999)", globals=globals(), number=100000)} - ordered_dict')

# items
print("items")
print(f'{timeit("test_dict.items()", globals=globals(), number=100000)} - dict')
print(f'{timeit("test_order_dict.items()", globals=globals(), number=100000)} - ordered_dict')

# values
print("values")
print(f'{timeit("test_dict.values()", globals=globals(), number=100000)} - dict')
print(f'{timeit("test_order_dict.values()", globals=globals(), number=100000)} - ordered_dict')

# values
print("values")
print(f'{timeit("test_dict.values()", globals=globals(), number=100000)} - dict')
print(f'{timeit("test_order_dict.values()", globals=globals(), number=100000)} - ordered_dict')

# popitem
print("popitem")
print(f'{timeit("test_dict.popitem()", globals=globals(), number=1000)} - dict')
print(f'{timeit("test_order_dict.popitem()", globals=globals(), number=1000)} - ordered_dict')

"""
get
0.022447300000000003 - dict
0.021604700000000004 - ordered_dict
items
0.017972500000000002 - dict
0.013919699999999993 - ordered_dict
values
0.0117033 - dict
0.01236130000000002 - ordered_dict
values
0.01214889999999999 - dict
0.012381900000000001 - ordered_dict
popitem
0.00011700000000000599 - dict
0.00024620000000000197 - ordered_dict

Большинство операций в dict и ordered_dict выполняются за примерно одинаковое время, немного быстрее в dict,
popitem в dict значительно быстрее
Поскольку в версиях 3.6 и позднее словари и так являются упорядоченными, то смыслв в использовании OrderedDict
в этих версиях нет, работу они не ускоряют
"""
