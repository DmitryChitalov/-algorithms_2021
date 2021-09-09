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

my_list = []
my_deque = deque()
items_count = 1000

my_list_2 = [i for i in range(items_count)]
my_deque_2 = [i for i in range(items_count)]


def lst_fill_insert(lst):
    for i in range(items_count):
        lst.insert(0, i)
    return lst


def dq_fill_appendleft(dq):
    for i in range(items_count):
        dq.appendleft(i)
    return dq


def lst_fill_append(lst):
    for i in range(items_count):
        lst.append(i)
    return lst


def dq_fill_append(dq):
    for i in range(items_count):
        dq.append(i)
    return dq


def lst_extendleft(lst):
    lst = my_list_2 + lst
    return lst


def dq_extendleft(dq):
    dq.extendleft(my_deque_2)
    return dq


def lst_modif(lst):
    for i in range(items_count):
        lst[i] = i + 1
    return lst


def dq_modif(dq):
    for i in range(items_count):
        dq[i] = i + 1
    return dq


def lst_popleft(lst):
    for i in range(items_count):
        lst.pop(0)
    return lst


def dq_popleft(dq):
    dq.popleft()
    return dq


print(f'lst_fill_insert: {timeit("lst_fill_insert(my_list)", globals=globals(), number=100)}')
print(f'dq_fill_appendleft: {timeit("dq_fill_appendleft(my_deque)", globals=globals(), number=100)}')
print(f'lst_fill_append: {timeit("lst_fill_append(my_list)", globals=globals(), number=100)}')
print(f'dq_fill_append: {timeit("dq_fill_append(my_deque)", globals=globals(), number=100)}')
print(f'lst_extendleft: {timeit("lst_extendleft(my_list)", globals=globals(), number=100)}')
print(f'dq_extendleft: {timeit("dq_extendleft(my_deque)", globals=globals(), number=100)}')
print(f'lst_modif: {timeit("lst_modif(my_list)", globals=globals(), number=100)}')
print(f'dq_modif: {timeit("dq_modif(my_deque)", globals=globals(), number=100)}')
print(f'lst_popleft: {timeit("lst_popleft(my_list)", globals=globals(), number=100)}')
print(f'dq_popleft: {timeit("dq_popleft(my_deque)", globals=globals(), number=100)}')

"""
Выводы:

1. Для вставки элементов в начало массива удобней работать с деком, т.к. appendleft для дека выполняется гораздо 
быстрее, чем insert для списка.
2. Обычный append выполняется примерно с одинаковой скоростью и для списка и для дека(чуть быстрее для дека).
3. При вставке элементов одного массива в начало другого массива также удобней работать с деком, операция extendleft 
выполняется гораздо быстрее, чем аналог у списков.
4. Операция изменения элементов работает быстрее для списка.
5. Операция удаления элементов с начала массива работает быстрее для дека.

"""