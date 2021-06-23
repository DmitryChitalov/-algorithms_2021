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
# 1) Заполнение листа и очереди через append показали примерно одинаковые трудозатраты на исполнение функций;
# 2) Appendleft дека работает быстрее, чем инсерт списка
# 3) Через лист комприхеншен, дэк работает быстрее
# 4) Разворот списка через дек работает быстрее, чем встр. функция reverse
# 5) Добавление только чётных элементов через список работает быстрее
# 6) Popleft и pop работают примерно одинаково

from timeit import timeit
from collections import deque

print('Это список')

fill_list = [el for el in range(1, 101)]
insert_list = [el for el in range(1, 101)]
insert_list.insert(0, [el for el in range(1, 100)])
a = [el for el in range(1, 101)]
reverse_list = a.reverse()
even_numbers = [el for el in range(1, 101) if el % 2 == 0]
pop_list = [el for el in range(1, 100)]
pop_list.pop()

print(timeit('fill_list', globals=globals()))
print(timeit('insert_list', globals=globals()))
print(timeit('reverse_list', globals=globals()))
print(timeit('even_numbers', globals=globals()))
print(timeit('pop_list', globals=globals()))

print('Это дек')
fill_deque = deque(range(1, 101))
append_deque = deque(range(1, 101))
append_deque.appendleft([el for el in range(1, 100)])
reversed_deque = deque(reversed(range(1, 101)))
even_numbers_deque = deque(range(2, 101, 2))
pop_deque = deque(range(1, 101))
pop_deque.popleft()
print(timeit('fill_deque', globals=globals()))
print(timeit('append_deque', globals=globals()))
print(timeit('reversed_deque', globals=globals()))
print(timeit('even_numbers_deque', globals=globals()))
print(timeit('pop_deque', globals=globals()))
