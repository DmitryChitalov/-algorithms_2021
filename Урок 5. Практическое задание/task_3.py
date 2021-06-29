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


from collections import deque
from timeit import timeit


my_list = []
my_deque = deque(my_list)


print(timeit("my_list.append('0')", globals=globals(), number=1000000))     # 0.234302912
print(timeit("my_deque.append('0')", globals=globals(), number=1000000))    # 0.17646894800000001

# Операция добавления элементов в deque производиться быстрее

print(timeit("my_list.pop()", globals=globals(), number=1000000))       # 0.147382063
print(timeit("my_deque.pop()", globals=globals(), number=1000000))      # 0.14765003200000004

# Удаление последнего элемента занимает одинаковое время

print(timeit("my_list.insert(-1, '0')", globals=globals(), number=1000000))     # 0.32577926599999996
print(timeit("my_deque.appendleft('0')", globals=globals(), number=1000000))    # 0.18667546999999995

# Вставка в начало списка также производиться быстрее в deque

print(timeit("my_list.pop(0)", globals=globals(), number=1000))       # 6.971623449999999
print(timeit("my_deque.popleft()", globals=globals(), number=1000))      # 0.00013611199999985502

# Удаление элементов с начала списка производится значительно быстрее в deque
