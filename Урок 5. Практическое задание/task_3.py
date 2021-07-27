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
from random import randint
from timeit import timeit

my_list = []

for i in range(150):
    my_list.append(randint(1, 1000))

my_deque = deque(my_list)

print(f"Время выполнения вставки элементов в начало list: "
      f"{timeit('my_list.insert(randint(1, 1000), 0)', globals=globals(), number=10000)}")
print(f"Время выполнения вставки элементов в начало deque:"
      f" {timeit('my_deque.appendleft(randint(1, 1000))', globals=globals(), number=10000)}")

# Определённо deque лучше справился с задачей вставки элемента в начало чем list.
# Это обусловленно тем, что функция вставки значений у deque имеет константную сложность,
# в то время как у list - линейную; из-за этого deque и получает достаточно приличный выйгрыш во времени.
#
# Время выполнения вставки элементов в начало list: 0.0377044
# Время выполнения вставки элементов в начало deque: 0.007005600000000001

print(f'Время выполнения доставания случайного элемента из list: '
      f'{timeit("my_list[randint(1, 1000)]", globals=globals(), number=10000000)}')
print(f'Время выполнения доставания случайного элемента из deque: '
      f'{timeit("my_deque[randint(1, 1000)]", globals=globals(), number=10000000)}')

# С задачей "Достать случайный элемент" list справился не на много, но всё же лучше deque.
# Время выполнения доставания случайного элемента из list: 6.549188
# Время выполнения доставания случайного элемента из deque: 6.819932

print(f'Время выполнения удаления элемента из list: '
      f'{timeit("my_list.pop(0)", globals=globals(), number=10000)}')
print(f'Время выполнения удаления элемента из deque: '
      f'{timeit("my_deque.pop()", globals=globals(), number=10000)}')

# Удаление элемента из начала списка. Здесь как и в случае добавления элемента в начало deque справился  
# в разы лучше list, что опять же обусловоенно константной сложностью.
# Время выполнения удаления элемента из list: 0.008509699999999398
# Время выполнения удаления элемента из deque: 0.00045010000000011985

# Из всего перечисленногоможно сделать вывод, что информация в документации достаточно достоверна.
