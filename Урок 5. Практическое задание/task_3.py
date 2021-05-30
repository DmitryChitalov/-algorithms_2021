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
from random import randint

n = randint(100, 1000)

lst = [randint(0, 100) for el in range(n)]
deq = deque(randint(0, 100) for el in range(n))

print(f'Время генерации элементов списка '
      f'{timeit("lst = [randint(0, 100) for el in range(n)]", globals=globals(), number=100)}')

print(f'Время генерации элементов дека '
      f'{timeit("deq = deque(randint(0, 100) for el in range(n))", globals=globals(), number=100)}')

print(f'Время добавления элементов в начало списка '
      f'{timeit("lst.insert(0, 1)", globals=globals(), number=100000)}')

print(f'Время добавления элементов в начало дека '
      f'{timeit("deq.appendleft(1)", globals=globals(), number=100000)}')

print(f'Время удаления элементов c начала списка '
      f'{timeit("lst.pop(0)", globals=globals(), number=100000)}')

print(f'Время удаления элементов c начала дека '
      f'{timeit("deq.popleft()", globals=globals(), number=100000)}')

print(f'Время добавления элементов в конец списка '
      f'{timeit("lst.append(2)", globals=globals(), number=100000)}')

print(f'Время добавления элементов в конец дека '
      f'{timeit("deq.append(2)", globals=globals(), number=100000)}')

print(f'Время удаления элементов c конца списка '
      f'{timeit("lst.pop()", globals=globals(), number=100000)}')

print(f'Время удаления элементов c конца дека  '
      f'{timeit("deq.pop()", globals=globals(), number=100000)}')

'''
Время генерации элементов дека и списка практически одинаковые как и встроеные функции pop и append. А вот 
appendleft и popleft во много раз быстрее у дека чем у списка. 
'''
