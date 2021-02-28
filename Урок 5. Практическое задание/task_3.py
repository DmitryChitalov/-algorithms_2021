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

import collections
import timeit


list1 = [n for n in range(5000)]
deque1 = collections.deque([n for n in range(5000)])

#
print(timeit.timeit('list1.append(0)', globals=globals()))
print(timeit.timeit('deque1.append(0)', globals=globals()))

print(timeit.timeit('list1.insert(0,0)', globals=globals(), number=10000))
print(timeit.timeit('deque1.appendleft(0)', globals=globals(), number=10000))

print(timeit.timeit('list1.pop()', globals=globals()))
print(timeit.timeit('deque1.pop()', globals=globals()))

print(timeit.timeit('list1.pop(0)', globals=globals(), number=10000))
print(timeit.timeit('deque1.popleft()', globals=globals(), number=10000))

print(timeit.timeit('list1[:] = [1, 2, 3] + list1', globals=globals(), number=10000))
print(timeit.timeit('deque1.extendleft([1, 2, 3])', globals=globals(), number=1000))

print(timeit.timeit('list1.extend([1, 2, 3])', globals=globals()))
print(timeit.timeit('deque1.extend([1, 2, 3])', globals=globals()))


#Во всех операциях представленных выше, deque оказался быстрее, чем лист, в частности, стоит отметить добавление элемента,
#либо же ещё одного списка, в начало списка, здесь deque оказался значительно быстрее в обоих случаях