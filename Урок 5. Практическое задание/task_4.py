"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""

from collections import OrderedDict
from timeit import timeit

my_dict = dict((int(n), int(n)) for n in range(100000))
my_order_dict = OrderedDict(dict((int(n), int(n)) for n in range(100000)))

print(
    timeit(
        "dict((int(n), int(n)) for n in range(1000000))",
        globals=globals(),
        number=10))  # 1.9422532

print(
    timeit(
        "OrderedDict(dict((int(n), int(n)) for n in range(1000000)))",
        globals=globals(),
        number=10))  # 3.8125499000000005

print(
    timeit(
        "my_dict[999]",
        globals=globals(),
        number=1000))  # 3.629999999965605e-05

print(
    timeit(
        "my_order_dict[999]",
        globals=globals(),
        number=1000))  # 3.609999999998337e-05

# Заполнение словаря происходит в два раза быстрее чем OrderDict
# Получение элемента происходит с практически одинаковой скоростью
# Использовать OrderDict в версиях Python начиная с 3.6 не имеет смысла
