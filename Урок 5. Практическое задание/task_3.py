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
from timeit import timeit


deq_obj = deque([])
list_obj = list()


def app_in_deq():
    for el in range(100):
        deq_obj.append(el)


def applef_deq():
    for el in range(100, 130):
        deq_obj.appendleft(el)


def pop_left_deq():
    for el in range(50):
        deq_obj.popleft()


def app_in_list():
    for el in range(100):
        list_obj.append(el)


def app_left_list():
    for el in range(100, 130):
        list_obj.insert(0, el)


def pop_list():
    for el in range(50):
        list_obj.pop(0)


print('app_in_deq\n', timeit("app_in_deq()", 'from __main__ import app_in_deq', number=1000))
print('app_in_list\n', timeit("app_in_list()", globals=globals(),  number=1000))
print()
print('applef_deq\n', timeit("applef_deq()", globals=globals(),  number=1000))
print('app_left_list\n', timeit("app_left_list()", globals=globals(),  number=1000))
print()
print('pop_left_deq\n', timeit("pop_left_deq()", globals=globals(), number=1000))
print('pop_list\n', timeit("pop_list()", globals=globals(), number=1000))
# app_in_deq()
# applef_deq()
# pop_left_deq()
#
# app_in_list()
# app_left_list()
# pop_list()
# print(deq_obj)
# print(list_obj)

