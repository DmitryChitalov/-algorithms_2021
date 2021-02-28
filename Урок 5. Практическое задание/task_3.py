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

my_list = list(range(10))
my_deque = deque(my_list)


print(timeit('my_list.append(1)', globals=globals()))
print(timeit('my_deque.append(1)', globals=globals()))

print()

print(timeit('my_list.insert(1, 0)', globals=globals(), number=1000))
print(timeit('my_deque.appendleft(0)', globals=globals(), number=1000))

print()

print(timeit('my_list.count(1)', globals=globals(), number=1000))
print(timeit('my_deque.count(1)', globals=globals(), number=1000))

print()

print(timeit('my_list.pop()', globals=globals(), number=10000))
print(timeit('my_deque.pop()', globals=globals(), number=10000))

print()

print(timeit('my_list.pop(0)', globals=globals(), number=10000))
print(timeit('my_deque.popleft()', globals=globals(), number=10000))

"""
Замеры показали, что операция подсчета количества вхождений элемента в список 
выполняется горазджо быстрее, чем аналогичная операция для дэка, так как дэк создавался 
для других нужд.

Зато операции добавления и удаления элементов выполняются либо за одинаковое время (append, pop), 
либо гораздо быстрее (appendleft, popleft).
"""