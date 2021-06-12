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

user_list = list(range(100000))
user_deque = deque(range(100000))

print(f'Заполнение list {timeit("list(range(10000))", globals=globals(), number=10000)}')  # 1.018476
print(f'Заполнение deque {timeit("deque(range(10000))", globals=globals(), number=10000)}\n')  # 1.6075066999999998

print(f'Добавление в начало list {timeit("user_list.insert(0, 1)", globals=globals(), number=100000)}')  # 6.806392499999999
print(f'Добавление в начало deque {timeit("user_deque.appendleft(1)", globals=globals(), number=100000)}\n')  # 0.004973900000001308

print(f'Добавление в конец list {timeit("user_list.append(1)", globals=globals(), number=1000000)}')  # 0.05932630000000039
print(f'Добавление в конец deque {timeit("user_deque.append(1)", globals=globals(), number=1000000)}\n')  # 0.06976090000000035

print(f'Элемент по индексу list {timeit("user_list.index(9876)", globals=globals(), number=1000)}')  # 1.1865021999999996
print(f'Элемент по индексу deque {timeit("user_deque.index(9876)", globals=globals(), number=1000)}\n')  # 1.1112251999999998

print(f'Удаление с конца list {timeit("user_list.pop()", globals=globals(), number=1000000)}')  # 0.04302189999999939
print(f'Удаление с конца deque {timeit("user_deque.pop()", globals=globals(), number=1000000)}\n')  # 0.041148199999998525

print(f'Удаление с начала list {timeit("user_list.pop(0)", globals=globals(), number=100000)}')  # 13.006120600000001
print(f'Удаление с начала deque {timeit("user_deque.popleft()", globals=globals(), number=100000)}')  #0.004228099999998847

'''
При замерах timeit list отстаёт по всем параметрам, кроме как добавления в конец списка.
При всех остальных методах deque либо одинаковый либо в сотни раз быстрее стандартного списка, особенно при добавлении 
и удалении в начале.
'''
