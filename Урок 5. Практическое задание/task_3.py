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


def fill_l(my_list):
    for i in range(10):
        my_list.append(i)
    return my_list


def fill_d(my_deque):
    for i in range(10):
        my_deque.append(i)
    return my_deque


li = list()
d = deque()

# заполнение
print(timeit('fill_l(li)', globals=globals(), number=1))  # 7.06099999999571e-06
print(timeit('fill_d(d)', globals=globals(), number=1))  # 5.787999999999627e-06             deque

# вставка
print(timeit('li.append("asd")', globals=globals(), number=100))  # 1.3865000000001793e-05
print(timeit('d.append("asd")', globals=globals(), number=100))  # 1.183100000000381e-05     deque

# удаление
print(timeit('li.pop()', globals=globals(), number=100))  # 1.3169000000000375e-052           list
print(timeit('d.pop()', globals=globals(), number=100))  # 1.7085000000000017e-05

# вставка в начало
print(timeit('li.insert(0,"a")', globals=globals(), number=100))  # 2.2086999999997026e-05
print(timeit('d.appendleft("a")', globals=globals(), number=100))  # 1.708599999999949e-05   deque

# удаление с начала
print(timeit('li.pop(0)', globals=globals(), number=100))  # 1.9499999999998685e-05
print(timeit('d.popleft()', globals=globals(), number=100))  # 1.120699999999919e-05   deque
'''Вывод: вообщем операции с deque работают быстрее, только на удалении с конца взял вверх list'''
