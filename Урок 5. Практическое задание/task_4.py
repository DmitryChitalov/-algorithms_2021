"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""

from collections import OrderedDict
from timeit import timeit

my_dictionary = {num: num ** 2 for num in range(50)}
ordered_dictionary = OrderedDict({num: num ** 2 for num in range(10)})

print(my_dictionary)
print(ordered_dictionary)
print(f'Заполнение словаря: {timeit("my_dictionary", globals=globals())}.')
print(f'Заполнение OrderedDict: {timeit("ordered_dictionary", globals=globals())}.')
print(f'Получение элемента из my_dictionary {timeit("my_dictionary.items()", globals=globals())}.')
print(f'Получение элемента из ordered_dictionary {timeit("ordered_dictionary.items()", globals=globals())}.')

# Вывод: Поскольку методы одинаковые, время выполнения почти одинаково. Так как словари являются упорядоченной
# коллекцией, начиная с версии Python 3.6, использование OrderedDict не имеет смысла.
