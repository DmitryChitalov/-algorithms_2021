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
from random import randint
from timeit import timeit

def fill_list(nums):
    return [n for n in nums]

def fill_deque_right(nums):
    new_deque = deque()
    for item in nums:
        new_deque.append(item)
    return new_deque

def fill_deque_left(nums):
    new_deque = deque()
    for item in nums:
        new_deque.appendleft(item)
    return new_deque

def fill_deque(nums):
    return deque(nums)


"""
Заполнение дека происходит медленнее, чем самый быстрый вариант заполнения списка. Однако можно заполнить список и 
конвертировать его в дек - это самый быстрый способ заполнить дек, который мне удалось придумать.
Извлечение элементов справа в деке происходит быстрее, слева - сильно быстрее.
Вставка в рандомное место в списке происходит незначительно быстрее.
Дек точно стоит использовать, когда элементы извлекаются только с краев.

List:  0.258603
Deque append:  0.6345072
Deque append left:  0.6312735
Convert to deque:  0.07645610000000014
Извлечь слева из дека:  4.870000000001262e-05
Извлечь слева из списка:  0.0014690000000001646
Извлечь справа из дека:  5.5200000000033e-05
Извлечь справа из списка:  0.00014479999999994497
Вставка в дек:  0.005069400000000002
Вставка в список:  0.004730699999999866
"""

num_list = [randint(0, 100) for _ in range(100000)]
print('List: ', timeit("fill_list(num_list)", globals=globals(), number=1000))
print('Deque append: ', timeit("fill_deque_right(num_list)", globals=globals(), number=1000))
print('Deque append left: ', timeit("fill_deque_left(num_list)", globals=globals(), number=1000))
print('Convert to deque: ', timeit("fill_deque(num_list)", globals=globals(), number=1000))

test_list = fill_list(num_list)
test_deque = fill_deque(num_list)

print('Извлечь слева из дека: ', timeit("test_deque.popleft()", globals=globals(), number=10000))
print('Извлечь слева из списка: ', timeit("del(test_list[0])", globals=globals(), number=10000))
print('Извлечь справа из дека: ', timeit("test_deque.pop()", globals=globals(), number=10000))
print('Извлечь справа из списка: ', timeit("test_list.pop(len(test_list)-1)", globals=globals(), number=10000))
print('Вставка в дек: ', timeit("test_deque.insert(randint(0, 79999), randint(0, 100))", globals=globals(), number=10000))
print('Вставка в список: ', timeit("test_list.insert(randint(0, 79999), randint(0, 100))", globals=globals(), number=10000))
