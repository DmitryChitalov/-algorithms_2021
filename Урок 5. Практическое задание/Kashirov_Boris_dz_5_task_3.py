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

VALUE_STR = 'abcdefghijklmnopqrstuvwxyz' * 2


def my_list_append():
    lst, new_lst = list(VALUE_STR), []
    for el in lst:
        new_lst.insert(0, el)


def my_deque_append():
    lst = list(VALUE_STR)
    deq_lst = deque(lst)
    for el in lst:
        deq_lst.appendleft(el)


print(
    'list_insertLeft:  ',
    timeit(f'my_list_append()', globals=globals())
)


print(
    'deque_appendLeft: ',
    timeit(f'my_deque_append()', globals=globals())
)


def my_list_popleft():
    lst = list(VALUE_STR).copy()
    for _ in range(len(lst)):
        lst.pop(0)


def my_deque_popleft():
    lst = deque(list(VALUE_STR).copy())
    for _ in range(len(VALUE_STR)):
        lst.popleft()


print(
    'list_popleft:  ',
    timeit(f'my_list_popleft()', globals=globals())
)

print(
    'deque_popleft: ',
    timeit(f'my_deque_popleft()', globals=globals())
)


def list_extend_left():
    lst = list(VALUE_STR).copy()
    for i in range(len('0123456789')):
        lst.insert(0, len('0123456789') - i - 1)


def deque_extendleft():
    lst = deque(list(VALUE_STR).copy())
    lst.extendleft('0123456789')


print(
    'list_extend_left: ',
    timeit(f'list_extend_left()', globals=globals())
)

print(
    'deque_extendleft: ',
    timeit(f'deque_extendleft()', globals=globals())
)


# list_insertLeft:   9.8304121
# deque_appendLeft:  7.240774000000002

# list_popleft:   9.6661414
# deque_popleft:  6.8764477000000035

# list_extend_left:  5.191704600000001
# deque_extendleft:  2.745451899999999

# Методы deque работают существенно быстрее методов list
# Так же для работы с началом списка дает существенное преимущество,
# но является дополнительным подгружаемым модулем
