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

lis = [i for i in range(0, 10000)]
deq = deque([i for i in range(0, 10000)])

print('fill operation')
print('list:')
print(timeit('lis = [i for i in range(0, 10000)]', number=10000))
print('deque:')
print(timeit('deq = deque([i for i in range(0, 10000)])', globals=globals(), number=10000))
print()

print('operation of insert-at-the-head for a list')
print(timeit('lis.insert(0, 10000)', globals=globals(), number=10000))
print(timeit('lis.pop(0)', globals=globals(), number=10000))
print(timeit('for i in range(100):'
             'lis.insert(i, 0)', globals=globals(), number=1000))
print()

print('operation of insert-at-the-head for a deque')
print(timeit('deq.appendleft(10000)', globals=globals(), number=10000))
print(timeit('deq.popleft()', globals=globals(), number=10000))
print(timeit('deq.extendleft(i for i in range(100))', globals=globals(), number=1000))
print()

print('Tests for the list')
print(timeit('lis.extend(i for i in range(100))', globals=globals(), number=10000))
print(timeit('lis.remove(50)', globals=globals(), number=100))
print()

print('Tests for the deque')
print(timeit('deq.extend(i for i in range(100))', globals=globals(), number=10000))
print(timeit('deq.remove(50)', globals=globals(), number=100))
