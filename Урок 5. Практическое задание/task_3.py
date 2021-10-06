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
print(timeit('fill_l(li)', globals=globals(), number=10000))        # 0.015863854000000004     list
print(timeit('fill_d(d)', globals=globals(), number=10000))         # 0.016802670000000006

# вставка
print(timeit('li.append("asd")', globals=globals(), number=10000))  # 0.001269783999999996
print(timeit('d.append("asd")', globals=globals(), number=10000))   # 0.0011314399999999974     deque

# удаление
print(timeit('li.pop()', globals=globals(), number=10000))          # 0.00102100799999999
print(timeit('d.pop()', globals=globals(), number=10000))           # 0.0010100690000000023    deque

# вставка в начало
print(timeit('li.insert(0,"a")', globals=globals(), number=10000))  # 0.836891959
print(timeit('d.appendleft("a")', globals=globals(), number=10000)) # 0.0010183980000000314   deque

# удаление с начала
print(timeit('li.pop(0)', globals=globals(), number=10000))         # 0.527847933
print(timeit('d.popleft()', globals=globals(), number=10000))       # 0.0009307079999998358   deque

'''Вывод: вообщем операции с deque работают быстрее, только на заполнении списка операции 
append немного превосходят deque'''
