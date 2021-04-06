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

my_list = list(range(2000))

my_deque = deque(range(2000))


# Пробовал двумя способами сделать добавление в начало списка. Оба варианта работают медленней deque
def add_in_list(my_list: list):
    # my_list[:] = [11] + my_list[:]
    my_list.insert(0, 11)
    return my_list


def add_in_deque(my_deque: deque):
    my_deque.appendleft(11)
    return my_deque


print('List add')
print(timeit("add_in_list(my_list)", "from __main__ import add_in_list, my_list", number=1000))
print('Degue add')
print(timeit("add_in_deque(my_deque)", "from __main__ import add_in_deque, my_deque", number=1000))
print()


def pop_in_list(my_list: list):
    my_list.pop(0)
    return my_list


def pop_in_deque(my_deque: deque):
    my_deque.popleft()
    return my_deque


print('List pop')
print(timeit("pop_in_list(my_list)", "from __main__ import pop_in_list, my_list", number=1000))
print('Degue pop')
print(timeit("pop_in_deque(my_deque)", "from __main__ import pop_in_deque, my_deque", number=1000))
print()


def extend_in_list(my_list: list):
    my_list[:] = [1, 1, 1, 1] + my_list
    return my_list


def extend_in_deque(my_deque: deque):
    my_deque.extendleft([2, 2, 2, 2])
    return my_deque


print('List extend')
print(timeit("extend_in_list(my_list)", "from __main__ import extend_in_list, my_list", number=1000))
print('Degue extend')
print(timeit("extend_in_deque(my_deque)", "from __main__ import extend_in_deque, my_deque", number=1000))

"""
Добавление и удаление элемента очереди быстрее с deque  т.к. при append extend или pop дек добавляет и убирает элемент
со сложностью O(1), тогда как списко переназначает ссылки всех элементов элементов с O(n)
"""
