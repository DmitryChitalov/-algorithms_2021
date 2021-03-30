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

my_deque = deque(range(1, 100000))
my_list = list(range(1, 100000))
new_list = ['qwer']


def app_list(my_list):
    my_list.insert(0, 5)
    return my_list


print('app_list')
print(timeit("app_list(my_list)", "from __main__ import app_list, my_list", number=100000))


def app_deque(my_deque):
    my_deque.appendleft(5)
    return my_deque


print('app_deque')
print(timeit("app_deque(my_deque)", "from __main__ import app_deque, my_deque", number=100000))


def pop_list(my_list):
    my_list.pop(0)
    return my_list


print('pop_list')
print(timeit("pop_list(my_list)", "from __main__ import pop_list, my_list", number=100000))


def pop_deque(my_deque):
    my_deque.popleft()
    return my_deque


print('pop_deque')
print(timeit("pop_deque(my_deque)", "from __main__ import pop_deque, my_deque", number=100000))


def ext_list(my_list):
    my_list = new_list + my_list
    return my_list


print('ext_list')
print(timeit("ext_list(my_list)", "from __main__ import ext_list, my_list", number=100000))


def ext_deque(my_deque):
    my_deque.extendleft(new_list)
    return my_deque


print('ext_deque')
print(timeit("ext_deque(my_deque)", "from __main__ import ext_deque, my_deque", number=100000))

''' При добавление элементов deque обладает большей скоростью за счет метода appendleft'''
''' При удалении элементов deque в начале списка через индекс медленнее чем метод очереди popleft'''
''' При добавлении элементов с другого списка метод extendleft работает быстрее'''
''' Благодаря методам которыми обладает deque в определенных задачах можно сильно ускорить процесс'''
# app_list
# 7.8018512
# app_deque
# 0.009326899999999583
# pop_list
# 10.0481384
# pop_deque
# 0.008857299999998958
# ext_list
# 29.371171
# ext_deque
# 0.012885400000001823