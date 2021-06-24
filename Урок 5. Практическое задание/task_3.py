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

from timeit import timeit
from collections import deque

simple_lst1 = []
simple_lst2 = []
deq_obj = deque(simple_lst1)


def func_1_1():
    deq_obj.append(1)
    return deq_obj


def func_1_2():
    simple_lst2.append(1)
    return simple_lst2


simple_lst1 = []
simple_lst2 = []
deq_obj = deque(simple_lst1)


def func_2_1():
    deq_obj.appendleft(1)
    return deq_obj


def func_2_2():
    simple_lst2.insert(0, 1)
    return simple_lst2


simple_lst1 = [[i * i for i in range(100000)]]
simple_lst2 = [[i * i for i in range(100000)]]
deq_obj = deque(simple_lst1)


def func_3_1():
    deq_obj.pop()
    return deq_obj


def func_3_2():
    simple_lst2.pop()
    return simple_lst2


print('append(deque)', timeit("func_1_1()", number=2500000, globals=globals()))
print('append(list)', timeit("func_1_2()", number=2500000, globals=globals()))
print('appendleft(deque)', timeit("func_2_1()", number=1000, globals=globals()))
print('insert(list)', timeit("func_2_2()", number=1000, globals=globals()))
print('pop(deque)', timeit("func_3_1()", number=1000, globals=globals()))
print('pop(list)', timeit("func_3_2()", number=1000, globals=globals()))
