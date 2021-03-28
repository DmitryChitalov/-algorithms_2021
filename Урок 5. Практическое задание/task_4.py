"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции, равные по смыслу, с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""

from timeit import timeit
from collections import OrderedDict


def simply_create():
    return {k: v for (k, v) in zip([x for x in range(50)],
                                   [k for k in range(50)])}


def or_create():
    return OrderedDict({k: v for (k, v) in zip([x for x in range(50)],
                                               [k for k in range(50)])})


print(f'\n{"=" * 15} Создание коллекции {"=" * 15}')
print(f'Обычный словарь: {timeit("simply_create()", globals=globals(), number=10000)}')
print(f'OrderedDict    : {timeit("or_create()", globals=globals(), number=10000)}')

simply_dict = simply_create()
or_dict = or_create()

print(f'\n{"=" * 14} Сортировка по ключам {"=" * 14}')
print(f'Обычный словарь: {timeit("sorted(simply_dict.items(), key=lambda t: t[0])", globals=globals(), number=10000)}')
print(f'OrderedDict    : {timeit("sorted(or_dict.items(), key=lambda t: t[0])", globals=globals(), number=10000)}')

print(f'\n{"=" * 12} Сортировка по значениям {"=" * 13}')
print(f'Обычный словарь: {timeit("sorted(simply_dict.items(), key=lambda t: t[1])", globals=globals(), number=10000)}')
print(f'OrderedDict    : {timeit("sorted(or_dict.items(), key=lambda t: t[1])", globals=globals(), number=10000)}')

print(f'\n{"=" * 9} Добавление пары ключ: значение {"=" * 9}')
key, value = 'key', 'value'
print(f'Обычный словарь: {timeit("simply_dict[key] = value", globals=globals(), number=1000000)}')
print(f'OrderedDict    : {timeit("or_dict[key] = value", globals=globals(), number=1000000)}')

print(f'\n{"=" * 9} Проверка на вхождениее {"=" * 9}')
print(f'Обычный словарь: {timeit("key in simply_dict", globals=globals(), number=1000000)}')
print(f'OrderedDict    : {timeit("key in or_dict", globals=globals(), number=1000000)}')

print(f'\n{"=" * 9} Доступ по  ключу {"=" * 9}')
print(f'Обычный словарь: {timeit("a = simply_dict[key]", globals=globals(), number=1000000)}')
print(f'OrderedDict    : {timeit("a = or_dict[key]", globals=globals(), number=1000000)}')

"""
Исходя из проведенных замеров работы методов можно сделать вывод, что в настоящее время
использовать OrderedDict нет необходимости.

Во всех проверенных случаях, за исключением работы с данными по ключу, где результат примерно одинаковый,
OrderedDict проигрывает классическому dict.
"""

