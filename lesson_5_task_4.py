"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
from timeit import timeit
import collections

new_dict = {a: a ** 2 for a in range(100)}
new_ordered_dict = collections.OrderedDict({a: a ** 2 for a in range(10)})
print(new_ordered_dict)
print(new_dict)

print(f'Время заполнения словаря {timeit("new_dict", globals=globals())}.')  # 0.06885
print(f'Время заполнения OrderedDict {timeit("new_dict", globals=globals())}.')  # 0.06920
# время заполнения примерно одинаково

print(f'Время получения элемента из словаря {timeit("new_dict.items()", globals=globals())}.')  # 0.23831
print(f'Время получения элемента из OrderedDict {timeit("new_dict.items()", globals=globals())}.')  # 0.24680
# время заполнения примерно одинаково (одинаковые методы)
# поскольку начиная с версии Python 3.6 и позднее словари - упорядоченная коллекция
# использовать OrderedDict в указанных версиях нет смысла
