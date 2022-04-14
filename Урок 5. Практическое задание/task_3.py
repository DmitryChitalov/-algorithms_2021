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

simple_lst = []
deq_obj = deque()


def append_to_list(n, lst):
    for i in range(n):
        lst.insert(0, i)
    return lst


def append_to_deque(n, deq):
    for i in range(n):
        deq.appendleft(i)
    return deq


print(append_to_list(10, simple_lst))
print(append_to_deque(10, deq_obj))


def pop_from_list(lst):  # удалить первый элемент слева
    lst.pop(0)
    return lst


def pop_from_deque(deq):
    deq.popleft()
    return deq


def extend_list(elements, lst):  # добавляем элементы в левую часть списка
    for i in range(len(elements)):
        lst.insert(0, i)
    return lst


def extend_deque(elements, deq):
    deq_obj.extendleft(elements)
    return deq


print(pop_from_list(simple_lst))
print(pop_from_deque(deq_obj))
print(extend_list([1, 2, 3], simple_lst))
print(extend_deque([4, 5, 6], deq_obj))

print(f'Время выполнения append_to_list: {timeit("append_to_list(10, simple_lst)", globals=globals(), number=1000)}')
print(f'Время выполнения append_to_deque: {timeit("append_to_deque(10, deq_obj)", globals=globals(), number=1000)}')
print(f'Время выполнения pop_from_list: {timeit("pop_from_list(simple_lst)", globals=globals(), number=1000)}')
print(f'Время выполнения pop_from_deque: {timeit("pop_from_deque(deq_obj)", globals=globals(), number=1000)}')
print(f'Время выполнения extend_list: {timeit("extend_list([1, 2, 3], simple_lst)", globals=globals(), number=1000)}')
print(f'Время выполнения extend_deque: {timeit("extend_deque([4, 5, 6], deq_obj)", globals=globals(), number=1000)}')

'''
Время выполнения append_to_list: 0.048472296
Время выполнения append_to_deque: 0.001128065999999997
Время выполнения pop_from_list: 0.006660728000000005
Время выполнения pop_from_deque: 0.0001624250000000077
Время выполнения extend_list: 0.019464515
Время выполнения extend_deque: 0.00022219299999999553
Вывод:
В операциях с началом списка deque выигрывает по скорости у списка, так как изначально заточен под такие операции и их
сложность для очереди составляет O(1), тогда как у списка операции insert и pop имеют сложность 0(n):
1) например, сложность вставки в начало списка составляет O(n), тогда как у очереди это O(1), следовательно, вставка 
происходит быстрее у очереди;
2) в операции удаления элемента из начала также выигрывает очередь;
3) операция вставки нескольких элментов в начало также оказалась быстрее у очереди.
списка.
'''
