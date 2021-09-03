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
from timeit import timeit


def fill_list():
    test_list = []
    for i in range(10000):
        test_list.append(i)
    return test_list


def fill_deque():
    test_deque = deque( )
    for i in range(10000):
        test_deque.append(i)
    return test_deque


print('Заполнение')
print(timeit('fill_list()', globals=globals( ), number=1000))
print(timeit('fill_deque()', globals=globals( ), number=1000))
"""
Deque заполняется быстрее, чем list.
"""
my_list = fill_list( )
my_deque = fill_deque( )


def left_insert_deque():
    my_deque.appendleft(100)
    return my_deque


def left_insert_list():
    my_list.insert(0, 100)
    return my_list


print('Вставка в начало массива')
print(timeit('left_insert_list()', globals=globals( ), number=10000))
print(timeit('left_insert_deque()', globals=globals( ), number=10000))
"""
Вставка в начало deque выполняется в разы быстрее, чем в list. 
"""


def pop_left_deque():
    my_deque.popleft( )
    return my_deque


def pop_left_list():
    my_list.pop(0)
    return my_list


print('Достать значение из начала массива')
print(timeit('pop_left_list()', globals=globals( ), number=10000))
print(timeit('pop_left_deque()', globals=globals( ), number=10000))
"""
Получение значения из начала массива также в несколько раз быстрее осуществляется у deque.
"""


def extend_left_deque():
    my_deque.extendleft([1, 2, 3])
    return my_deque


def extend_left_list():
    my_list[:0] = [1, 2, 3]
    return my_list


print('Extendleft list/deque')
print(timeit('extend_left_list()', globals=globals( ), number=10000))
print(timeit('extend_left_deque()', globals=globals( ), number=10000))
"""
Добавление массива в начало deque выполняется в несколько раз быстрее.
"""


def index_deque():
    return my_deque[100]


def index_list():
    return my_list[100]


print('Indexing list/deque')
print(timeit('index_list()', globals=globals( )))
print(timeit('index_deque()', globals=globals( )))
"""
Получение элемента по индексу deque выполняет дольше.
"""

