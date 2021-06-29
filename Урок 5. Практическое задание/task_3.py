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

import timeit
from collections import deque


def lst_append(lst):
    lst.append(1)
    return lst


def deque_append(deq):
    deq.append(1)
    return deq


def lst_extend(lst):
    lst.extend([1, 2])
    return lst


def deque_extend(deq):
    deq.extend([1, 2])
    return deq


def lst_pop(lst):
    lst.pop()
    return lst


def deque_pop(deq):
    deq.pop()
    return deq


def lst_insert(lst):
    lst.insert(0, 1)
    return lst


def deque_appendleft(deq):
    deq.appendleft(1)
    return deq


def lst_del(lst):
    del lst[0]
    return lst


def deque_popleft(deq):
    deq.popleft()
    return deq


def lst_ind(lst):
    lst[1] = 10
    return lst


def deque_ind(deq):
    deq[1] = 10
    return deq


lst = []
deq = deque()

stmt = ["lst_append(lst)",
        "deque_append(deq)",
        "lst_extend(lst)",
        "deque_extend(deq)",
        "lst_pop(lst)",
        "deque_pop(deq)",
        "lst_ind(lst)",
        "deque_ind(deq)"]

for st in stmt:
    print(f'на выполение функции {st} затрачено времени: '
          f'{timeit.timeit(st, globals=globals())}')

stmt_1 = ["lst_insert(lst)",
          "deque_appendleft(deq)",
          "lst_del(lst)",
          "deque_popleft(deq)"]

for st in stmt_1:
    print(f'на выполение функции {st} затрачено времени: '
          f'{timeit.timeit(st, number=10000, globals=globals())}')

"""
на выполение функции lst_append(lst) затрачено времени: 0.0933485
на выполение функции deque_append(deq) затрачено времени: 0.07480219999999999
на выполение функции lst_extend(lst) затрачено времени: 0.13529709999999995
на выполение функции deque_extend(deq) затрачено времени: 0.14120410000000005
на выполение функции lst_pop(lst) затрачено времени: 0.07389999999999997
на выполение функции deque_pop(deq) затрачено времени: 0.07789789999999996
на выполение функции lst_ind(lst) затрачено времени: 0.06508040000000004
на выполение функции deque_ind(deq) затрачено времени: 0.07664349999999998
на выполение функции lst_insert(lst) затрачено времени: 11.0715462
на выполение функции deque_appendleft(deq) затрачено времени: 0.000790699999999589
на выполение функции lst_del(lst) затрачено времени: 12.103831399999999
на выполение функции deque_popleft(deq) затрачено времени: 0.0007644000000013307

При использование стандартных для списков методов extend, pop список и двусторонняя очередь работают одинаково.
Однако, при использовании метода append быстрее работет двусторонняя очередь, но при получении элемента по индексу 
быстрее отрабатывает уже список. Методов appendleft и popleft у списков не существует, а их аналоги, в отличии от 
методов очереди appendleft и popleft, имеют линейную сложность О(n). Таким образом можно сделать вывод, что для 
вставки и удаления элементов предпочтительнее использовать deque, но если требуется быстрый случайный доступ к элементу
следует использовать list.
"""
