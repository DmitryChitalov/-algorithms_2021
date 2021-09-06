"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""

from timeit import timeit
import collections

print('Заполнение. dict намного быстрее ordereddict')
print('dict time', timeit("NEW_DICT = {'a': 1, 'b': 2, 'c': 3}", globals=globals()))
print('ordereddict time',
      timeit("NEW_ODICT = collections.OrderedDict([('a', 1), ('b', 2), ('c', 3)])", globals=globals()))
print('---')
NEW_DICT = {'a': 1, 'b': 2, 'c': 3}
NEW_ODICT = collections.OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print('Извлечение. нет существенной разницы')
print('dict time', timeit("item = NEW_DICT['a']", globals=globals()))
print('ordereddict time', timeit("item = NEW_ODICT['a']", globals=globals()))

'''
Нет смысла использовать OrderedDict в Python 3.6 и более поздних версиях,
так как стандартный Словарь умеет теперь тоже самое, и еще и быстрее работает
'''
