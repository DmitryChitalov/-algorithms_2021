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


#
#
# def timing(func):
#     def wrapped(*args, **kwargs):
#         string = func.__name__
#         print('Время выполнения:', {timeit(f'string()', globals=globals())})
#         return func(*args, **kwargs)
#
#     return wrapped

def create_d():
    d = deque(range(100))
    return d


def create_l():
    l = list(range(100))
    return l


def append_left_d(d: deque, val: int):
    d.appendleft(val)
    return d


def append_left_l(l: list, val: int):
    l.insert(0, val)
    return l


def extend_left_d(d: deque):
    d.extendleft(deque([1, 2, 3]))
    return d


def extend_left_l(l: list):
    l.insert(0, [1, 2, 3])
    return l


def popleft_d(d: deque):
    d.popleft()
    return d


def popleft_l(l: list):
    l.pop(0)
    return l


def index_l(l: list):
    a = l[0]


def index_d(d: deque):
    a = d[0]


d = deque()
l = list()
val = 1
# d = create_d()
# l = create_l()
print('Время выполнения create_d:', timeit(f'create_d()', globals=globals()))
print('Время выполнения create_l:', timeit(f'create_l()', globals=globals()))
print('Время выполнения append_left_l:', timeit(f'append_left_l(l, val)', globals=globals(), number=1000))
print('Время выполнения append_left_d:', timeit(f'append_left_d(d, val)', globals=globals(), number=1000))
print('Время выполнения extend_left_d:', timeit(f'extend_left_d(d)', globals=globals(), number=1000))
print('Время выполнения extend_left_l:', timeit(f'extend_left_l(l)', globals=globals(), number=1000))
print('Время выполнения pop_left_d:', timeit(f'popleft_d(d)', globals=globals(), number=1000))
print('Время выполнения pop_left_l:', timeit(f'popleft_l(l)', globals=globals(), number=1000))
print('Время выполнения index_d:', timeit(f'index_d(d)', globals=globals(), number=1000))
print('Время выполнения index_l:', timeit(f'index_l(l)', globals=globals(), number=1000))

"""

Время выполнения create_d: 1.5944987
Время выполнения create_l: 1.221224
Время выполнения append_left_l: 0.0004920999999997733
Время выполнения append_left_d: 0.00014959999999986096
Время выполнения extend_left_d: 0.00037850000000005934
Время выполнения extend_left_l: 0.0011937999999998006
Время выполнения pop_left_d: 0.00010810000000027742
Время выполнения pop_left_l: 0.00031800000000004047
Время выполнения index_d: 0.055382400000000054
Время выполнения index_l: 0.0003399000000001706

"""

"""
Из результатов видно, что в быстроте заполнения дек уступает списку в 1.5-2 раза
но зато все операции с левой стороны выполняются в разы быстрее
однако доступ по индексу также занимает меньше времени у списка
поэтому если в какой-то задаче нам не так важно работать с индексацией, а
куда важнее иметь доступ к двум сторонам контейнера, лучше использовать дек
"""