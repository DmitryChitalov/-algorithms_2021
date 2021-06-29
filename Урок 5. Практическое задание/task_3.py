"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list .

Задача: 
1) создайте простой список (list ) и очередь (deque). Сделайте замеры и оцените что заполняется быстрее.
2) Выполните различные операции с каждым из объектов. Сделайте замеры и оцените, где и какие операции быстрее.

В первую очередь необходимо выполнить замеры для ф-ций appendleft, popleft, extendleft дека и для их аналогов у списков.
"""
from collections import deque
import timeit


# 1)
def sample_list():
    return [x**2 for x in range(999)]


def sample_deque():
    return deque([x**2 for x in range(999)])


print('# создание')
print('list ', timeit.timeit("sample_list ()", globals=globals(), number=1000))
print('deque', timeit.timeit("sample_deque()", globals=globals(), number=1000))
print('-' * 10)
lst = sample_list()
dqe = sample_deque()

# 2)
print('# получение элемента')
print('list ', timeit.timeit("lst[100]", globals=globals(), number=100000))
print('deque', timeit.timeit("dqe[100]", globals=globals(), number=100000))
print('-' * 10)
#
print('# добавление элемента слева')
print('list ', timeit.timeit("lst.insert(0, -1)", globals=globals(), number=10000))
print('deque', timeit.timeit("dqe.appendleft(-1)", globals=globals(), number=10000))
print('-' * 10)
#
print('# удаление элемента слева')
print('list ', timeit.timeit("lst.remove(-1)", globals=globals(), number=10000))
print('deque', timeit.timeit("dqe.popleft()", globals=globals(), number=10000))
print('-' * 10)
#
print('# добавление списка элементов в начало')
print('list ', timeit.timeit("[1, 2, 3, 4, 5, 6, 7, 8, 9, 0] + lst", globals=globals(), number=10000))
print('deque', timeit.timeit("dqe.extendleft([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])", globals=globals(), number=10000))
print('-' * 10)
'''
# создание
list  0.21427543300000002
deque 0.220321309
Одинаковое время выполнения
----------
# получение элемента
list  0.0027878439999999838
deque 0.003211383000000012
Получение элемента чуть быстрее в list
----------
# добавление элемента слева
list  0.02161866200000001
deque 0.0004630760000000067
Добавление элемента в начало гораздо быстрее в deque
----------
# удаление элемента слева
list  0.007810856000000033
deque 0.00036579700000000104
Удаление элемента из начала гораздо быстрее в deque
----------
# добавление списка элементов в начало
list  0.01917300500000002
deque 0.0019020830000000544
Добавлене списка элементов в начало гораздо быстрее в deque
'''