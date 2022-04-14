"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
from collections import OrderedDict
from timeit import timeit

dict = {1: 'A',
        2: 'B',
        3: 'C'}

od = OrderedDict([(1, 'A'), (2, 'B'), (3, 'C')])


def pop_dict(n):
    for i in range(n):
        del dict[i]
        # print(dict)


def popitem_od(n):
    for i in range(n):
        od.popitem(last=True)
        # print(od)


# pop_dict()
# popitem_od()
print(f'Время выполнения функции create_lst:',
      timeit('pop_dict(3)', globals=globals(), number=1000))
print(f'Время выполнения функции create_lst:',
      timeit('popitem_od(3)', globals=globals(), number=1000))


"""
По замерам разница не значительная, но OrderedDict отстает по времени
"""