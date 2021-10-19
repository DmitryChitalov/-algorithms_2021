"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

Задача: 
1) создайте простой список (list) и очередь (deque). Сделайте замеры и оцените что заполняется быстрее.
2) Выполните различные операции с каждым из объектов. Сделайте замеры и оцените, где и какие операции быстрее.

В первую очередь необходимо выполнить замеры для ф-ций appendleft, popleft, extendleft дека и для их аналогов у списков.
"""

from collections import deque
from timeit import timeit


def pull_list():
    data = list(range(10000))
    return data


def popleft_list(data: list):
    data.pop(0)
    return data


def appendleft_list(data: list):
    data.insert(0, 10)
    return data


def extendleft_list(data: list):
    new_lst = [1, 2, 3, 4, 5]
    for i, num in enumerate(new_lst):
        data.insert(i, num)
    return data


def append_list(data: list):
    data.append(1)
    return data


def pull_deque():
    data = deque(range(10000))
    return data


def popleft_deque(data: deque):
    data.popleft()
    return data


def appendleft_deque(data: deque):
    data.appendleft(10)
    return data


def extendleft_deque(data: deque):
    new_lst = [1, 2, 3, 4, 5]
    data.extendleft(new_lst)
    return data


def append_deque(data: deque):
    data.append(1)
    return data


my_list = pull_list()
my_deque = pull_deque()

print(timeit("pull_list()", globals=globals(), number=10000))
print(timeit("pull_deque()", globals=globals(), number=10000))
print('-' * 80)
print(timeit("popleft_list(my_list)", globals=globals(), number=10000))
print(timeit("popleft_deque(my_deque)", globals=globals(), number=10000))
print('-' * 80)
print(timeit("appendleft_list(my_list)", globals=globals(), number=10000))
print(
    timeit("appendleft_deque(my_deque)", globals=globals(), number=10000))
print('-' * 80)
print(timeit("extendleft_list(my_list)", globals=globals(), number=10000))
print(
    timeit("extendleft_deque(my_deque)", globals=globals(), number=10000))
print('-' * 80)
print(timeit("append_list(my_list)", globals=globals(), number=10000))
print(timeit("append_deque(my_deque)", globals=globals(), number=10000))

"""
2.044193296
2.2009629829999997
--------------------------------------------------------------------------------
0.013363693999999704
0.0016260040000002363
--------------------------------------------------------------------------------
0.02422223499999987
0.0014262650000000932
--------------------------------------------------------------------------------
0.9239032470000001
0.002771648000000404
--------------------------------------------------------------------------------
0.0014300709999996997
0.0019690509999996664

Список заполняется быстрее цем дека, но все действия связанные в левой части 
деки соверщаются в разы быстрее. И действиях подобных append дека всеравно 
немного быстрее чем список.
"""
