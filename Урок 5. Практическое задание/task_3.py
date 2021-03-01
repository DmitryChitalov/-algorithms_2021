"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.

Операции равные по семантике (по смыслу)
Но разные по используемым ф-циям

И добавить аналитику, так ли это или нет.!
"""

from collections import deque
from timeit import timeit


def append_left_list(check_list, el):
    check_list.insert(0, el)


def append_left_deque(check_deque, el):
    check_deque.appendleft(el)


def pop_left_list(check_list):
    check_list.pop(0)


def pop_left_deque(check_deque):
    check_deque.popleft()


def extend_left_list(check_list, el):
    for i in el:
        check_list.insert(0, i)


def extend_left_deque(check_deque, el):
    check_deque.extendleft(el)


def pop_list(check_list):
    check_list.pop()


def pop_deque(check_deque):
    check_deque.pop()


some_list = [el for el in range(100000)]
some_deque = deque(some_list)
some_el = True
some_lst = [1, 2]

print('appendleft list')
print(timeit('append_left_list(some_list, some_el)', globals=globals(), number=10000))

print('appendleft deque')
print(timeit('append_left_deque(some_deque, some_el)', globals=globals(), number=10000))

print('popleft list')
print(timeit('pop_left_list(some_list)', globals=globals(), number=10000))

print('popleft deque')
print(timeit('pop_left_deque(some_deque)', globals=globals(), number=10000))

print('extendleft list')
print(timeit('extend_left_list(some_list, some_lst)', globals=globals(), number=100))

print('extendleft deque')
print(timeit('extend_left_deque(some_deque, some_lst)', globals=globals(), number=100))

print('pop list')
print(timeit('pop_list(some_list)', globals=globals(), number=100))

print('pop deque')
print(timeit('pop_deque(some_deque)', globals=globals(), number=100))

'''
В результате замеров времени получилось, что встроенные в deque операции
работают во много раз быстрее, чем аналогичные в простом списке. Информация в документации
соответствует дейтсвительности. При этом, если делать замеры одинаковых фукнций - время сопоставимо.
'''
