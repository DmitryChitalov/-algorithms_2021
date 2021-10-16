"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
from collections import OrderedDict
from timeit import timeit

some_dict = dict(zip([k for k in range(1000)], [v for v in range(1000, 2000)]))

ordered = OrderedDict(zip([k for k in range(1000)], [v for v in range(1000, 2000)]))

print('Тесты заполнения')
print(timeit('some_dict = dict(zip([k for k in range(1000)], '
             '[v for v in range(1000, 2000)]))', globals=globals(), number=10000))
print(timeit('ordered = OrderedDict(zip([k for k in range(1000)], '
             '[v for v in range(1000, 2000)]))', globals=globals(), number=10000))
print('*' * 50)
# По времени заполения OrderedDict значительно проигрывает обычному словарю

print('Тесты получения элемента')
print(timeit('some_dict[500]', globals=globals()))
print(timeit('ordered[500]', globals=globals()))
print('*' * 50)
# Время получения элемента у обоих словарей одинаковое

print('Тесты занесения нового элемента')
print(timeit('some_dict["key"] = "value"', globals=globals()))
print(timeit('ordered["key"] = "value"', globals=globals()))
print('*' * 50)
# Время занесения одного нового элемента у OrderedDict примерно на 20% хуже
# Вывод: смысла использования OrderedDict в новых версиях Python нет
