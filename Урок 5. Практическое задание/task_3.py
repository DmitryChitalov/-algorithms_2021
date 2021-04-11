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

import random

from collections import deque

from timeit import timeit


tests_number = 10000

test_list = list(random.sample(range(1, 500000), 10000))

test_deque = deque(random.sample(range(1, 500000), 10000))

print(test_list)
print(test_deque)

print("Append")

print(timeit("test_list.append('1')", number=tests_number, globals=globals()))
print(timeit("test_deque.append('1')", number=tests_number, globals=globals()))

print("Insert VS Appendleft")

print(timeit("test_list.insert(0,'1')", number=tests_number, globals=globals()))
print(timeit("test_deque.appendleft('1')", number=tests_number, globals=globals()))

print("Insert")

print(timeit("test_list.insert(0,'1')", number=tests_number, globals=globals()))
print(timeit("test_deque.insert(0,'1')", number=tests_number, globals=globals()))

print("Pop")

print(timeit("test_list.pop()", number=tests_number, globals=globals()))
print(timeit("test_deque.pop()", number=tests_number, globals=globals()))

print("Pop VS Popleft")

print(timeit("test_list.pop(0)", number=tests_number, globals=globals()))
print(timeit("test_deque.popleft()", number=tests_number, globals=globals()))

print("Count")

print(timeit("test_list.count(1)", number=tests_number, globals=globals()))
print(timeit("test_deque.count(1)", number=tests_number, globals=globals()))

print("Reverse")

print(timeit("test_list.reverse()", number=tests_number, globals=globals()))
print(timeit("test_deque.reverse()", number=tests_number, globals=globals()))

print("Index")

print(timeit("test_list[8000]", number=tests_number, globals=globals()))
print(timeit("test_deque[8000]", number=tests_number, globals=globals()))

"""
-----------------------------------------------------------------------------------------------------------------------
Append - работает почти с одиннаковой эффективностью

0.00041220000000000145
0.00041060000000001096
-----------------------------------------------------------------------------------------------------------------------
appendleft vs insert
Здесь дек быстрее списка и в разы

0.1470221
0.00045090000000003183
-----------------------------------------------------------------------------------------------------------------------
insert
Здесь дек работает быстрее списка (тоже довольно сильно быстрее)

0.20385450000000005
0.0007716000000000389
-----------------------------------------------------------------------------------------------------------------------
pop
Почти одинаково эффективно для обоих

0.0008098000000000272
0.0006553000000000253
-----------------------------------------------------------------------------------------------------------------------
pop vs popleft
Дек работает быстрее списка (тоже довольно сильно быстрее)

0.04073700000000002
0.0003428999999999238
-----------------------------------------------------------------------------------------------------------------------
count
Здесь не сильно существенная разница

2.3688602000000003
2.5395810000000005
-----------------------------------------------------------------------------------------------------------------------
reverse
Дек довольно сильно быстрее

0.06469399999999936
0.1175657999999995
-----------------------------------------------------------------------------------------------------------------------
index

0.0005596000000007706
0.0021919000000005795
-----------------------------------------------------------------------------------------------------------------------
Утверждение данное в начале задачи верно. Deque работает намного быстрее в операциях удаления и добавления.
А list работает намного быстрее чем deque при досиуае к элементам (случайном дступе).
-----------------------------------------------------------------------------------------------------------------------
"""
