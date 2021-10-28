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
from random import randint
import random
from timeit import timeit



test_list = []

x_list = [3, 643, 43, 432]
a = [1,2,3]

for i in range(500):
    test_list.append(randint(1, 500))

z_list = x_list

test_deque = deque(range(500))
random.sample(test_deque, 500)




print(test_list)
print(test_deque)

print(f"Время выполнения вставки элементов в начало list: "
      f"{timeit(stmt='test_list.insert(randint(1, 1000), 0)', globals=globals(), number=100000)}")
print(f"Время выполнения вставки элементов в начало deque:"
      f" {timeit(stmt='test_deque.appendleft(randint(1, 1000))', globals=globals(), number=100000)}")

print(test_list)
print(test_deque)

""" deque гораздо лучше справился со вставкой элемента в начало, чем list, в связи с тем, что функция вставки значений у 
deque имеет O(1) -  константную сложность, а у list O(1) - линейную.
Время выполнения заметно различается в пользу deque
"""

print(f'Время выполнения удаления элемента из list: '
      f'{timeit(stmt="test_list.pop(0)", globals=globals(), number=10000)}')
print(f'Время выполнения удаления элемента из deque: '
      f'{timeit(stmt="test_deque.pop()", globals=globals(), number=10000)}')

"""
Удаление элемента так же проходит значительно быстрее в случае с deque, связанно так же с константной сложностью против линейной
"""

print(f'Добавление списка элементов в начало list: '
      f'{timeit(stmt="for i in range(len(a)): test_list.insert(0, a[i])", globals=globals(), number=10000)}')
print(f'Добавление списка элементов в начало deque: '
      f'{timeit(stmt="test_deque.extendleft(a)", globals=globals(), number=10000)}')

"""
Расширение слева так же в случае с deque так же происходит гораздо быстрее, в связи с константной сложностью, 
и наличием встроенного метода. 
"""


print(test_list)
print(test_deque)