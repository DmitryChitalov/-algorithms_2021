"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции, равные по смыслу, с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""

from collections import OrderedDict
from timeit import timeit

test_val = -1
test_dict = dict()
test_ordr = OrderedDict()
n = 1000
operation = ['создание', 'чтение', 'поиск', 'копирование', 'копир.+удаление']
dict_operation = [
    '''for a in range(n):
    test_dict[a] = a''',
    '''for a in range(n):
    test_val = test_dict[a]''',
    '''test_dict.get(test_val,-1)''',
    '''test_dict_2 = test_dict.copy()''',
    '''test_dict_2 = test_dict.copy()
for a in range(n):
    test_val = test_dict_2.popitem()'''
]

ordr_operation = [
    '''for a in range(n):
    test_ordr[a] = a''',
    '''for a in range(n):
    test_val = test_ordr[a]''',
    '''test_ordr.get(test_val,-1)''',
    '''test_ordr_2 = test_ordr.copy()''',
    '''test_ordr_2 = test_ordr.copy()
for a in range(n):
    test_ordr_2.popitem()'''
]

print('Операции с словарем:')
for op, st in zip(operation, dict_operation):
    print(f'{op} {timeit(st, number=100000, globals=globals())}')

print('\nОперарации с OrderedDict')
for op, st in zip(operation, ordr_operation):
    print(f'{op} {timeit(st, number=100000, globals=globals())}')

'''
Результаты.

Операции с словарем:
создание 6.001549154
чтение 4.778829647
поиск 0.005833520999999564
копирование 0.4905431130000011
копир.+удаление 7.4751661710000015

Операрации с OrderedDict
создание 8.494324056
чтение 4.859963643
поиск 0.005932334000000594
копирование 7.426256572
копир.+удаление 18.633267904999997

Выводы. OrderedDict во многих операциях медленее словаря. 
        OrderedDict стоит использовать если нужен метод move_to_end,
        если выгода перекроет возросшие затраты.   
'''