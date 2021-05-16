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
import random

list_test = list(random.sample(range(1, 500000), 10000))
deque_test = deque(random.sample(range(1, 500000), 10000))

print('Сравнение append:')
print(timeit("list_test.append('1')", number=10**6, globals=globals()))
print(timeit("deque_test.append('1')", number=10**6, globals=globals()))

print('Сравнение insert и appendleft:')
print(timeit("list_test.insert(0,'1')", number=10**3, globals=globals()))
print(timeit("deque_test.appendleft('1')", number=10**3, globals=globals()))

print('Сравнение insert:')
print(timeit("list_test.insert(0,'1')", number=10**3, globals=globals()))
print(timeit("deque_test.insert(0,'1')", number=10**3, globals=globals()))

print('Сравнение pop и popleft:')
print(timeit("list_test.pop(0)", number=10**3, globals=globals()))
print(timeit("deque_test.popleft()", number=10**3, globals=globals()))

print('Сравнение count:')
print(timeit("list_test.count(1)", number=10**2, globals=globals()))
print(timeit("deque_test.count(1)", number=10**2, globals=globals()))

print('Сравнение reverse:')
print(timeit("list_test.reverse()", number=10**3, globals=globals()))
print(timeit("deque_test.reverse()", number=10**3, globals=globals()))

print('Сравнение index:')
print(timeit("list_test[8000]", number=10**6, globals=globals()))
print(timeit("deque_test[8000]", number=10**6, globals=globals()))

"""
Сравнение append - deque отрабатывает на 30% быстрее, чем list
0.08720119999999998
0.06101619999999999

Сравнение insert и appendleft - deque отрабатывает на порядок быстрее, чем list
0.7072007
6.810000000001537e-05

Сравнение insert - deque отрабатывает на порядок быстрее, чем list
0.7021615999999999
0.00010739999999986871

Сравнение pop и popleft - deque отрабатывает на порядок быстрее, чем list
0.5597397000000002
6.119999999976145e-05

Сравнение count - разница не существенная, чаще лидирует list
3.2581941999999997
3.4790628000000003

Сравнение reverse - list отрабатывает в 2 раза быстрее, чем deque
0.07639969999999963
0.18242629999999949

Сравнение index - list отрабатывает на порядок быстрее, чем deque
0.0006155000000003241
0.004326599999999736

Вывод:
При добавлении и удалении элементов deque существенно выигрывает у list по времени выполения команд.
При случайном доступе к элементам выигрывает list.
"""
