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

import random
import timeit
from collections import deque

count = 1000


def list_fill():
    simple_list = []
    for i in range(count):
        simple_list.append(i)


def deq_fill():
    deq = deque([])
    for i in range(count):
        deq.append(i)


def deq_fill_left():
    deq = deque([])
    for i in range(count):
        deq.appendleft(i)
    return deq


def list_fill_left():
    simple_list = []
    for i in range(count):
        simple_list.insert(0, i)
    return simple_list


deq = deq_fill_left()
simple_list = list_fill_left()


def deq_pop_left(d):
    for i in range(count):
        d.popleft()


def list_pop_left(l):
    for i in range(count):
        l.pop(0)


def get_list_item():
    for i in range(count):
        c = simple_list[random.randint(0, count)]


def get_deq_item():
    for i in range(count):
        c = deq[random.randint(0, count)]


t1 = timeit.Timer('list_fill()', 'from __main__ import list_fill', globals=globals())
print("list_fill work time", t1.timeit(number=1000), "milliseconds")

t2 = timeit.Timer('deq_fill()', 'from __main__ import deq_fill', globals=globals())
print("deq_fill work time", t2.timeit(number=1000), "milliseconds")

"""
По документации добавление в конец – незначительно уступает спискам, но фактически происходит даже немного быстрее
list_fill work time 0.5000646249391139 milliseconds
deq_fill work time 0.48980683204717934 milliseconds
"""

t3 = timeit.Timer('deq_fill_left()', 'from __main__ import deq_fill_left', globals=globals())
print("deq_fill_left work time", t3.timeit(number=100), "milliseconds")

t4 = timeit.Timer('list_fill_left()', 'from __main__ import list_fill_left', globals=globals())
print("list_fill_left work time", t4.timeit(number=100), "milliseconds")

"""
Добавление в начало же происходит горааздо быстрее, как и заявлено в документации
deq_fill_left work time 0.4884786820039153 milliseconds
list_fill_left work time 15.385008943034336 milliseconds
"""

t5 = timeit.Timer('get_deq_item()', 'from __main__ import get_deq_item', globals=globals())
print("get_deq_item work time", t5.timeit(number=1), "milliseconds")

t6 = timeit.Timer('get_list_item()', 'from __main__ import get_list_item', globals=globals())
print("get_list_item work time", t6.timeit(number=1), "milliseconds")
"""
Получение элемента по индексу работает примерно одинаково, хоть и заявлено, что в списках должно быть быстрее
get_deq_item work time 0.0005671760300174356 milliseconds
get_list_item work time 0.0005457389634102583 milliseconds
"""

t7 = timeit.Timer('deq_pop_left(deq)', 'from __main__ import deq_pop_left, deq', globals=globals())
print("deq_pop_left work time", t7.timeit(number=1), "milliseconds")

t8 = timeit.Timer('list_pop_left(simple_list)', 'from __main__ import list_pop_left, simple_list', globals=globals())
print("list_pop_left work time", t8.timeit(number=1), "milliseconds")

"""
удаление из начала так же происходит гораздо быстрее
deq_pop work time 4.245690070092678e-05 milliseconds
list_pop work time 0.0001086229458451271 milliseconds
"""
