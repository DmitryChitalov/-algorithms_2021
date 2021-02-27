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

from timeit import timeit
from collections import deque

my_list = [i for i in range(100000)]
my_deque = deque(my_list)
elem = 5
ext_el = [1, 2]


# Проверим команды с одинаковыми результатами, но разной реализацией:
def pop_left_list(check_list):
    check_list.pop(0)


def pop_left_deque(check_deque):
    check_deque.popleft()


def append_left_list(check_list, el):
    check_list.insert(0, el)


def append_left_deque(check_deque, el):
    check_deque.appendleft(el)


def extend_left_list(check_list, el):
    for i in el:
        check_list.insert(0, i)


def extend_left_deque(check_deque, el):
    check_deque.extendleft(el)


# Функцию с одинаковой реализацией тоже проверим:
def pop_list(check_list):
    check_list.pop()


def pop_deque(check_deque):
    check_deque.pop()


print('popleft list')
print(timeit('pop_left_list(my_list)', globals=globals(), number=1000))

print('popleft deque')
print(timeit('pop_left_deque(my_deque)', globals=globals(), number=1000))

print('appendleft list')
print(timeit('append_left_list(my_list, elem)', globals=globals(), number=1000))

print('appendleft deque')
print(timeit('append_left_deque(my_deque, elem)', globals=globals(), number=1000))

print('extendleft list')
print(timeit('extend_left_list(my_list, ext_el)', globals=globals(), number=100))

print('extendleft deque')
print(timeit('extend_left_deque(my_deque, ext_el)', globals=globals(), number=100))

print('pop list')
print(timeit('pop_list(my_list)', globals=globals(), number=100))

print('pop deque')
print(timeit('pop_deque(my_deque)', globals=globals(), number=100))

'''
По итогу можно сказать, что все действительно так, как в документации: заранее встроенные в deque операции
работают в нескоько раз быстрее, чем аналогичные в list, но при этом одинковые операции выполняются
с равными затратами времени
'''
