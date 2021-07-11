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
import timeit
import collections
import random

def fill(in_seq, volume):
    """Заполнение"""
    for i in range(volume):
        in_seq.append(i*2)

def lst_append_left(in_lst,volume):
    """ Name is doc"""
    for i in range(volume):
        in_lst.insert(0,random.randint(0, volume))


def lst_pop_left(in_lst,volume):
    """Name is doc"""
    for i in range(volume):
        in_lst.pop(0)

def lst_extend_left(in_lst,volume):
    """Name is doc"""
    in_lst.insert(0,list(range(volume)).reverse())

def deck_append_left(in_deck,volume):
    """Name is doc"""
    for i in range(volume):
        in_deck.appendleft(random.randint(0, volume))

def deck_pop_left(in_deck,volume):
    """Name is doc"""
    for i in range(volume):
        deck.popleft()

def deck_extend_left(in_deck,volume):
    """Name is doc"""
    in_deck.extendleft(list(range(volume)))

def lst_random_insert(in_lst, volume):
    """Name is doc"""
    for i in range(volume):
        in_lst.insert(random.randint(0, len(in_lst)-1), 5)

def deck_random_insert(in_deck, volume):
    """Name is doc"""
    for i in range(volume):
        in_deck.insert(random.randint(0, len(in_deck)-1), 5)

VOLUME = 300
lst  = list()
deck = collections.deque()
print('Заполнение списка:')
print(timeit.timeit('fill(lst, VOLUME)',globals=globals(),number=VOLUME))
print('Заполнение дека')
print(timeit.timeit('fill(deck, VOLUME)',globals=globals(),number=VOLUME))
print("\nВремя выполнения appendleft:")
print(f'Список {timeit.timeit("lst_append_left(lst, VOLUME)",globals=globals(),number=VOLUME)}')
print(f'Дэк {timeit.timeit("deck_append_left(deck, VOLUME)",globals=globals(),number=VOLUME)}')
print("\nВремя выполнения popleft:")
print(f'Список {timeit.timeit("lst_pop_left(lst, VOLUME)",globals=globals(),number=VOLUME)}')
print(f'Дэк {timeit.timeit("deck_pop_left(deck, VOLUME)",globals=globals(),number=VOLUME)}')
print("\nВремя выполнения extendleft:")
print(f'Список {timeit.timeit("lst_extend_left(lst, VOLUME)",globals=globals(),number=VOLUME)}')
print(f'Дэк {timeit.timeit("deck_extend_left(deck, VOLUME)",globals=globals(),number=VOLUME)}')
print("\nВремя выполнения вставки по случайному индексу:")
print(f'Список {timeit.timeit("lst_random_insert(lst, VOLUME)",globals=globals(),number=VOLUME)}')
print(f'Дэк {timeit.timeit("deck_random_insert(deck, VOLUME)",globals=globals(),number=VOLUME)}')
"""
Заполнение списка:
0.007773099999999998
Заполнение дека
0.006345099999999999

Время выполнения appendleft:
Список 7.5529096000000004
Дэк 0.07794869999999943

Время выполнения popleft:
Список 9.581983800000001
Дэк 0.0045290999999991755

Время выполнения extendleft:
Список 0.01924619999999777
Дэк 0.0017592999999997971

Время выполнения вставки по случайному индексу:
Список 3.8046028000000014
Дэк 7.584230299999998
Анализируя результаты работы видим, что дэк выполняет операции вставки и удаления на концах значительно быстрее списка,
однако при вставке на случайную позицию список оказывается быстрее.
"""
