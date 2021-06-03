"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
from collections import OrderedDict
from timeit import timeit

temp_dict = {i: i + 1 for i in range(100)}
temp_orderdict = OrderedDict(temp_dict)

print('OrderedDict update: ' + str(timeit('temp_orderdict.update({1:2050})', globals=globals(), number=1000000)))
print('Dict update: ' + str(timeit('temp_dict.update({1:2050})', globals=globals(), number=1000000)))

print('OrderedDict get values: ' + str(timeit('temp_orderdict.values', globals=globals(), number=1000000)))
print('Dict get values: ' + str(timeit('temp_dict.values', globals=globals(), number=1000000)))

print('OrderedDict keys: ' + str(timeit('temp_orderdict.keys', globals=globals(), number=1000000)))
print('Dict keys: ' + str(timeit('temp_dict.keys', globals=globals(), number=1000000)))

print('OrderedDict get: ' + str(timeit('temp_orderdict[10]', globals=globals(), number=1000000)))
print('Dict get: ' + str(timeit('temp_dict[10]', globals=globals(), number=1000000)) + '\n')

'''
OrderedDict update: 0.5918047000000001
Dict update: 0.4360274999999999
OrderedDict get values: 0.07577080000000014
Dict get values: 0.0626977999999998
OrderedDict keys: 0.06495050000000013
Dict keys: 0.06430809999999987
OrderedDict get: 0.05163209999999996
Dict get: 0.050503900000000046

OrderDict уступает по производительности обычному словарю во всех операцих. 
'''
