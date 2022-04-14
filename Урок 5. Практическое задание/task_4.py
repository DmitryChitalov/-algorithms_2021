"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
from collections import OrderedDict
from timeit import timeit

my_dct = {i: i for i in range(1000)}
my_ord_dct = OrderedDict((i, i) for i in range(1000))
print('Скорость возврата пары (ключ,значение):')
print(f'{timeit("my_dct.items()", globals=globals(), number=100000)} - Словарь')  # 0.02973184999427758
print(f'{timeit("my_ord_dct.items()", globals=globals(), number=100000)} - OrderedDict')  # 0.02973184999427758
print('Скорость возврата значения ключа:')
print(f'{timeit("my_dct.get(100)", globals=globals(), number=100000)} - Словарь')  # 0.02973184999427758
print(f'{timeit("my_ord_dct.get(100)", globals=globals(), number=100000)} - OrderedDict')  # 0.02973184999427758
"""
Скорости работы словаря  и OrderedDict практически не отличается.
Смысла использования OrderedDict я не вижу, но это только в версии python 3.6 и  старше.
Так как словарь в этих версия уже упорядоченный.
"""
