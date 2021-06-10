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

my_list = list(range(10000))
my_deque = deque(range(10000))

print('Заполнение:')
print(f'Список: {timeit("my_list = list(range(10000))", globals=globals(), number=10000)}')  # 0.9166470999999999
print(f'Дек: {timeit("my_deque = deque(range(10000))", globals=globals(), number=10000)}')  # 1.346708

print('Добавление в конец:')
print(f'Список: {timeit("my_list.append(10)", globals=globals(), number=1000000)}')  # 0.05829989999999974
print(f'Дек: {timeit("my_deque.append(10)", globals=globals(), number=1000000)}')  # 0.05547879999999994

print('Добавление в начало:')
print(f'Список: {timeit("my_list.insert(0, 1)", globals=globals(), number=10000)}')  # 4.9819376
print(f'Дек: {timeit("my_deque.appendleft(1)", globals=globals(), number=10000)}')  # 0.00040429999999958

print('Удаление с конца:')
print(f'Список: {timeit("my_list.pop()", globals=globals(), number=1000000)}')  # 0.03648410000000002
print(f'Дек: {timeit("my_deque.pop()", globals=globals(), number=1000000)}')  # 0.03546469999999946

print('Удаление с начала:')
print(f'Список: {timeit("my_list.pop(0)", globals=globals(), number=10000)}')  # 0.01728129999999961
print(f'Дек: {timeit("my_deque.popleft()", globals=globals(), number=10000)}')  # 0.0003551000000001636

print('Поиск по индексу:')
print(f'Список: {timeit("my_list.index(9999)", globals=globals(), number=10000)}')  # 0.9049084000000001
print(f'Дек: {timeit("my_deque.index(9999)", globals=globals(), number=10000)}')  # 0.8580945

# Заполнение происходит быстрее в деке, список отстает почти на 40%
# Добавление в конец происходит практически с одинаковой скоростью
# Добавление в начало происходит в сотни раз бысрее в деке
# Удаление с конца происходит с одинаковой скоростью в списке и деке
# Удаление с начала происходит в десятки раз быстрее в деке
# Поиск по индексу практически идентичны в списке и деке
