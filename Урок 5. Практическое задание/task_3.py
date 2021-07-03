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

n = 100


def dqe():
    return deque([x for x in range(n)])


def lst():
    return [x for x in range(n)]


def dqe_append_l():
    for i in range(n):
        my_deque.appendleft(i)
    return my_deque


def lst_insert():
    for i in range(n):
        my_list.insert(0, i)
    return my_list


def dqe_pop_l():
    for i in range(n):
        my_deque.popleft()
    return my_deque


def lst_pop():
    for i in range(n):
        my_list.pop(0)
    return my_list


def dqe_extend_l():
    for i in range(n):
        my_deque.extendleft([0])
    return my_deque


def lst_extend():
    for i in range(n):
        my_list.extend([0])
    return my_list


my_deque = dqe()
my_list = lst()

# deque выполняет операции вставки значительно быстрее чем list
print(f'deque appendleft()  ', timeit('dqe_append_l()', globals=globals(), number=1000))
print(f'list insert()       ', timeit('lst_insert()', globals=globals(), number=1000))
print('')

# Тоже самое можно сказать для операций удаления: deque popleft значительно выигрывает list pop
print(f'deque popleft()     ', timeit('dqe_pop_l()', globals=globals(), number=1000))
print(f'list pop()          ', timeit('lst_pop()', globals=globals(), number=1000))
print('')

# А вот использование метода deque extendleft выполняется чуть медленнее (еще и в перевернутом порядке),
# чем list extend
print(f'deque extendleft()  ', timeit('dqe_extend_l()', globals=globals(), number=1000))
print(f'list extend()       ', timeit('lst_extend()', globals=globals(), number=1000))
print('')

# Таким образом, коллекция deque всегда на порядки лучше чем list кроме extendleft метода,
# который оказался чуть медленнее чем list в моем случае
