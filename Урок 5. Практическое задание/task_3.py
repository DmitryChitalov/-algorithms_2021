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


def extend_list_in_left(lst, extend_list):     # extend добавляет в конец списка, потому не подходит
    for i in extend_list:
        lst.insert(0, i)


list_for_extend = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]    # список для расширения
print('Создание списков:')
print('list: ', timeit('my_list = [i for i in range(100)]', globals=globals()))
print('deque: ', timeit('my_deque = deque([i for i in range(100)])',
                        globals=globals()))
# Для операций со списками их необходимо создать
my_list = [i for i in range(10)]
my_deque = deque([i for i in range(10)])
print('Добавление в начало (по одному)')
print('list:', timeit('my_list.insert(0, 0)', globals=globals(), number=10000))
print('deque:', timeit('my_deque.appendleft(0)', globals=globals(), number=10000))
print('Добавление в конец (по одному)')
print('list:', timeit('my_list.append(0)', globals=globals(), number=10000))
print('deque:', timeit('my_deque.append(0)', globals=globals(), number=10000))
print('Удаление первого элемента:')
print('list:', timeit('my_list.pop(0)', globals=globals(), number=9000))
print('deque:', timeit('my_deque.popleft()', globals=globals(), number=9000))
print('Добавление списка в начало')
# возможно не самый правильный вариант, но иных путей добавить список в начало не нашел
print('list:', timeit('extend_list_in_left(my_list, list_for_extend)', globals=globals(), number=10000))
print('deque:', timeit('my_deque.extendleft(list_for_extend)', globals=globals(), number=10000))
print('Изменение элемента с индексом 0')
print('list:', timeit('my_list[0] += 1', globals=globals()))
print('deque:', timeit('my_deque[0] += 1', globals=globals()))
print('Изменение элемента с индексом 50000')
print('list:', timeit('my_list[50000] += 1', globals=globals()))
print('deque:', timeit('my_deque[50000] += 1', globals=globals()))
print('Изменение элемента с индексом 99999')
print('list:', timeit('my_list[99999] += 1', globals=globals()))
print('deque:', timeit('my_deque[99999] += 1', globals=globals()))

"""
Создание списков:
list:  2.5579959000000003
deque:  3.3707374000000003
Добавление в начало (по одному)
list: 0.022265700000000166
deque: 0.0004639000000006277
Добавление в конец (по одному)
list: 0.0005326999999999416
deque: 0.0005188000000000415
Удаление первого элемента:
list: 0.03207990000000027
deque: 0.000362900000000721
Добавление списка в начало
list: 2.6039632999999993
deque: 0.0017332999999997156
Изменение элемента с индексом 0
list: 0.07196839999999938
deque: 0.11998419999999932
Изменение элемента с индексом 50000
list: 0.07139090000000081
deque: 8.4512518
Изменение элемента с индексом 99999
list: 0.07159970000000015
deque: 0.8054270999999993

deque лучше в добавлении в начало (по одному или списком) и удалении из начала.
Если нужно обращаться по индексам, то лучше list, при этом разница при обращении к индексам из середины deque 
значительно медленнее (в моем случае разница более чем в 100 раз).
"""
