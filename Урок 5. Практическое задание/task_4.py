"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции, равные по смыслу, с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""

from collections import OrderedDict
from timeit import timeit

num = 1000

dic = {i: None for i in range(num)}
odic = OrderedDict.fromkeys([i for i in range(num)])


#  изменение значений каждого ключа с итерацией по диапазону
def change_values(n, d):
    d = {d[i]: 'new_i' for i in range(n)}


#  изменение значений каждого ключа с итерацией по элементам
def change_values_by_keys(d):
    d = {k: 'new_k' for k in dic.items()}


#  удаление последних пар ключ-значение
def popitem_from_dict(d):
        d.popitem()


print(f'    Изменение значений кючей с итерацией по диапазону\n'
      f'выполняется за '
      f'{timeit(stmt="change_values(num, dic)", setup="from __main__ import change_values, num, dic", number=10000)}'
      f' в обычном словаре\n'
      f'и за '
      f'{timeit(stmt="change_values(num, odic)", setup="from __main__ import change_values, num, odic", number=10000)}'
      f' в OrderedDict\n', "-"*120, end='\n')
print(f'    Изменение значений ключей с итерацией по элементам\n'
      f'выполняется за '
      f'{timeit(stmt="change_values_by_keys(dic)", number=10000, globals=globals())}'
      f' в обычном словаре\n'
      f'и за {timeit(stmt="change_values_by_keys(odic)", number=10000, globals=globals())}'
      f' в OrderedDict\n', "-"*120, end='\n')
print(f'    Взятие значения по ключу\n'
      f'выполняется за '
      f'{timeit(stmt="dic[100]", number=10000, globals=globals())}'
      f' в обычном словаре\n'
      f'и за {timeit(stmt="odic[100]", number=10000, globals=globals())} в OrderedDict\n', "-"*120, end='\n')

print(f'    Удаление последних пар ключ-значение\n'
      f'выполняется за '
      f'{timeit(stmt="popitem_from_dict(dic)", setup="from __main__ import popitem_from_dict, dic", number=1000)}'
      f' в обычном словаре\n'
      f'и за '
      f'{timeit(stmt="popitem_from_dict(odic)", setup="from __main__ import popitem_from_dict, odic", number=1000)}'
      f' в OrderedDict\n', "-"*120, end='\n')

print("Вывод: время выполнения операций в упорядоченном и обычном словаре почти не отличается,\n"
      "поэтому никаких преимуществ в нем не вижу, кроме возможно полезного метода перемещения\n"
      "ключа в конец словаря. Моя версия python 3.9")

