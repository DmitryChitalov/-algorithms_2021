"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""

from timeit import timeit
from collections import OrderedDict


my_dict = {}
my_OrederedDict = OrderedDict()

############################################################

def completion_dict(my_dict):
    for i in range(100):
        my_dict[i] = i

print('Заполняем dict:       ', round((timeit('''
def completion_dict(my_dict):
    for i in range(100):
        my_dict[i] = i
my_dict = {}
completion_dict(my_dict)
''')), 6))

print('Заполняем OrderedDict:', round((timeit('''
from collections import OrderedDict
def completion_dict(my_dict):
    for i in range(100):
        my_dict[i] = i
my_OrederedDict = OrderedDict()
completion_dict(my_OrederedDict)
''', number=1000)), 6))

#completion_dict(my_dict)
#completion_dict(my_OrederedDict)

############################################################

def change_dict(my_dict):
    for i in range(20):
        my_dict[i] = 'something'

print('Меняем элементы dict:       ', round((timeit('''
def change_dict(my_dict):
    for i in range(20):
        my_dict[i] = i
    for i in range(5, 100):
        my_dict[i] = 'something'
my_dict = {}
change_dict(my_dict)
''', number=100)), 6))

print('Меняем элементы OrderedDict:', round((timeit('''
from collections import OrderedDict
def change_dict(my_dict):
    for i in range(5, 100):
        my_dict[i] = 'something'
my_OrederedDict = OrderedDict()  
change_dict(my_OrederedDict)
''', number=100)), 6))

#change_dict(my_dict)
#change_dict(my_OrederedDict)

############################################################

def removal_dict(my_dict):
    for i in range(100):
        my_dict[i] = i
    for i in range(100):
        my_dict.pop(i)

print('Удаляем элементы dict:       ', round((timeit('''
def removal_dict(my_dict):
    for i in range(100):
        my_dict[i] = i
    for i in range(100):
        my_dict.pop(i)
my_dict = {}
removal_dict(my_dict)
''', number=1000)), 6))

print('Удаляем элементы OrderedDict:', round((timeit('''
from collections import OrderedDict
def removal_dict(my_dict):
    for i in range(100):
        my_dict[i] = i
    for i in range(100):
        my_dict.pop(i)
my_OrederedDict = OrderedDict()  
removal_dict(my_OrederedDict)
''', number=1000)), 6))

#removal_dict(my_dict)
#removal_dict(my_OrederedDict)

"""
Замеры:
    Заполняем dict:        4.367252
    Заполняем OrderedDict: 0.008232
    Меняем элементы dict:        0.000479
    Меняем элементы OrderedDict: 0.000796
    Удаляем элементы dict:        0.009062
    Удаляем элементы OrderedDict: 0.020129
    
Итог:
    OrderedDict отрабатывает гораздо быстрее только при заполнении объекта согласно полученным замерам,
  но если говорить о удалении элементов, либо изменении, то обычный dict будет более лучшим выбором.
"""
