"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции, равные по смыслу, с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""

from timeit import timeit
from collections import OrderedDict

#  Генерирую одинаковое наполнение для словарей
my_dict = {f'key{str(i)}': i for i in range(100, 1000)}
# my_order_dict = OrderedDict([(f'key{str(i)}', i) for i in range(100, 1000)])
my_order_dict = OrderedDict(my_dict)
print(my_dict)
print(my_order_dict)
copy_od = my_order_dict.copy()
copy_d = my_dict.copy()

my_order_dict.update()

print('Время копирования OrderedDict:')
print(timeit(stmt="""copy_od = my_order_dict.copy()""",
             globals=globals(), number=100000))
print('Время очистки OrderedDict:')
print(timeit(stmt="""copy_od.clear()""",
             globals=globals(), number=100000))
print('Время добавления элемента в  OrderedDict:')
print(timeit(stmt="""my_order_dict.update({'key000': 99})""",
             globals=globals(), number=100000))
print('Время возвращения элемента в  OrderedDict:')
print(timeit(stmt="""my_order_dict.get('key101')""",
             globals=globals(), number=100000))
print('/*/*/*/*/*/*/*/*/*/*/*/*/*/\n')

print('Время копирования dict:')
print(timeit(stmt="""copy_d = my_dict.copy()""",
             globals=globals(), number=100000))
print('Время очистки dict:')
print(timeit(stmt="""copy_d.clear()""",
             globals=globals(), number=100000))
print('Время добавления элемента в Dict:')
print(timeit(stmt="""my_dict.update({'key000': 99})""",
             globals=globals(), number=100000))
print('Время возвращения элемента в Dict:')
print(timeit(stmt="""my_dict.get('key101')""",
             globals=globals(), number=100000))


"""
Время копирования OrderedDict:
10.135324113
Время очистки OrderedDict:
0.004752653999998913
Время добавления элемента в  OrderedDict:
0.03356663099999935
Время возвращения элемента в  OrderedDict:
0.006882446000000542
/*/*/*/*/*/*/*/*/*/*/*/*/*/

Время копирования dict:
0.5211824519999997
Время очистки dict:
0.005183349999999365
Время добавления элемента в Dict:
0.016542900000001026
Время возвращения элемента в Dict:
0.006475830999999488

В использовании OrderedDict в версиях 3.6 и старше смысла нет, обычный Dict уже сохраняет начальный порядок элементов.
Так же в некоторых операциях OrderedDict работает медленнее, значительно дольше работает копирование OrderedDict
"""