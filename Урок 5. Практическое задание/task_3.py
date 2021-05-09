"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

Задача:
1) создайте простой список (list) и очередь (deque).
Сделайте замеры и оцените что заполняется быстрее.
2) Выполните различные операции с каждым из объектов.
 Сделайте замеры и оцените, где и какие операции быстрее.

Не забудьте, что сравнивать, например, можно операцию appendleft дека и insert списка и т.д.
"""

from timeit import timeit
from collections import deque

test_deque = deque()
test_list = []


# добавление элементов в конец
def fill_list(elem_count):
    for _ in range(elem_count):
        test_list.append(None)


def right_fill_deque(elem_count):
    for _ in range(elem_count):
        test_deque.append(None)


print(f'Добавление элементов (list) '
      f'{timeit("fill_list(100000)", globals=globals(), number=1)}')
print(f'Добавление элементов (deque) '
      f'{timeit("right_fill_deque(100000)", globals=globals(), number=1)}')
"""
Добавление элементов (list) 0.006255299999999998
Добавление элементов (deque) 0.006034699999999997
"""


# добавление элементов в начало
def insert_into_list(elem_count):
    for _ in range(elem_count):
        test_list.insert(0, None)


def left_fill_deque(elem_count):
    for _ in range(elem_count):
        test_deque.appendleft(None)


print(f'Добавление элементов в начало (list) '
      f'{timeit("insert_into_list(100000)", globals=globals(), number=1)}')
print(f'Добавление элементов в начало (deque) '
      f'{timeit("left_fill_deque(100000)", globals=globals(), number=1)}')
"""
Добавление элементов в начало (list) 7.3290258
Добавление элементов в начало (deque) 0.007556300000000071
"""


# Вставка в середину
def insert_into_list_mid():
    i = len(test_list) // 2
    test_list.insert(i, None)


def insert_into_deque():
    i = len(test_deque) // 2
    test_deque.insert(i, None)


print(f'Вставка в середину (list) '
      f'{timeit("insert_into_list_mid()", globals=globals(), number=1000)}')
print(f'Вставка в середину (deque) '
      f'{timeit("insert_into_deque()", globals=globals(), number=1000)}')
"""
Вставка в середину (list) 0.050168099999999605
Вставка в середину (deque) 0.18394140000000014
"""


# получение элемента по индексу
def get_list_elem():
    for i in range(len(test_list)):
        test_list[i]


def get_deque_elem():
    for i in range(len(test_deque)):
        test_deque[i]


print(f'Получение элемента по индексу (list) '
      f'{timeit("get_list_elem()", globals=globals(), number=1)}')
print(f'Получение элемента по индексу (deque) '
      f'{timeit("get_deque_elem()", globals=globals(), number=1)}')
"""
Получение элемента по индексу (list) 0.007712299999999672
Получение элемента по индексу (deque) 0.6783413999999999
"""


# Реверс
print(f'Реверс (list) {timeit("test_list.reverse()", globals=globals(), number=1)}')
print(f'Реверс (deque) {timeit("test_deque.reverse()", globals=globals(), number=1)}')
"""
Реверс (list) 0.00011410000000111609
Реверс (deque) 0.0003643999999987102
"""

# Копирование
print(f'Копирование (list) {timeit("test_list.copy()", globals=globals(), number=1)}')
print(f'Копирование (deque) {timeit("test_deque.copy()", globals=globals(), number=1)}')
"""
Копирование (list) 0.0012761000000001133
Копирование (deque) 0.0032668999999998505
"""


# удаление элементов c начала
def pop_from_list_begin(elem_count):
    for _ in range(elem_count):
        test_list.pop(0)


def pop_from_deque_left(elem_count):
    for _ in range(elem_count):
        test_deque.popleft()


print(f'Удаление элементов c начала (list) '
      f'{timeit("pop_from_list_begin(100000)", globals=globals(), number=1)}')
print(f'Удаление элементов c начала (deque) '
      f'{timeit("pop_from_deque_left(100000)", globals=globals(), number=1)}')
"""
Удаление элементов c начала (list) 11.3628583
Удаление элементов c начала (deque) 0.006510699999999758
"""


# удаление элементов c конца
def pop_from_list_end(elem_count):
    for _ in range(elem_count):
        test_list.pop()


def pop_from_deque_right(elem_count):
    for _ in range(elem_count):
        test_deque.pop()


print(f'Удаление элементов c конца (list) '
      f'{timeit("pop_from_list_end(100000)", globals=globals(), number=1)}')
print(f'Удаление элементов c конца (deque) '
      f'{timeit("pop_from_deque_right(100000)", globals=globals(), number=1)}')
"""
Удаление элементов c конца (list) 0.005286800000000369
Удаление элементов c конца (deque) 0.0051538999999998225
"""


# Удаление
def del_from_list():
    i = len(test_list) // 2
    del test_list[i]


def del_from_deque():
    i = len(test_deque) // 2
    del test_deque[i]


print(f'Удаление из середины (list) '
      f'{timeit("del_from_list()", globals=globals(), number=1000)}')
print(f'Удаление из середины (deque) '
      f'{timeit("del_from_deque()", globals=globals(), number=1000)}')
"""
Удаление из середины (list) 0.00031570000000158416
Удаление из середины (deque) 0.0007816999999974428
"""

"""
При добавлении элементов в конец или извлечении элементов с конца
список и дек работают примерно одинаково.
При обращении к середине массива (доступ по индексу, вставка в
середину, удаление из середины) списки работают несколько быстрее.
Копирование и реверс элементов также быстрее для списка.
Однако при работе с началом списка (добавление/удаление элементов)
у дека значительное преимущество по времени выполнения.
Таким образом можно подтвердить справедливость высказывания
"если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list."
"""
