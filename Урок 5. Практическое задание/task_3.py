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
from collections import deque
from timeit import Timer

list_obj = []

N = int(input('Введите размер дека/списка: '))
for i in range(N):
    value = input(f'{i}) Введите что-нибудь: ')
    list_obj.append(value)

deq_obj = deque(list_obj)


def deque_append():
    deq_obj.append('something')


def deque_appendleft():
    deq_obj.appendleft('something')


def list_insert_start():
    list_obj.insert(0, 'something')


def list_insert_back():
    list_obj.insert(-1, 'something')


def deque_extend():
    deq_obj.extend(['hello', 'bye'])


def list_extend():
    list_obj.extend(['hello', 'bye'])


def deque_extendleft():
    deq_obj.extendleft(['hello', 'bye'])


def list_extendleft():
    some_list = ['hello', 'bye']
    for t in some_list:
        list_obj.append(t)


t1 = Timer("deque_append()", "from __main__ import deque_append")
print("deque append", t1.timeit(number=10000), "seconds")

t4 = Timer("list_insert_back()", "from __main__ import list_insert_back")
print("list insert back", t4.timeit(number=10000), "seconds")

t2 = Timer("deque_appendleft()", "from __main__ import deque_appendleft")
print("deque appendleft", t2.timeit(number=10000), "seconds")

t3 = Timer("list_insert_start()", "from __main__ import list_insert_start")
print("list insert start", t3.timeit(number=10000), "seconds")

t5 = Timer("deque_extend()", "from __main__ import deque_extend")
print("deque extend", t5.timeit(number=10000), "seconds")

t6 = Timer("list_extend()", "from __main__ import list_extend")
print("list extend", t6.timeit(number=10000), "seconds")

t7 = Timer("deque_extendleft()", "from __main__ import deque_extendleft")
print("deque extendleft", t7.timeit(number=10000), "seconds")

t8 = Timer("list_extendleft()", "from __main__ import list_extendleft")
print("list extendleft", t8.timeit(number=10000), "seconds")

"""
Операции с деком работают быстрее

deque append 0.001954500000000081 seconds
list insert back 0.001150700000000171 seconds

deque appendleft 0.001675000000000093 seconds
list insert start 0.06981169999999981 seconds

deque extend 0.0010973000000000788 seconds
list extend 0.0014121000000000272 seconds

deque extendleft 0.0011033000000000293 seconds
list extendleft 0.0018068000000002193 seconds
"""
