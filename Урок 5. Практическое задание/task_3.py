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


def fill_list():
    return [i**2 for i in range(10)]


def fill_deque():
    return deque([i**2 for i in range(10)])


def insert_list(list):
    list.insert(0, 1000)


def append_left_deq(deq):
    deq.appendleft(1000)


def pop_list(list):
    list.pop()


def pop_deq(deq):
    deq.pop()

reg_list = fill_list()
deq = fill_deque()

print(
    'fill_list: ',
    timeit(
        f'fill_list()',
        globals=globals(),  number=100000))
print(
    'fill_deque: ',
    timeit(
        f'fill_deque()',
        globals=globals(), number=100000))
print(
    'insert_list: ',
    timeit(
        f'insert_list(reg_list)',
        globals=globals(),  number=100000))
print(
    'append_left_deq: ',
    timeit(
        f'append_left_deq(deq)',
        globals=globals(), number=100000))
print(
    'pop_list: ',
    timeit(
        f'pop_list(reg_list)',
        globals=globals(),  number=100000))
print(
    'pop_deq: ',
    timeit(
        f'pop_deq(deq)',
        globals=globals(), number=100000))

"""
    fill_list:  0.6244650999999999
    fill_deque:  0.5787163
    insert_list:  6.3181382
    append_left_deq:  0.03186490000000042
    pop_list:  0.03134760000000014
    pop_deq:  0.03297020000000028
    
    Операции заполнения списка и Deque, и извлечения элемента выполняются соизмеримо.
    Вставка элемента в начало списка проходит в сотни раз медленнее
"""