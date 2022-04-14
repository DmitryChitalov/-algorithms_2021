"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.
Задача: 
1) создайте простой список (list) и очередь (deque). Сделайте замеры и оцените что заполняется быстрее.
2) Выполните различные операции с каждым из объектов. Сделайте замеры и оцените, где и какие операции быстрее.
Не забудьте, что сравнивать, например, можно операцию appendleft дека и insert списка и т.д.
"""

from collections import deque
from timeit import timeit


random_int = int(input('Введите целое число - границу списка целых чисел: '))

def gen_list(range_int):
    a_list = [i for i in range(1,range_int)]
    return a_list

def gen_deque(range_int):
    a_deque = deque([i for i in range(1, range_int)])
    return a_deque

ran_list = gen_list(random_int)


print(
    'генерация списка: ',
    timeit(
        f'gen_list({random_int})',
        globals=globals(),
        number=10000))

ran_deque = gen_deque(random_int);


print(
    'генерация очереди: ',
    timeit(
        f'gen_deque({random_int})',
        globals=globals(),
        number=10000))

new_range = random_int * 3

def add_list(some_list, range_int, some_range):
    for i in range(range_int + 1, some_range):
        some_list.insert(0, i)
        return some_list

def add_deque(some_deque, range_int, some_range):
    for i in range(range_int + 1, some_range):
        some_deque.appendleft(i)
        return some_deque

ran_list = add_list(ran_list, random_int, new_range)
ran_deque = add_deque(ran_deque, random_int, new_range)

print(
    'добавление списка: ',
    timeit(
        f'add_list({ran_list}, {random_int}, {new_range})',
        globals=globals(),
        number=10000))

print(
    'добавление очереди: ',
    timeit(
        f'add_deque({ran_deque}, {random_int}, {new_range})',
        globals=globals(),
        number=10000))


"""
результаты:
Введите целое число - границу списка целых чисел: 1301
генерация списка:  0.4843666999999998
генерация очереди:  0.5606992000000002
добавление списка:  0.05019680000000015
добавление очереди:  0.12614490000000078

генерация и добавление в очереди проходят дольше, чем в списке на низких значениях


Введите целое число - границу списка целых чисел: 10000
генерация списка:  2.8592839999999997
генерация очереди:  3.952096599999999
добавление списка:  0.47964379999999984
добавление очереди:  1.2727944000000004



