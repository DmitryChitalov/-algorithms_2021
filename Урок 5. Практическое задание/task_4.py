"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции, равные по смыслу, с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""

from collections import OrderedDict
from timeit import timeit

my_dict = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}

my_order_dict = OrderedDict(my_dict)


print(timeit("""
my_dict = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}
"""))

print(timeit("""
from collections import OrderedDict
my_order_dict = OrderedDict([('banana', '1'), ('apple', '4'), ('pear', '1'), ('orange', '2')])
"""))

print(timeit("""
my_dict = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}
my_dict['pineapple'] = '5'
"""))

print(timeit("""
from collections import OrderedDict
my_order_dict = OrderedDict([('banana', '1'), ('apple', '4'), ('pear', '1'), ('orange', '2')])
my_order_dict.update({'pineapple': '5'})
"""))

"""
Полагаю, что использование OrderedDict останется актуальным, несмотря на реалтзации многих
методов в обычных словарях, так как некоторые методы для него остаются уникальными. Например,
move_to_end. Однако, замеры времени показали, что обычные словари работают быстрее.
"""