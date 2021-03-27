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
from random import randint
from collections import deque

rand_min = 1
rand_max = 1000

default_list = [randint(rand_min, rand_max) for num in range(rand_max)]
deque_list = deque(default_list)


def default_add_left(list_to_work):
    list_to_work.insert(0, 777)
    return list_to_work


def default_add_right(list_to_work):
    list_to_work.append(666)
    return list_to_work


def default_del_left(list_to_work):
    list_to_work.pop(0)
    return list_to_work


def default_del_right(list_to_work):
    list_to_work.pop(len(list_to_work) - 1)
    return list_to_work


def default_get(list_to_work):
    return list_to_work[rand_min - 1]


def deque_add_left(list_to_work):
    list_to_work.appendleft(777)
    return list_to_work


def deque_add_right(list_to_work):
    list_to_work.append(666)
    return list_to_work


def deque_pop_left(list_to_work):
    list_to_work.popleft()
    return list_to_work


def deque_pop_right(list_to_work):
    list_to_work.pop()
    return list_to_work


def deque_get(list_to_work):
    return list_to_work[rand_min - 1]


print(f'list, получение элемента: {timeit("default_get(default_list)", globals=globals(), number=100000)}')
print(f'list, добавление left: {timeit("default_add_left(default_list)", globals=globals(), number=100000)}')
print(f'list, добавление right: {timeit("default_add_right(default_list)", globals=globals(), number=100000)}')
print(f'list, удаление left: {timeit("default_del_left(default_list)", globals=globals(), number=100000)}')
print(f'list, удаление right: {timeit("default_del_right(default_list)", globals=globals(), number=100000)}')
print('=' * 50)
print(f'deque, получение элемента: {timeit("deque_get(deque_list)", globals=globals(), number=100000)}')
print(f'deque, добавление left: {timeit("deque_add_left(deque_list)", globals=globals(), number=100000)}')
print(f'deque, добавление right: {timeit("deque_add_right(deque_list)", globals=globals(), number=100000)}')
print(f'deque, добавление left: {timeit("deque_pop_left(deque_list)", globals=globals(), number=100000)}')
print(f'deque, добавление right: {timeit("deque_pop_right(deque_list)", globals=globals(), number=100000)}')
"""
Результат работы:
list, получение элемента: 0.014396299999999997
list, добавление left: 2.6414072
list, добавление right: 0.010980800000000013
list, удаление left: 2.9151684999999996
list, удаление right: 0.014019900000000085
==================================================
deque, получение элемента: 0.009513700000000291
deque, добавление left: 0.009621000000000102
deque, добавление right: 0.009268000000000498
deque, добавление left: 0.009162499999999518
deque, добавление right: 0.008414100000000424

Добавление и удаление элементов через deque происходит быстрей.
Получение элементов в deque и list происходит примерно одинаково, на уровне погрешности.
"""
