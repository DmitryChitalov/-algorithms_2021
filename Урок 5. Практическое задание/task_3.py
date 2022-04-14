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


from timeit import timeit
from collections import deque

my_list = []
my_deque = deque()


def lst_app(my_lst):
    for i in range(50000):
        my_lst.append(i)
    return my_lst


def deque_app(my_dqe):
    for i in range(50000):
        my_dqe.append(i)
    return my_dqe


# В заполнении использование дек даёт преимущество по скорости


def lst_app_left(my_lst):
    for i in range(500):
        my_lst.insert(0, i)
    return my_lst


def deque_app_left(my_dqe):
    for i in range(500):
        my_dqe.appendleft(i)
    return my_dqe


# Здесь deque отрабатывает в разы быстрее


def lst_pop(my_lst):
    for i in range(10):
        my_lst.pop(0)
    return my_lst


def deque_pop(my_dqe):
    for i in range(10):
        my_dqe.popleft()
    return my_dqe


# Операция с deque, где мы достаём элементы слева, выполняется в разы быстрее, чем с list, так как дек и создан для работы с элементами с любой стороны списка


def lst_del(my_lst):
    for i in range(100):
        del my_lst[i]
    return my_lst


def deque_del(my_dqe):
    for i in range(100):
        del my_dqe[i]
    return my_dqe
# Взятие элементов по индексу в deque также обходится значительно быстрее, чем в list

def lst_clear(my_lst):
    return my_lst.clear()


def deque_clear(my_dqe):
    return my_dqe.clear()


# В случае с clear deque проигрывает
# Можно сделать вывод, что deque имеет огромное преимущество по времени, если надо работать с элементами не с конца списка

# append
# 0.23926380000000003
# 0.1971546
# append_left
# 1.9503151
# 3.15000000004062e-05         ---- Пришлось оставить такой вывод, иначе операции с list пришлось бы ждать очень долго
# pop_left
# 3.3838194
# 5.2400000000396574e-05
# del
# 33.7516677
# 0.0011596000000011486
# clear
# 0.03393739999999923
# 0.03848590000000485
# 


print('append')
print(timeit(
    'lst_app(my_list)',
    globals=globals(),
    number=100
))
print(timeit(
    'deque_app(my_deque)',
    globals=globals(),
    number=100
))


print('append_left')
print(timeit(
    'lst_app_left(my_list)',
    globals=globals(),
    number=1
))
print(timeit(
    'deque_app_left(my_deque)',
    globals=globals(),
    number=1
))

print('pop_left')
print(timeit(
    'lst_pop(my_list)',
    globals=globals(),
    number=100
))
print(timeit(
    'deque_pop(my_deque)',
    globals=globals(),
    number=100
))

print('del')
print(timeit(
    'lst_del(my_list)',
    globals=globals(),
    number=100
))
print(timeit(
    'deque_del(my_deque)',
    globals=globals(),
    number=100
))

print('clear')
print(timeit(
    'lst_clear(my_list)',
    globals=globals(),
    number=100
))
print(timeit(
    'deque_clear(my_deque)',
    globals=globals(),
    number=100
))
