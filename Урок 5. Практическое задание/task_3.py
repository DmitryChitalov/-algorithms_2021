"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

Задача: 
1) создайте простой список (list) и очередь (deque). Сделайте замеры и оцените что заполняется быстрее.
2) Выполните различные операции с каждым из объектов. Сделайте замеры и оцените, где и какие операции быстрее.

Не забудьте, что сравнивать, например, можно операцию appendleft дека и insert списка и т.д.
"""

from timeit import timeit
from collections import deque
from random import randint

lst = [randint(0, 999999) for _ in range(20)]
dq = deque(lst)

print('Замеры операции заполнения для списка через timeit: ' + str(timeit(
    'lst = [randint(0, 999999) for _ in range(20)]',
    globals=globals(), number=10000)))

print('Замеры операции заполнения для дека через timeit: ' + str(timeit(
    'dq = deque([randint(0, 999999) for _ in range(20)])',
    globals=globals(), number=10000)))


print('Замеры операции append для списка через timeit: ' + str(timeit(
    'lst.append(1000)',
    globals=globals())))

print('Замеры операции append для дека через timeit: ' + str(timeit(
    'dq.append(1000)',
    globals=globals())))

print('Замеры операции insert для списка через timeit: ' + str(timeit(
    'lst.insert(0, 1000)',
    globals=globals(), number=10000)))

print('Замеры операции appendleft для дека через timeit: ' + str(timeit(
    'dq.appendleft(1000)',
    globals=globals(), number=10000)))

print('Замеры операции pop для списка через timeit: ' + str(timeit(
    'lst.pop()',
    globals=globals())))

print('Замеры операции pop для дека через timeit: ' + str(timeit(
    'dq.pop()',
    globals=globals())))

print('Замеры операции pop(0) для списка через timeit: ' + str(timeit(
    'lst.pop(0)',
    globals=globals(), number=10000)))

print('Замеры операции popleft для дека через timeit: ' + str(timeit(
    'dq.popleft()',
    globals=globals(), number=10000)))

print('Замеры операции reverse для списка через timeit: ' + str(timeit(
    'lst.reverse()',
    globals=globals())))

print('Замеры операции reverse для дека через timeit: ' + str(timeit(
    'dq.reverse()',
    globals=globals())))

'''
Вывод:
Документация говорит правду. При добавлении или удалении элемента из конца списка, скорости у дека и списка похожие.
Заполняются структуры по времени так же похоже.
Добавляется чуть быстрее в дек, удаляется же у меня чуть быстрее из списка.
В операциях же с началом списка/дека дек быстрее на порядки.
Разворачиваются они за примерно одно и то же время.

Замеры операции заполнения для списка через timeit: 0.175265
Замеры операции заполнения для дека через timeit: 0.19678579999999998
Замеры операции append для списка через timeit: 0.1323956
Замеры операции append для дека через timeit: 0.08426809999999998
Замеры операции insert для списка через timeit: 7.1946589
Замеры операции appendleft для дека через timeit: 0.0005917999999995871
Замеры операции pop для списка через timeit: 0.08131100000000036
Замеры операции pop для дека через timeit: 0.13335970000000064
Замеры операции pop(0) для списка через timeit: 0.014750900000000122
Замеры операции popleft для дека через timeit: 0.0005259000000004121
Замеры операции reverse для списка через timeit: 0.05679020000000001
Замеры операции reverse для дека через timeit: 0.06671010000000077
'''
