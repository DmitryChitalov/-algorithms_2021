"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""

from collections import OrderedDict
from timeit import timeit

normal_dict = {}
for i in range(1000000):
    normal_dict.setdefault(i, 'default_val')
order_dict = OrderedDict(normal_dict)


print(timeit('order_dict.popitem()', globals=globals(), number=1000000))  # 0.11692820000000004
print(timeit('normal_dict.popitem()', globals=globals(), number=1000000))  # 0.0645796999999999
print('\n')
print(timeit('order_dict.items', globals=globals(), number=1000000))  # 0.034024799999999966
print(timeit('normal_dict.items', globals=globals(), number=1000000))  # 0.0336843

"""
По одному лишь извлечению можно увидеть, что операции с простым словарем горазда быстрее чем с ordered, так что 
можно сделать вывод что особого смысла в использовании ordered нет. Может быть и есть некие специфические
ситуации, но я их не могу представить (разве что более ранняя версия питона).
"""
