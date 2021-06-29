"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
import timeit
from collections import OrderedDict
from random import randint


# наполнение
sampl_dict = {f'{x}': 9 * x for x in range(99999)}
order_dict = OrderedDict({f'{x}': 6 * x for x in range(99999)})
print('заполнение')
print('Dict       ', timeit.timeit("{f'{x}': 9 * x for x in range(1000)}", globals=globals(), number=10000))
print('OrderedDict', timeit.timeit("OrderedDict({f'{x}': 6 * x for x in range(1000)})", globals=globals(),
                                   number=10000))
print('-' * 10)
print('добавлене элемента')
print('Dict       ', timeit.timeit("sampl_dict.setdefault(str(randint(1000, 999999999)), 123)", globals=globals(),
                                   number=100000))
print('OrderedDict', timeit.timeit("order_dict.setdefault(str(randint(1000, 999999999)), 123)", globals=globals(),
                                   number=100000))
print('-' * 10)
print('получение элемента')
print('Dict       ', timeit.timeit("sampl_dict[str(randint(0, 99998))]", globals=globals(), number=10000))
print('OrderedDict', timeit.timeit("order_dict[str(randint(0, 99998))]", globals=globals(), number=10000))
print('-' * 10)
print('извлечение последнего элемента')
print('Dict       ', timeit.timeit("sampl_dict.popitem()", globals=globals(), number=1000))
print('OrderedDict', timeit.timeit("order_dict.popitem()", globals=globals(), number=1000))
print('-' * 10)

'''
OrderedDict показывает не лучшие результаты в python 3.9
заполнение
Dict        1.725124445
OrderedDict 3.080219136
----------
добавлене элемента
Dict        0.10089799299999935
OrderedDict 0.11592407599999976
----------
получение элемента
Dict        0.010870060000000237
OrderedDict 0.010964496000000601
----------
извлечение последнего элемента
Dict        0.00018232899999937047
OrderedDict 0.00026680899999931285
----------
'''
