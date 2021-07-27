"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""


from timeit import timeit
from collections import OrderedDict

dict_simple = {a: a ** 2 for a in range(50)}
dict_ordered = OrderedDict({a: a ** 2 for a in range(5)})
print(dict_ordered)
print(dict_simple)

print(f'Заполнения словаря {timeit("dict_simple", globals=globals())}.')
print(f'Заполнения OrderedDict {timeit("dict_ordered", globals=globals())}.')

print(f'Получения элемента из словаря {timeit("dict_simple.items()", globals=globals())}.')
print(f'Получения элемента из OrderedDict {timeit("dict_ordered.items()", globals=globals())}.')
"""
время заполнения почти одинаково так как одинаковые методы

начиная с версии Python 3.6 и позднее словари - упорядоченная коллекция,
нет смысла использовать OrderedDict 
"""