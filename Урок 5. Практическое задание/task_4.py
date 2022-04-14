"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
import timeit
import collections
import random

def fill(in_dict, volume):
    """Заполнение"""
    for i in range(volume):
        in_dict[i] = i * 2

def get_el(in_dict, num):
    """Получение элемента"""
    try:
        return in_dict[num]
    except KeyError:
        return None

def time_check(in_dict, volume):
    """Получение элементов по случайному ключу"""
    for i in range(volume):
        get_el(in_dict,random.randint(0, VOLUME))

VOLUME = 10000
gen_dict = {}
ord_dict = collections.OrderedDict()
print('Создание обычного словаря:')
print(timeit.timeit('fill(gen_dict,VOLUME)',globals=globals(),number=VOLUME))
print('Создание OrderedDict:')
print(timeit.timeit('fill(ord_dict,VOLUME)',globals=globals(),number=VOLUME))
print('Выборка из обычного словаря:')
print(timeit.timeit('time_check(gen_dict,VOLUME)',globals=globals(),number=VOLUME))
print('Выборка из OrderedDict:')
print(timeit.timeit('time_check(ord_dict,VOLUME)',globals=globals(),number=VOLUME))
"""
Создание обычного словаря:
9.4190769
Создание OrderedDict:
12.233870399999999
Выборка из обычного словаря:
99.8354435
Выборка из OrderedDict:
102.70430180000001
По результатам выполнения видно, что создание обычного словаря происходит быстрее,
а результаты случайной выборки практически совпадают.
Таким образом, смысла использовать JrderedDict в Python старше 3.6 нет.
"""
