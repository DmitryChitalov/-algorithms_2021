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


dque = deque(range(1, 100))
lst = [i for i in range(100)]
other_lst = ['a', 'b', 'c']

def append_list(lst):
    lst.insert(0, 5)
    return lst

print('Добавление элементов в list:')
print(timeit("append_list(lst)", globals=globals(), number=100000))

def append_deque(dque):
    dque.appendleft(5)
    return dque

print('Добавление элементов в deque: ')
print(timeit("append_deque(dque)", globals=globals(), number=100000))

def pop_list(lst):
    lst.pop(0)
    return lst

print('Удаление первого элемента list:')
print(timeit("pop_list(lst)", globals=globals(), number=100000))

def pop_deque(dque):
    dque.popleft()
    return dque

print('Удаление первого элемента deque:')
print(timeit("pop_deque(dque)", globals=globals(), number=100000))

def ext_list(lst):
    lst = other_lst + lst
    return lst

print('Добавление элемента из другого списка в list')
print(timeit("ext_list(lst)", globals=globals(), number=100000))

def ext_deque(dque):
    dque.extendleft(lst)
    return dque

print('Добавление элемента из другого списка в deque')
print(timeit("ext_deque(dque)", globals=globals(), number=100000))

# Метод deque имеет большую скорость при добавлении элементов в лист и
# при удалении первого элемента.
# Но добавление элемента из другого списка методом extendleft работает медленее.
# Иногда, метод deque будет работать быстрее.