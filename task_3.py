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
import timeit

deq_list = deque()
ls_list = []
n = [i for i in range(100)]


def append_list(n):
    for i in n:
        ls_list.append(i)


def append_deque(n):
    for i in n:
        deq_list.append(i)


def append_left_list(n):
    for i in n:
        ls_list.insert(0, i)


def append_left_deque(n):
    for i in n:
        deq_list.appendleft(i)


def pop_list(m):
    for i in range(m):
        ls_list.pop()


def pop_deque(m):
    for i in range(m):
        deq_list.pop()


def pop_left_list(m):
    for i in range(m):
        ls_list.pop(0)


def pop_left_deque(m):
    for i in range(m):
        deq_list.popleft()


print(f'Добавление в список {timeit.timeit("append_list(n)", globals=globals(), number=1000)}')
print(f'Добавление в deque {timeit.timeit("append_deque(n)", globals=globals(), number=1000)}')
print(f'Добавление в список с начала списка {timeit.timeit("append_left_list(n)", globals=globals(), number=1000)}')
print(f'Добавление в deque с начала списка {timeit.timeit("append_left_deque(n)", globals=globals(), number=1000)}')
print(f'Удаление из списока {timeit.timeit("pop_list(99)", globals=globals(), number=1000)}')
print(f'Удаление из deque {timeit.timeit("pop_deque(99)", globals=globals(), number=1000)}')
print(f'Удаление из списока с начала списка {timeit.timeit("pop_left_list(99)", globals=globals(), number=1000)}')
print(f'Удаление из deque с начала списка {timeit.timeit("pop_left_deque(99)", globals=globals(), number=1000)}')

'''
Добавление в список 0.005610799999999999
Добавление в deque 0.005051099999999989
Добавление в список с начала списка 5.5932191
Добавление в deque с начала списка 0.004508200000000073
Удаление из списока 0.0049608000000000985
Удаление из deque 0.004296700000000264
Удаление из списока с начала списка 1.3392824
Удаление из deque с начала списка 0.004250600000000659

deque очень хорошо работает когда необходимо добавлять или удалять элементы в начало списка. В списках наоборот,
при работе с началом списка время резко увеличивается. При добавлении и удалении элементов в конце списка и deque и 
список показывают практически одинаковое время. При этом сам deque лучше работает, когда необходимо добавлять или 
удалять элементы в начало списка

'''

