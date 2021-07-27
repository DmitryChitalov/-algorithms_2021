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

lst_obj = [5, 6, 7]
deq_obj = deque(lst_obj)


def load_lst():
    lst = [x for x in range(10000)]
    return lst


def load_deq():
    deq = [x for x in range(10000)]
    return deq


def lst_in():
    lst_obj.insert(0, 4)
    return lst_obj


def deq_al():
    deq_obj.appendleft(4)
    return deq_obj


def lst_pop():
    lst_obj.pop(0)
    return lst_obj


def deq_pop():
    deq_obj.popleft()
    return deq_obj


def lst_ext():
    a = [1, 2, 3]
    for i in range(len(a)):
        lst_obj.insert(0, a[i])
    return lst_obj


def deq_ext():
    deq_obj.extendleft([5, 6, 7])


print(f'Заполнение списка: {timeit("load_lst()", globals=globals(), number=1000)}')
print(f'Заполнение deque:  {timeit("load_deq()", globals=globals(), number=1000)}')
print(f'Insert : {timeit("lst_in()", globals=globals(), number=10000)}')
print(f'appenleft: {timeit("deq_al()", globals=globals(), number=10000)}')
print(f'pop : {timeit("lst_pop()", globals=globals(), number=10000)}')
print(f'Popleft : {timeit("deq_pop()", globals=globals(), number=10000)}')
print(f'extend в начало : {timeit("lst_ext()", globals=globals(), number=10000)}')
print(f'extendLeft : {timeit("deq_ext()", globals=globals(), number=10000)}')

# Заполнение списка: 0.6932834
# Заполнение deque:  0.6415878
# Insert : 0.07330870000000012
# appenleft: 0.0026441999999988752
# pop : 0.019091300000001254
# Popleft : 0.0025109000000007597
# extend в начало : 0.6010226999999997
# extendLeft : 0.005667100000000147

# Заполняется  deuqe быстрее но не намного в отличии от других методов
