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


def fill_list(count_el):
    list_for_fill = [_ for _ in range(count_el)]
    return list_for_fill


def fill_deque(count_el):
    deq_for_fill = deque([_ for _ in range(count_el)])
    return deq_for_fill


def push_left_list(list_for_push):
    list_for_push.insert(0, 1)


def push_list(list_for_push):
    list_for_push.append(1)


def push_left_deque(deq):
    deq.appendleft(1)


def push_deque(deq):
    deq.append(1)


def pop_left_list(list_for_pop):
    list_for_pop.pop(0)


def pop_list(list_for_pop):
    list_for_pop.pop()


def pop_left_deque(deq):
    deq.popleft()


def pop_deque(deq):
    deq.pop()


def ext_left_list(list_for_ext):
    for i in range(10):
        list_for_ext.insert(0, i)


def ext_list(list_for_ext):
    list_for_ext.extend([_ for _ in range(10)])


def ext_left_deq(deq):
    deq.extendleft([_ for _ in range(10)])


def ext_deq(deq):
    deq.extend([_ for _ in range(10)])


N = 10000

my_list = fill_list(1000)
my_deq = fill_deque(1000)

print(f"Заполнение списка: {timeit('fill_list(100)', globals=globals(), number=N)}")
print(f"Заполнение дека: {timeit('fill_deque(100)', globals=globals(), number=N)}")

print(f"Добавление элемента в начало списка: {timeit('push_left_list(my_list)', globals=globals(), number=N)}")
print(f"Добавление элемента в начало дека: {timeit('push_left_deque(my_deq)', globals=globals(), number=N)}")

print(f"Добавление элемента в конец списка: {timeit('push_list(my_list)', globals=globals(), number=N)}")
print(f"Добавление элемента в конец дека: {timeit('push_deque(my_deq)', globals=globals(), number=N)}")

print(f"Удаление элемента с начала списка: {timeit('pop_left_list(my_list)', globals=globals(), number=N)}")
print(f"Удаление элемента с начала дека: {timeit('pop_left_deque(my_deq)', globals=globals(), number=N)}")

print(f"Удаление элемента с конца списка: {timeit('pop_list(my_list)', globals=globals(), number=N)}")
print(f"Удаление элемента с конца дека: {timeit('pop_deque(my_deq)', globals=globals(), number=N)}")

print(f"Добавление нескольких элементов в начало списка: {timeit('ext_left_list(my_list)', globals=globals(), number=N)}")
print(f"Добавление нескольких элементов в начало дека: {timeit('ext_left_deq(my_deq)', globals=globals(), number=N)}")

print(f"Добавление нескольких элементов в конец списка: {timeit('ext_list(my_list)', globals=globals(), number=N)}")
print(f"Добавление нескольких элементов в конец дека: {timeit('ext_deq(my_deq)', globals=globals(), number=N)}")


'''
Заполнение дека происходит немного медленее, чем заполнение сипска. Остальные операции с деком выполняются быстрее, 
особенное это заметно при работе с началом списка/дека.
'''


