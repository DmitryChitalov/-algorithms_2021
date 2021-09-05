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
from random import randint
from collections import deque
from timeit import timeit


def create_list(num):
    """Создание и зполнение списка"""
    return [randint(0, 100000) for _ in range(num)]


def insert(lst, arg):
    """Вставка элемента в начало списка"""
    lst.insert(0, arg)


def pop_zero(lst):
    """Удаление первого элемента списка"""
    lst.pop(0)


def insert_list_to_begin(lst_1, lst_2):
    """Вставка списка в начало существующего"""
    for i in reversed(lst_2):
        lst_1.insert(0, i)


def create_deque(num):
    """Создание и заполнение дека"""
    return deque(randint(0, 100000) for _ in range(num))


def append_lft(deq, arg):
    """Добавление элемента слева"""
    deq.appendleft(arg)


def pop_lft(deq):
    """Удаление элемента слева"""
    deq.popleft()


def extend_lft(deq, lst):
    """Добавление элементов слева"""
    deq.extendleft(reversed(lst))


#  Создание списка и дека с 1000 целых чисел
print('Создание списка и дека с 1000 целых чисел')
print('Создание списка:', timeit('create_list(1000)', globals=globals(), number=10000), 'сек')
print('Создание дека:', timeit('create_deque(1000)', globals=globals(), number=10000), 'сек')
# Создание списка: 8.93504378399939 сек
# Создание дека: 8.846965398000066 сек

my_list = create_list(1000)
my_deque = create_deque(1000)

# appendleft VS insert
print('\nappendleft VS insert')
print('insert:', timeit('insert(my_list, 1)', globals=globals(), number=100000), 'сек')
print('appendleft:', timeit('append_lft(my_deque, 1)', globals=globals(), number=100000), 'сек')
# insert: 3.2477192710011877 сек
# appendleft: 0.013542038999730721 сек

# popleft VS pop([i])
print('\npopleft VS pop([i])')
print('pop([i]):', timeit('pop_zero(my_list)', globals=globals(), number=100000), 'сек')
print('popleft:', timeit('pop_lft(my_deque)', globals=globals(), number=100000), 'сек')
# pop([i]): 2.1101269249993493 сек
# popleft: 0.011096619999079849 сек

# extendleft VS insert
print('\nextendleft VS insert')
print('insert:', timeit(
    'insert_list_to_begin(my_list, [1, 2, 3])',
    globals=globals(),
    number=100000), 'сек')
print('extendleft:', timeit(
    'extend_lft(my_deque, [1, 2, 3])',
    globals=globals(),
    number=100000), 'сек')
# insert: 30.583021852000456 сек
# extendleft: 0.03376167100032035 сек
