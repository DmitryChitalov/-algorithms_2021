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

list_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
deque_arr = deque(list_arr)


def deque_appendleft():
    deque_arr.appendleft('abc')


def list_insert():
    list_arr.insert(0, 'abc')


def deque_extend():
    deque_arr.extend(list_arr)


def list_extend():
    list_arr.extend(list_arr)


# Добавление элементов в начало
print(
    f"{timeit('deque_appendleft()', 'from __main__ import deque_appendleft', number=1000)}")  # -> 0.000212799999999999
print(f"{timeit('list_insert()', 'from __main__ import list_insert', number=1000)}")  # -> 0.00025510000000000116

# Добавление элементов в конец
print(f"{timeit('deque_extend()', 'from __main__ import deque_extend', number=1000)}")
print(f"{timeit('list_extend()', 'from __main__ import list_extend', number=10)}")  # if number > 10 --> memory end

"""
Deque будет выполняться быстрее list, так как списки больше оптимизированы для быстрых операций с 
последовательностями фиксированной длины и требуют затрат O(n), а deque поддерживает поточно-ориентированные, 
эффективные по памяти операции добавления и извлечения элементов последовательности с любой стороны с примерно 
одинаковой производительностью O(1) в любом направлении.
"""
