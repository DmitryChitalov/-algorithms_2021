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


def new_lst(my_lst, new_my_lst):
    my_lst.reverse()
    my_lst.extend(new_my_lst)
    return my_lst.reverse()


my_lst = [i for i in range(10000)]
my_dq = deque([i for i in range(10000)])
new_my_lst = [1, 2, 3]
print('Скорость добавления в конец:')
print(f'{timeit("my_lst.append(0)", globals=globals(), number=10000)} - Список')  # 0.0014866000000000046
print(f'{timeit("my_dq.append(0)", globals=globals(), number=10000)} - deque')  # 0.0012338000000000071
print('Скорость добавления в начало:')
print(f'{timeit("my_lst.insert(0,0)", globals=globals(), number=10000)} - Список')  # 0.32608489999999996
print(f'{timeit("my_dq.appendleft(0)", globals=globals(), number=10000)} - deque')  # 0.00137769999999998
print('Скорость извлечения с конца:')
print(f'{timeit("my_lst.pop()", globals=globals(), number=10000)} - Список')  # 0.0012912999999999952
print(f'{timeit("my_dq.pop()", globals=globals(), number=10000)} - deque')  # 0013548999999999367
print('Скорость извлечения с начала:')
print(f'{timeit("my_lst.pop(0)", globals=globals(), number=10000)} - Список')  # 0.09027180000000001
print(f'{timeit("my_dq.popleft()", globals=globals(), number=10000)} - deque')  # 0.0013767000000000085
print('Скорость добавления в начало все элементы списка начиная с последнего:')
print(f'{timeit("new_lst(my_lst,new_my_lst)", globals=globals(), number=10000)} - Список')  # 0.4562405999999999
print(f'{timeit("my_dq.extendleft(new_my_lst)", globals=globals(), number=10000)} - deque')  # 0.002639300000000011
"""
Deque выполяет быстрее операции с началом списка.
Скорости в работе с концом списка отличаются незначительно.
"""
