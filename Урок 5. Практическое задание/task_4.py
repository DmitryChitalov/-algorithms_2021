"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
from collections import OrderedDict
from timeit import timeit
from random import randint

n = randint(1000, 10000)

dct = {el: randint(0, 1000) for el in range(n + 1)}
order_dct = OrderedDict(dct)

print(f'Время генерации элементов словаря '
      f'{timeit("dct ={el: randint(0,1000) for el in range(n)}" ,globals=globals(), number=1000)}')

print(f'Время генерации элементов OrderedDict '
      f'{timeit("order_dct = OrderedDict.fromkeys([randint(0, 1000) for el in range(n)])",globals=globals(), number=1000)}')

print(f'Время получения элемента из словаря '
      f'{timeit("dct[randint(100, n)]", globals=globals(), number=100000)}')

print(f'Время получения элемента из OrderedDict '
      f'{timeit("order_dct[randint(100, n)]", globals=globals(), number=100000)}')

print(f'Время получения пар значений из словаря '
      f'{timeit("dct.items()", globals=globals(), number=100000)}')

print(f'Время получения пар значений из OrderedDict '
      f'{timeit("order_dct.items()", globals=globals(), number=100000)}')

print(f'Время удаления всех элементов из словаря '
      f'{timeit("dct.popitem()", globals=globals(), number=n)}')

print(f'Время удаления всех элементов из OrderedDict '
      f'{timeit("order_dct.popitem()", globals=globals(), number=n)}')


'''
Судя по всем замерам они практически идентичны, но чутку быстрее обычный словарь. 
Смысла использовать OrderedDict в версии python 3.6 и выше нет.
Может в каких нибудь только специфических задачах.
'''
