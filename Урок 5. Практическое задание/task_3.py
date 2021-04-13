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
lst = [i for i in range(10000)]
new_lst = ['new']


def app_list(lst):
    lst.insert(0, 5)
    return lst

print('Добавление элементов в лист (list)')
print(timeit("app_list(lst)", "from __main__ import app_list, lst", number=100000))


def app_deque(my_deque):
    my_deque.appendleft(5)
    return my_deque


print('Добавление элементов в лист (deque)')
print(timeit("app_deque(my_deque)", "from __main__ import app_deque, my_deque", number=100000))


def pop_list(lst):
    lst.pop(0)
    return lst


print('Удаление первого элемента (list)')
print(timeit("pop_list(lst)", "from __main__ import pop_list, lst", number=100000))


def pop_deque(my_deque):
    my_deque.popleft()
    return my_deque


print('Удаление первого элемента (deque)')
print(timeit("pop_deque(my_deque)", "from __main__ import pop_deque, my_deque", number=100000))


def ext_list(lst):
    lst = new_lst + lst
    return lst

print('Добавление элемента с другого списка (list)')
print(timeit("ext_list(lst)", "from __main__ import ext_list, lst", number=100000))


def ext_deque(my_deque):
    my_deque.extendleft(lst)
    return my_deque


print('Добавление элемента с другого списка (deque)')
print(timeit("ext_deque(my_deque)", "from __main__ import ext_deque, my_deque", number=100000))

# Как видно из результатов, метод deque имеет большую скорость при добавлении элементов в лист и
# при удалении первого элемента, однако при добавлении элемента с другого списка метод extendleft работает медленее.
# При решении определенных задач, метод deque будет работать быстрее.
