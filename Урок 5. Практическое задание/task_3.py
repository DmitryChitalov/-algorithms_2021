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


def init_list():
    return [num ** 3 for num in range(1000)]


def init_deque():
    return deque([num ** 3 for num in range(1000)])


def extend_left_list():
    my_list.insert(0, 1)
    my_list.insert(0, 2)
    my_list.insert(0, 3)


my_list = init_list()
my_deque = init_deque()

print(timeit("init_list", globals=globals()))  # 0.015773799999999998
print(timeit("init_deque", globals=globals()))  # 0.017491299999999994
print(timeit("my_list.append(1)", globals=globals()))  # 0.0616037
print(timeit("my_deque.append(1)", globals=globals()))  # 0.04378549999999999
print(timeit("my_list.insert(0, 2)", globals=globals(), number=10000))  # 8.0945955
print(timeit("my_deque.appendleft(2)", globals=globals(), number=10000))  # 0.000617899999999527
print(timeit("my_list.pop(0)", globals=globals(), number=10000))  # 5.6562016999999996
print(timeit("my_deque.popleft()", globals=globals(), number=10000))  # 0.0004259999999991493
print(timeit("extend_left_list()", globals=globals(), number=10000))  # 22.4794741
print(timeit("my_deque.extendleft([1,2,3])", globals=globals(), number=10000))  # 0.0020577000000004944

# Получилось, что все операции на несколько порядков быстрее получились у типа deque, чем у list
# за исключением создания, но и там разница небольшая.
# Получается настолько быстро работает deque, сохраняя при этом все методы list, что его желательно использовать
# во всех случаях, когда необходимо вставлять и извлекать объект.
