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
from timeit import timeit

insert_list = [el for el in range(0, 10)]
simple_list = [el for el in range(0, 20)]
dq = deque(el for el in range(0, 20))

print('Добавление элемента в начало списка')
print(timeit('simple_list.insert(0, insert_list)', globals=globals(), number=10000))
print(timeit('dq.appendleft(insert_list)', globals=globals(), number=10000))
print('-' * 100)

print('Извлечение 1го элемента списка')
print(timeit('simple_list[0:0] = insert_list', globals=globals(), number=10000))
print(timeit('dq.popleft()', globals=globals(), number=10000))
print('-' * 100)

print('Групповое добавление элементов в начало списка')
print(timeit('simple_list.extend(insert_list)', globals=globals(), number=10000))
print(timeit('dq.extendleft(insert_list)', globals=globals(), number=10000))
print('-' * 100)


"""
Добавление элемента в начало списка
0.0380903
0.0006568000000000129

Извлечение 1го элемента списка
0.1716352
0.0005058999999999758

Групповое добавление элементов в начало списка
0.0026621000000000006
0.001984100000000044

Исходя из полученных результатов видно, что стандартный список хуже работает с 
операциями связанных с добавлением и извлечение в начало списка 
"""