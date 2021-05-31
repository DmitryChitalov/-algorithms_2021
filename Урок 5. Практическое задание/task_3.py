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

lst = [i for i in range(10000)]
deq = deque(lst)
elem = 10000
ext_el = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def pop_list(check_list):
    check_list.pop(0)


def pop_deque(check_deque):
    check_deque.pop()


def append_left_list(check_list, el):
    check_list.insert(0, el)


def append_left_deque(check_deque, el):
    check_deque.appendleft(el)


def extend_left_list(check_list, el):
    for i in el:
        check_list.insert(0, i)


def extend_left_deque(check_deque, el):
    check_deque.extendleft(el)


print('pop_list: ' + str(timeit('pop_list(lst)', globals=globals(), number=10000)))
print('pop_deque: ' + str(timeit('pop_deque(deq)', globals=globals(), number=10000)))
#  Удаление элемента через deque быстрее.

print('append_list: ' + str(timeit('append_left_list(lst, elem)', globals=globals(), number=10000)))
print('append_deque: ' + str(timeit('append_left_deque(deq, elem)', globals=globals(), number=10000)))
#  Добавление елемента в начало через deque быстрее.

print('extend_list: ' + str(timeit('extend_left_list(lst, ext_el)', globals=globals(), number=10000)))
print('extend_deque: ' + str(timeit('extend_left_deque(deq, ext_el)', globals=globals(), number=10000)))
#  Добавление елементов в начало через deque снова быстрее.
