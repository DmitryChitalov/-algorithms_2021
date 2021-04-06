"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции, равные по смыслу, с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
from collections import OrderedDict
from timeit import timeit

dct = {f'key_{i}': f'val_{i}' for i in range(100000)}
order_dct = OrderedDict(dct)

print('Получение значения по ключу:')
key = 'key_5000'
print(f"\tDict:  {timeit('dct.get(key)', globals=globals(),number=100000):0.8f}")
print(f"\tOrderedDict:  {timeit('order_dct.get(key)', globals=globals(),number=100000):0.8f}")
'''
Выборка по ключу:
        Dict:  0.01704560
        OrderedDict:  0.02086780
'''
print('Получение значений:')
print(f"\tDict:  {timeit('dct.values()', globals=globals(),number=100000):0.8f}")
print(f"\tOrderedDict:  {timeit('order_dct.values()', globals=globals(),number=100000):0.8f}")
'''
Получение значений:
        Dict:  0.01288720
        OrderedDict:  0.01372420
'''
print('Получение пар значений:')
print(f"\tDict:  {timeit('dct.items()', globals=globals(),number=100000):0.8f}")
print(f"\tOrderedDict:  {timeit('order_dct.items()', globals=globals(),number=100000):0.8f}")
'''
Получение пар значений:
        Dict:  0.01225450
        OrderedDict:  0.01156860
'''

'''
Замеры, на данных операциях, показали отсутствие преимуществ OrderedDict, 
поэтому смысл использования этот тип словаря в замен Dict нет.
'''