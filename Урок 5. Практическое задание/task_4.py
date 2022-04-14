"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""

from collections import OrderedDict
from timeit import timeit

simple_dict = {kv: kv for kv in range(10)}
ordered_dict = OrderedDict(simple_dict)

copy_simple_dict = simple_dict
copy_ordered_dict = ordered_dict


print(f'{"~"*40}Time for creating{"~"*40}\n'
      f'Simple dict: {timeit("simple_dict", globals=globals(), number=10)}\n'
      f'Ordered dict: {timeit("ordered_dict", globals=globals(), number=10)}\n'
      f'\n{"~"*40}Time for operating{"~"*40}\n'
      f'Simple dict: {timeit("copy_simple_dict.update({1000: 1000})", globals=globals(), number=10)}\n'
      f'Ordered dict: {timeit("copy_ordered_dict.update({1000: 1000})", globals=globals(), number=10)}\n'
      )
"""
Создание словарей: 
Обычный создается быстрее, чем упорядоченный 
    Simple dict: 1.0920002750935964e-06
    Ordered dict: 4.000003173132427e-07
    
Действия со словарями:
На примере update. Обычные словари работают быстрее, чем упорядоченные. 
    Simple dict: 5.370000053517288e-06
    Ordered dict: 6.892999863339355e-06

Основной вывод: использование упорядоченных словарей, в современных версиях Python, не является необходимым, т.к 
OrderedDict использовался только из-за сохранения порядка добавленных в него элементов. 
А сейчас Oict работает намного быстрее, с теми же процедурами и функциями, при этом также сохраняет порядок элементов
"""
