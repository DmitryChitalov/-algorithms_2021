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


# Заполнение списка
def create_list():
    return [s for s in range(300)]


# Заполнение списка
def create_deq():
    return deque([s for s in range(300)])


# Вставка слева список
def insert_list(temp):
    for s in range(100):
        temp.insert(0, s)
    return temp


# Вставка слева дек
def deq_append_left(temp):
    for s in range(100):
        temp.appendleft(s)
    return temp


# Заполнение справа список
def append_list(temp):
    for s in range(300):
        temp.append(s)
    return temp


# Заполнение справа дек
def deq_append_right(temp):
    for s in range(300):
        temp.append(s)
    return temp


# Удаление слева в списке
def list_pop(temp):
    temp.pop(0)
    return temp


# Удаление слева в деке
def deq_pop_left(temp):
    temp.popleft()
    return temp


# Это скорее костыль, т.к. такого метода в списке нет, Extend вставляет в конец списка
def list_extend(temp):
    temp.reverse()
    temp.extend([4, "890", 678, False])
    temp.reverse()
    return temp


def deq_extend_left(temp):
    temp.extendleft([4, "890", 678, False])
    return temp


my_list = create_list()
my_deq = create_deq()

print("create_list()", timeit("create_list()", globals=globals(), number=10000))
print("create_deq()", timeit("create_deq()", globals=globals(), number=10000))
print('*' * 10)

print("insert_list()", timeit("insert_list(my_list)", globals=globals(), number=1000))
print("deq_append_left()", timeit("deq_append_left(my_deq)", globals=globals(), number=1000))
print('*' * 10)

print("append_list()", timeit("append_list(my_list)", globals=globals(), number=10000))
print("deq_append_right()", timeit("deq_append_right(my_deq)", globals=globals(), number=10000))
print('*' * 10)

print("list_pop()", timeit("list_pop(my_list)", globals=globals(), number=4000))
print("deq_pop_left()", timeit("deq_pop_left(my_deq)", globals=globals(), number=4000))
print('*' * 10)

print("list_extend()", timeit("list_extend(my_list)", globals=globals(), number=4000))
print("deq_extend_left()", timeit("deq_extend_left(my_deq)", globals=globals(), number=4000))

"""
Реультаты :

create_list() 0.05830199999999999
create_deq() 0.06989710000000002
**********
insert_list() 2.2973895
deq_append_left() 0.0036649999999998073
**********
append_list() 0.14401960000000003
deq_append_right() 0.11748639999999977
**********
list_pop() 6.3352548
deq_pop_left() 0.0003220000000005996
**********
list_extend() 13.126561
deq_extend_left() 0.0006048000000014042

Беру свои слова обратно насчёт дек. Проблема была в маленьких обьёмах, передаваемых
в фукции. Единственное где список выигрывает это при создании с помощью LH и близко
при append, во всем остальном разница колоссальна. 
"""



