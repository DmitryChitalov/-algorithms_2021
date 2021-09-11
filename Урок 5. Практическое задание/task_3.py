"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

Задача: 
1) создайте простой список (list) и очередь (deque). Сделайте замеры и оцените что заполняется быстрее.
2) Выполните различные операции с каждым из объектов. Сделайте замеры и оцените, где и какие операции быстрее.

В первую очередь необходимо выполнить замеры для ф-ций appendleft, popleft, extendleft дека и для их аналогов у списков.
"""

from collections import deque
import timeit


my_list = []
my_deque = deque()


def fill_list(some_list):
    some_list = [i for i in range(10000)]
    return some_list


print('Заполнение list')
print(timeit.timeit('fill_list(my_list)', globals=globals(), number=1000))


def fill_deque(some_deque):
    some_deque = [i for i in range(10000)]
    return some_deque


print('Заполнение deque')
print(timeit.timeit('fill_deque(my_deque)', globals=globals(), number=1000))


def app_list(some_list):
    for i in range(100):
        some_list.insert(0, i)
    return some_list


print('Добавление в начало list')
print(timeit.timeit('app_list(my_list)', globals=globals(), number=1000))


def app_deque(some_deque):
    for i in range(100):
        some_deque.appendleft(i)
    return some_deque


print('Добавление в начало deque')
print(timeit.timeit('app_deque(my_deque)', globals=globals(), number=1000))


def pop_list(some_list):
    for i in range(100):
        some_list.pop(0)
    return some_list


print('Удаление из начала list')
print(timeit.timeit('pop_list(my_list)', globals=globals(), number=1000))


def pop_deque(some_deque):
    for i in range(100):
        some_deque.popleft()
    return some_deque


print('Удаление из начала deque')
print(timeit.timeit('pop_deque(my_deque)', globals=globals(), number=1000))

new_list = [i for i in range(1000)]
new_deque = deque([i for i in range(1000)])


def ext_list(some_list):
    some_list.reverse()
    new_list.reverse()
    some_list.extend(new_list)
    some_list.reverse()
    return some_list


print('Добавление элементов в начало list')
print(timeit.timeit('ext_list(my_list)', globals=globals(), number=1000))


def ext_deque(some_deque):
    some_deque.extendleft(new_deque)
    return some_deque


print('Добавление элементов в начало deque')
print(timeit.timeit('ext_deque(my_deque)', globals=globals(), number=1000))


def el_list(some_list):
    for i in range(100, 200):
        some_list[i] = 7
    return some_list


print('Изменение случайного элемента list')
print(timeit.timeit('el_list(my_list)', globals=globals(), number=1000))


def el_deque(some_deque):
    for i in range(100, 200):
        some_deque[i] = 7
    return some_deque


print('Изменение случайного элемента deque')
print(timeit.timeit('el_deque(my_deque)', globals=globals(), number=1000))

"""
Вывод: По результатам замеров deque заполняется чуть быстрее, чем list.
Добавление элемента в начало, удаление из начала и добавление группы элементов значительно быстрее в deque.
А вот доступ к заданному элементу в list оказался быстрее, чем в deque.
"""
