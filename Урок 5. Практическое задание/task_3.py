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


list_x = [el for el in range(10000)]
list_y = deque(list_x)
list_z = [el for el in range(1000)]


print(f'Замер функции appendleft для deque: '
      f'{timeit(stmt="list_y.appendleft(1)", globals=globals(), number=100000)}')
print(f'Замер функции insert для list: '
      f'{timeit(stmt="list_x.insert(0, 1)", globals=globals(), number=100000)}')
# Замер функции appendleft для deque: 0.004451999999999991
# Замер функции insert для list: 2.399234

print(f'Замер функции popleft для deque: '
      f'{timeit(stmt="list_y.popleft()", globals=globals(), number=100000)}')
print(f'Замер функции pop для list: '
      f'{timeit(stmt="list_x.pop(0)", globals=globals(), number=100000)}')
# Замер функции popleft для deque: 0.004429000000000016
# Замер функции pop для list: 1.2978537

print(f'Замер функции extendleft для deque: '
      f'{timeit(stmt="list_y.extendleft(list_z)", globals=globals(), number=100000)}')
print(f'Замер объединение списков: '
      f'{timeit(stmt="list_z + list_x", globals=globals(), number=100000)}')
# Замер функции extendleft для deque: 1.1952055000000001
# Замер объединение списков: 1.8587627000000007


# По данным замерам можно сделать вывод что если нужен список с быстрым доступом
# к началу и концу списка быстрее будет работать deque.
