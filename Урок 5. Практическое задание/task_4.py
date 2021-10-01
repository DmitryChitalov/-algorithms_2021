"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
from collections import OrderedDict
from timeit import timeit

dict_obj = {12: 'Двенадцать'}
ord_dict_obj = OrderedDict([(12, 'Двенадцать')])


# Функция, выполняющая заполнение словаря
def app_to_dict(dct):
    for i, el in enumerate(list(range(10)), start=1):
        dct[i] = el
    return dct


# Замеры функции заполнения обычного словаря и OrderedDict
# print(timeit('app_to_dict(dict_obj)', number=1000000, globals=globals()))  # 1.808
# print(timeit('app_to_dict(ord_dict_obj)', number=1000000, globals=globals()))  # 2.258

# Замеры получения элемента обычного словаря и OrderedDict
print(timeit('dict_obj[12]', number=100000000, globals=globals()))  # 6.8445566
print(timeit('ord_dict_obj[12]', number=100000000, globals=globals()))  # 5.6500784


'''
Аналитика:
Начиная от версии Python 3.6 нет смысла использовать OrderedDict, операция получения
элементов из OrderedDict, будет чуть быстрее, но не значительно, а в операциях заполнения 
оказывается еще и медленее.
'''