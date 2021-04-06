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

from timeit import timeit
from collections import deque

lst = ["hsfghf", 5, "afger", [1, "r"], 7]
dq = deque()
dq.extend(lst)

print(timeit('lst.append("sdf")', globals = globals(), number=100000000))
print(timeit('dq.append("sdf")', globals = globals(), number=100000000))

# 4.842087708
# 4.898164427
# По скорости примерно одинаково

print(timeit('lst.insert(0,"sdf")', globals = globals(), number=5000))
print(timeit('dq.appendleft("sdf")', globals = globals(), number=5000))

# 40.508913542
# 0.00035782700000197565
# Видно что deque значительно лучше справилься со вставкой эдемента в начало

print(timeit('lst.pop()', globals = globals(), number=10000000))
print(timeit('dq.pop()', globals = globals(), number=10000000))

# 0.4636373549999999
# 0.46903092700000015
# По скорости примерно одинаково

print(timeit('lst.pop(0)', globals = globals(), number=5))
print(timeit('dq.popleft()', globals = globals(), number=5))

# 2.8629999999640887e-06
# 1.2489999998699375e-06
# В удалении первого элемента deque лучше

# В целом видно что специальные функции deque выполняет быстрее