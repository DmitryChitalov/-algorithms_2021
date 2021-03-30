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

lst = [i for i in range(10000)]
deq = deque(lst)
elem = 10000
ext_el = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


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


def pop_list(check_list):
    check_list.pop()


def pop_deque(check_deque):
    check_deque.pop()


print('popleft list: ' + str(timeit('pop_left_list(lst)', globals=globals(), number=10000)))
print('popleft deque: ' + str(timeit('pop_left_deque(deq)', globals=globals(), number=10000)))
print(f'Удаление первого элемента. Очередь (deque) быстрее \n')

print('append_left list: ' + str(timeit('append_left_list(lst, elem)', globals=globals(), number=10000)))
print('append_left deque: ' + str(timeit('append_left_deque(deq, elem)', globals=globals(), number=10000)))
print(f'Добавление елемента в начало. Очередь (deque) быстрее. \n')

print('extend_left list: ' + str(timeit('extend_left_list(lst, ext_el)', globals=globals(), number=10000)))
print('extend_left deque: ' + str(timeit('extend_left_deque(deq, ext_el)', globals=globals(), number=10000)))
print(f'Добавление елементов в начало. Очередь (deque) гораздо быстрее. \n')

print('pop list: ' + str(timeit('pop_list(lst)', globals=globals(), number=10000)))
print('pop deque: ' + str(timeit('pop_deque(deq)', globals=globals(), number=10000)))
print(f'Удаление последнего элемента. Практически одинаково. \n')
