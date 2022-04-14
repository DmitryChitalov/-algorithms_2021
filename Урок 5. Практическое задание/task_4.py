"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""

from timeit import timeit
from collections import OrderedDict

new_dict = {a: a ** 2 for a in range(50)}
new_ordered_dict = OrderedDict({a: a ** 2 for a in range(5)})
print(new_ordered_dict)
print(new_dict)

print(f'Время заполнения словаря {timeit("new_dict", globals=globals())}.')
print(f'Время заполнения OrderedDict {timeit("new_dict", globals=globals())}.')

print(f'Время получения элемента из словаря {timeit("new_dict.items()", globals=globals())}.')
print(f'Время получения элемента из OrderedDict {timeit("new_dict.items()", globals=globals())}.')
"""
время заполнения одинаково так как одинакомые методы
поскольку начиная с версии Python 3.6 и позднее словари - упорядоченная коллекция и
использовать OrderedDict в указанных версиях нет смысла
"""