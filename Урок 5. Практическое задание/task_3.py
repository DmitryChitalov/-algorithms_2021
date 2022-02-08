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

from timeit import timeit
from collections import deque


test_list = list(range(99000))
deque_list = deque(list(range(99000)))

print(f'Заполнение списка: '
      f'{timeit("test_list = list(range(100))", globals=globals(), number=99000)}')

print(f'Заполнение дека: '
      f'{timeit("deque_list = deque(list(range(100)))", globals=globals(), number=99000)}')

print(f'Добавление в конец списка: '
      f'{timeit("test_list.append(1)", globals=globals(), number=990000)}')

print(f'Добавление в конец дека: '
      f'{timeit("deque_list.append(1)", globals=globals(), number=99000)}')

print(f'Добавление в начало списка: '
      f'{timeit("test_list.insert(0, 1)", globals=globals(), number=99000)}')

print(f'Добавление в начало дека: '
      f'{timeit("deque_list.appendleft(1)", globals=globals(), number=99000)}')

print(f'Удаление с конца списка: '
      f'{timeit("test_list.pop(-1)", globals=globals(), number=99000)}')

print(f'Удаление с конца дека: '
      f'{timeit("deque_list.pop()", globals=globals(), number=99000)}')

print(f'Удаление с начала списка: '
      f'{timeit("test_list.pop(0)", globals=globals(), number=99000)}')

print(f'Удаление с начала дека: '
      f'{timeit("deque_list.popleft()", globals=globals(), number=99000)}')

print(f'Поиск по индексу списка: '
      f'{timeit("test_list.index(5000)", globals=globals(), number=99000)}')

print(f'Поиск по индексу дека: '
      f'{timeit("deque_list.index(5000)", globals=globals(), number=99000)}')

"""
Заполнение списка происходит быстрее, чем заполнение дека
Операции добавления и удаления в конец незначительно быстрее у дека
Операции добавления и удаления из начала быстрее у дека
Поиск по индексу быстрее в списке
"""