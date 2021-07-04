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


my_list = []

my_list_deque = deque()


def app():
    my_list.append("asd")
    my_list.append("2sd")
    my_list.append("as")
    return my_list


print(app())


def appdequ():
    my_list_deque.append("asd")
    my_list_deque.append("2sd")
    my_list_deque.append("as")
    return my_list_deque


print(appdequ())


def insdeq():
    for i in range(3):
        my_list_deque.appendleft(i)
    return my_list_deque


print(insdeq())


def ins_list():
    for i in range(3):
        my_list.insert(0, i)
    return my_list

print(ins_list())


print(
    timeit(
        "app()",
        globals=globals(),
        number=100
    )
)

print(
    timeit(
        "appdequ()",
        globals=globals(),
        number=100
    )
)

print(
    timeit(
        "insdeq()",
        globals=globals(),
        number=100
    )
)

print(
    timeit(
        "ins_list()",
        globals=globals(),
        number=100
    )
)

""" Операции с deque выполняются бестрее(операция по добавлению в список выполняется не намного быстрее,
 а команда добавления в начало списка выполняется в deque в 2 раза быстрее)"""