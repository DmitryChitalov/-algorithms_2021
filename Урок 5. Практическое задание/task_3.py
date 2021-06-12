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
from random import randint

list_obj = []
deque_obj = deque()


def full_list(list_ob):
    for i in range(1000):
        list_ob.append(i)


def full_dec(dec_ob):
    for i in range(1000):
        dec_ob.append(i)


def left_dec(dec_ob):
    for i in range(1000):
        dec_ob.appendleft(i * 2)


def left_list(list_ob):
    for i in range(1000):
        list_ob.insert(0, i * 2)


def rand_list(list_ob, n=1000):
    for _ in range(n):
        num = randint(0, 1999)
        list_ob[num] = list_ob[num] * 3 + 25


def rand_dec(dec_ob, n=1000):
    for _ in range(n):
        num = randint(0, 1999)
        dec_ob[num] = dec_ob[num] * 3 + 25


full_list(list_obj)
full_dec(deque_obj)
left_list(list_obj)
left_dec(deque_obj)
rand_list(list_obj)
rand_dec(deque_obj)
print(f'{list_obj}\n{deque_obj}')

print(f'Время заполнения списка: {timeit("full_list(list_obj)", globals=globals(), number=1000)}')
print(f'Время заполнения дэка: {timeit("full_dec(deque_obj)", globals=globals(), number=1000)}')
print(f'Время заполнения в начало списка: {timeit("left_list(list_obj)", globals=globals(), number=100)}')
print(f'Время заполнения в начало дэка: {timeit("left_dec(deque_obj)", globals=globals(), number=100)}')
print(f'Время изменения элементов списка: {timeit("rand_list(list_obj)", globals=globals(), number=1000)}')
print(f'Время изменения элементов дэка: {timeit("rand_dec(deque_obj)", globals=globals(), number=1000)}')

'''
Время заполнения списка: 0.1103283
Время заполнения дэка: 0.08749869999999998
Время заполнения в начало списка: 91.3605223
Время заполнения в начало дэка: 0.01157380000000785
Время изменения элементов списка: 1.4507932000000068
Время изменения элементов дэка: 1.5255997000000008

Исходя из измерений можно утверждать, что когда необходимо заполнять список, добавляя новый элемнет в начало списка,
а не в конец, то Deque работает в разы быстрее чем обычный список. (Для того чтобы провести измерения для операций
вставки в начало кол-во запусков функции было сокращено с 1000 до 100)

В остальных случаях список и дэк работают практически одинаково. При заполнении значений дэк работает быстрее. 
При получении случайного элемента быстрее работает список.
'''
