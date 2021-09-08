"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""

from collections import OrderedDict
from timeit import timeit


def fill_dict(count):
    return {i: i for i in range(count)}


def fill_order(count):
    return OrderedDict([(i, i) for i in range(count)])


def add_dict(k, v):
    new_dict[k] = v
    return new_dict


def add_order(k, v):
    new_order[k] = v
    return new_order


def get_dict(k):
    return new_dict.get(k)


def get_order(k):
    return new_order.get(k)


def pop_dict():
    return new_dict.popitem()


def pop_order():
    return new_order.popitem()


new_dict = fill_dict(20)
new_order = fill_order(20)

key = 'key'
value = 'value'

print(new_dict)
print(new_order)
print(add_dict(key, value))
print(add_order(key, value))
print(get_dict(key))
print(get_order(key))
print(pop_dict())
print(pop_order())

new_dict = fill_dict(1010)
new_order = fill_order(1010)
print(f'fill_dict(1000):    {timeit("fill_dict(2000)", globals=globals(), number=1000)}')
print(f'fill_order(1000):   {timeit("fill_order(2000)", globals=globals(), number=1000)}')
print(f'add_dict():         {timeit("add_dict(key, value)", globals=globals())}')
print(f'add_order():        {timeit("add_order(key, value)", globals=globals())}')
print(f'get_dict():         {timeit("get_dict(key)", globals=globals())}')
print(f'get_order():        {timeit("get_order(key)", globals=globals())}')
print(f'pop_dict():         {timeit("pop_dict()", globals=globals(), number=1000)}')
print(f'pop_order():        {timeit("pop_order()", globals=globals(), number=1000)}')

"""
fill_dict(1000):    0.1326274 seconds
fill_order(1000):   0.3043256 seconds
add_dict():         0.1254199 seconds
add_order():        0.1335591 seconds
get_dict():         0.0961443 seconds
get_order():        0.1194082 seconds
pop_dict():         0.0001149 seconds
pop_order():        0.0001519 seconds

Заполнение быстрее у словаря. Добавление, получение и удаление у словаря и OrderedDict примерно одинаковы по скорости.
Следовательно нет смысла использовать OrderedDict в Python 3.6 и более поздних версиях.
"""
