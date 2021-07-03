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

numbers = [randint(0, 1000) for _ in range(10000)]
numbers_to_extend = [randint(0, 1000) for _ in range(100)]

lst = numbers.copy()
deq = deque(numbers)


def lst_insert_to_begin(data):
    for i in range(100):
        data.insert(0, i)
    return data


def deq_insert_to_begin(data):
    for i in range(100):
        data.appendleft(i)
    return data


"""
Операции вставки элементов в начало deque выполняются во много раз быстрее, 
так как имеют константную сложность в отличие от метода insert списов, 
имеющего линейную сложность
"""
print(f'Время вставки элементов в начало списка: {timeit("lst_insert_to_begin(lst)", globals=globals(), number=1000)}')
print(f'Время вставки элементов в начало deque: {timeit("deq_insert_to_begin(deq)", globals=globals(), number=1000)}')


def lst_insert_to_end(data):
    for i in range(100):
        data.append(i)
    return data


def deq_insert_to_end(data):
    for i in range(100):
        data.append(i)
    return data


"""
Операции вставки элементов в конец deque и списка выполняются примерно одинаково, 
так как обе имеют константную сложность
"""
print(f'Время вставки элементов в конец списка: {timeit("lst_insert_to_end(lst)", globals=globals(), number=1000)}')
print(f'Время вставки элементов в конец deque: {timeit("deq_insert_to_end(deq)", globals=globals(), number=1000)}')


def lst_pop_from_begin(data):
    for i in range(100):
        data.pop(0)
    return data


def deq_pop_from_begin(data):
    for i in range(100):
        data.popleft()
    return data


"""
Вывод, аналогичный вставке элементов в начало
"""
print(f'Время удаления элементов сначала списка: {timeit("lst_pop_from_begin(lst)", globals=globals(), number=1000)}')
print(f'Время удаления элементов сначала deque: {timeit("deq_pop_from_begin(deq)", globals=globals(), number=1000)}')


def lst_pop_from_end(data):
    for i in range(100):
        data.pop()
    return data


def deq_pop_from_end(data):
    for i in range(100):
        data.pop()
    return data


"""
Вывод, аналогичный вставке элементов в конец
"""
print(f'Время удаления элементов с конца списка: {timeit("lst_pop_from_end(lst)", globals=globals(), number=1000)}')
print(f'Время удаления элементов с конца deque: {timeit("deq_pop_from_end(deq)", globals=globals(), number=1000)}')


def lst_extend_to_end(data):
    data.extend(numbers_to_extend)


def deq_extend_to_end(data):
    data.extend(numbers_to_extend)


"""
Вывод, аналогичный вставке элементов в конец
"""
print(f'Время расширения списка: {timeit("lst_extend_to_end(lst)", globals=globals(), number=100000)}')
print(f'Время расширения deque: {timeit("deq_extend_to_end(deq)", globals=globals(), number=100000)}')
