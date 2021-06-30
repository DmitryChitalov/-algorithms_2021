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

from timeit import timeit
from collections import deque

data_deque = deque(range(100_000))
data_list = list(range(100_000))

def fill_list():
    data_list.append(0)
    return data_list

def fill_deque():
    data_deque.append(0)
    return data_deque

print('Заполнение:')
print('список: ', timeit('fill_list()', globals=globals(), number=1_000_000))
print('deque: ', timeit('fill_deque()', globals=globals(), number=1_000_000))

# При нескольких запусках ннполнение deque всегда занимало немного меньше времени, хотя значения очень близкие:
# список:  0.2419286
# deque:  0.21811730000000007

# Пробуем appendleft:

data_deque = deque(range(100_000))
data_list = list(range(100_000))

def append_left():
    data_deque.appendleft(0)
    return data_deque

def insert_left():
    data_list.insert(0, 0)
    return data_list

print('Append_left:')
print('список: ', timeit('insert_left()', globals=globals(), number=10_000))
print('deque: ', timeit('append_left()', globals=globals(), number=10_000))

# Deque значительно быстрее:
# список:  0.5780936
# deque:  0.0021265999999999785


# Пробуем popleft

def pop_left():
    return data_deque.popleft()

def pop_left_list():
    return data_list.pop(0)

print('Popleft:')
print('список: ', timeit('pop_left_list()', globals=globals(), number=1000))
print('deque: ', timeit('pop_left()', globals=globals(), number=1000))

# Снова преимущество на стороне deque:
# список:  0.030974000000000057
# deque:  0.00017570000000000086


# Пробуем extendleft


def extend_left():
    data_deque.extendleft([1, 2, 3])
    return data_deque

def extend_list():
    result = [1, 2, 3] + data_list
    return result

print('Extend_left:')
print('список: ', timeit('extend_list()', globals=globals(), number=1000))
print('deque: ', timeit('extend_left()', globals=globals(), number=1000))

# Deque опять выигрывает:
# список:  1.0768655
# deque:  0.00036089999999999733
