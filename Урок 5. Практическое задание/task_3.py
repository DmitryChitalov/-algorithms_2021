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

simple_list = []
deque_list = deque([])
deque_list_to_simple = deque([])


def to_insert(num, my_list):
    for i in range(num):
        my_list.insert(i, i)
    return my_list


def to_append_left(num, my_deq_list):
    for i in range(num):
        my_deq_list.appendleft(i)


def simple_pop(num, my_list):
    for i in range(num):
        my_list.pop()
    return my_list


def deq_pop(num, deq_list):
    for i in range(num):
        deq_list.popleft()
    return deque_list


def my_reverse(my_list):
    return my_list.reverse()


print(timeit('to_insert(100, simple_list)', globals=globals(), number=1000))  # 3.1353239759337157
print(timeit('to_insert(100, deque_list_to_simple)', globals=globals(), number=1000))  # 0.021031533018685877
print(timeit('to_append_left(100, deque_list)', globals=globals(), number=1000))  # 0.005526070948690176
"""
на заполнение insert для обычного списка мега-долгий, для deq списка быстрый,
а appendleft для deq списка очень быстрый
"""

print(timeit('my_reverse(simple_list)', globals=globals(), number=100000))  # 5.682099067023955
print(timeit('my_reverse(deque_list)', globals=globals(), number=100000))  # 6.364160979050212
"""
разворот обычного списка не намного, но стабильно быстрее
"""

to_insert(10000, simple_list)
to_insert(10000, deque_list_to_simple)
to_append_left(10000, deque_list)

print(timeit('simple_pop(10, simple_list)', globals=globals(), number=1000))  # 0.5727231309283525
print(timeit('simple_pop(10, deque_list_to_simple)', globals=globals(), number=1000))  # 0.5713505960302427
print(timeit('deq_pop(10, deque_list)', globals=globals(), number=1000))  # 0.6424458930268884

"""
с завидным постоянством popleft чуточку долше, чем pop
"""


