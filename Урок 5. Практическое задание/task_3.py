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

my_list = list(range(1000))
my_deque = deque(range(1000))

print(f'append list : {timeit("my_list.append(1)", number=10000, globals=globals())}')
print(f'append deque : {timeit("my_deque.append(1)", number=10000, globals=globals())}')
print('*' * 20)
print(f'appendleft deque : {timeit("my_deque.appendleft(1)", number=10000, globals=globals())}')
print(f'insert deque (0, 1) : {timeit("my_deque.insert(0, 1)", number=10000, globals=globals())}')
print(f'insert list (0, 1) : {timeit("my_list.insert(0, 1)", number=10000, globals=globals())}')
print(f'insert list (250, 1) : {timeit("my_list.insert(200, 1)", number=10000, globals=globals())}')
print(f'insert deque (250, 1) : {timeit("my_deque.insert(200, 1)", number=10000, globals=globals())}')
print('*' * 20)
print(f'index list : {timeit("my_list.index(500)", number=10000, globals=globals())}')
print(f'index deque : {timeit("my_deque.index(500)", number=10000, globals=globals())}')
print('*' * 20)
print(f'reverse list : {timeit("my_list.reverse()", number=10000, globals=globals())}')
print(f'reverse deque : {timeit("my_deque.reverse()", number=10000, globals=globals())}')
print('*' * 20)
print(f'pop list : {timeit("my_list.pop()", number=10000, globals=globals())}')
print(f'pop deque : {timeit("my_deque.pop()", number=10000, globals=globals())}')
print('*' * 20)
print(f'pop list (0) : {timeit("my_list.pop(0)", number=10000, globals=globals())}')
print(f'popleft deque : {timeit("my_deque.popleft()", number=10000, globals=globals())}')

"""
append list : 0.0006513000000000005
append deque : 0.0005881999999999971
********************
appendleft deque : 0.0006116000000000038
insert deque (0, 1) : 0.0010118999999999961
insert list (0, 1) : 0.1064376
insert list (250, 1) : 0.1735652
insert deque (250, 1) : 0.005812300000000048
********************
index list : 2.7929538
index deque : 4.0339358999999995
********************
reverse list : 0.12165530000000047
reverse deque : 0.38219849999999944
********************
pop list : 0.0005366999999996125
pop deque : 0.00047740000000029426
********************
pop list (0) : 0.02334999999999976
popleft deque : 0.0004809000000003394


Основное правильно по работе с deque подтвердилось.
deque значительно лучше выполняет свои функции: append слева и pop слева
минус deque - плохо работает deque с функцией reverse и index (в два раза медленней)
Если нужен быстрый случайный доступ - используем list.
"""