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

array = [i for i in range(1000)]
deq_obj = deque(array)

def add_list():
    return [i for i in range(1000)]

def add_deque():
    return deque(range(1000))

print(f'{timeit("add_list()", globals=globals(), number=10000)} - создание list',
f'{timeit("add_deque()", globals=globals(), number=10000)} - создание deque', sep='\n')

def standart_append(arr):
    return arr.insert(0, 100)

def deque_append(deq):
    deq.appendleft(100)
    return deq_obj

print(f'{timeit("standart_append(array)", globals=globals(), number=10000)} - list append',
f'{timeit("deque_append(deq_obj)", globals=globals(), number=10000)} - deque append', sep='\n')

def standart_pop(arr):
    return arr.pop(0)

def deque_pop(deq):
    return deq.popleft()

print(f'{timeit("standart_pop(array)", globals=globals(), number=10000)} - list pop',
f'{timeit("deque_pop(deq_obj)", globals=globals(), number=10000)} - deque pop', sep='\n')

def standart_extend(arr):
    for i in reversed([1, 0, 0]):
        arr.insert(0, i)
    return arr

def deq_extend(deq):
    deq.extendleft(reversed([1, 0, 0]))
    return deq

print(f'{timeit("standart_extend(array)", globals=globals(), number=10000)} - list extend',
f'{timeit("deq_extend(deq_obj)", globals=globals(), number=10000)} - deque extend', sep='\n')

"""
Создание deque и операции с deque гораздо быстрее создания списка стандартных операций с ним.
Подозреваю, что deque работает на основе генератора и большая скорость за счёт того, 
что операции проводятся с началом списка.
"""