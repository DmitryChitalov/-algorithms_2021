"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

Задача: 
1) создайте простой список (list) и очередь (deque). Сделайте замеры и оцените что заполняется быстрее.
2) Выполните различные операции с каждым из объектов. Сделайте замеры и оцените, где и какие операции быстрее.

Не забудьте, что сравнивать, например, можно операцию appendleft дека и insert списка и т.д.
"""
from collections import deque
from timeit import timeit


def list_gen():
    return [i * i for i in range(100000)]


def deque_gen():
    return deque([i * i for i in range(100000)])


def list_append(lst):
    for i in range(10000):
        lst.append(i)
    return lst


def deque_append(dq):
    for i in range(10000):
        dq.append(i)
    return dq


def list_insert(lst):
    for i in range(10000):
        lst.insert(0, i)
    return lst


def deque_appendleft(dq):
    for i in range(10000):
        dq.appendleft(i)
    return dq


def list_pop(lst):
    for i in range(0, 10000):
        lst.pop()
    return lst


def deque_pop(dq):
    for i in range(0, 10000):
        dq.pop()
    return dq


def list_popleft(lst):
    for i in range(0, 10000):
        lst.pop(0)
    return lst


def deque_popleft(dq):
    for i in range(0, 10000):
        dq.popleft()
    return dq


def list_reverse(lst):
    return lst[::-1]


def deque_reverse(dq):
    dq.reverse()
    return dq


my_list = list_gen()
my_deque = deque_gen()
print(f'{list_gen.__name__}:\n', timeit('list_gen()', globals=globals(), number=10))
print(f'{deque_gen.__name__}:\n', timeit('deque_gen()', globals=globals(), number=10), '\n')
print(f'{list_append.__name__}:\n', timeit('list_append(my_list)', globals=globals(), number=10))
print(f'{deque_append.__name__}:\n', timeit('deque_append(my_deque)', globals=globals(), number=10), '\n')
print(f'{list_insert.__name__}:\n', timeit('list_insert(my_list)', globals=globals(), number=10))
print(f'{deque_appendleft.__name__}:\n', timeit('deque_appendleft(my_deque)', globals=globals(), number=10), '\n')
print(f'{list_pop.__name__}:\n', timeit('list_pop(my_list)', globals=globals(), number=10))
print(f'{deque_pop.__name__}:\n', timeit('deque_pop(my_deque)', globals=globals(), number=10), '\n')
print(f'{list_popleft.__name__}:\n', timeit('list_popleft(my_list)', globals=globals(), number=10))
print(f'{deque_popleft.__name__}:\n', timeit('deque_popleft(my_deque)', globals=globals(), number=10), '\n')
print(f'{list_reverse.__name__}:\n', timeit('list_reverse(my_list)', globals=globals(), number=10))
print(f'{deque_reverse.__name__}:\n', timeit('deque_reverse(my_deque)', globals=globals(), number=10), '\n')

'''
list_gen:
 0.166901299
deque_gen:
 0.18628201700000002 

list_append:
 0.014753136
deque_append:
 0.013479693999999987 

list_insert:
 18.365549326
deque_appendleft:
 0.012082681999999068 

list_pop:
 0.016670998000002157
deque_pop:
 0.0158783679999992 

list_popleft:
 8.460158564
deque_popleft:
 0.015611207000002736 

list_reverse:
 0.005796314999997776
deque_reverse:
 0.001347738999999848 
 
*****************

* Чтобы быстро вставить слева,
  deque решит сию проблему! *

Разница в скорости "левых" функций в 700+ раз больше.
deque жжёт!

reverse() deque быстрее среза в 4+ раз
'''
