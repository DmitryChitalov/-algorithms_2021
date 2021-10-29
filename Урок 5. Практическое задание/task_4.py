"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
from timeit import timeit
from collections import OrderedDict
from random import randint

def add_dict():
  dictionary = dict()
  for i in range(1000):
    dictionary[i] = randint(1, 100)
  return dictionary

def add_orderdict():
  dictionary = OrderedDict()
  for i in range(1000):
    dictionary[i] = randint(1, 100)
  return dictionary

print(f'{timeit("add_dict()", globals=globals(), number=1000)} - заполнение dict',
f'{timeit("add_orderdict()", globals=globals(), number=1000)} - заполнение OrderedDict', sep='\n')

standart_dict = {x: x + 1 for x in range(1000)}
orderdict = OrderedDict(standart_dict)

def get_dict(standart_dict: dict):
  return standart_dict.items()

def get_orderdict(order_dict: dict):
  return order_dict.items()

print(f'{timeit("get_dict(standart_dict)", globals=globals(), number=1000000)} - получение элементов dict',
f'{timeit("get_orderdict(orderdict)", globals=globals(), number=1000000)} - получение элементов OrderedDict', sep='\n')

"""
Заполнение и получение элементов у обычного словаря немного быстрее, чем у OrderedDict.
Не имеет смысла использовать OrderedDict, т.к. он медленнее и после версии Python 3.6 обычный словарь упорядочен.
"""