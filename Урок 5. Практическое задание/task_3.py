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
temp_list = []
temp_deque = deque()

print('List fill ' + str(timeit('temp_list = [i for i in range(100)]', globals=globals())))
print('Deque fill ' + str(timeit('temp_deque = deque([i for i in range(100)])', globals=globals())))

print('List insert ' + str(timeit('temp_list.insert(-1, 555)', globals=globals())))
print('Deque appendleft ' + str(timeit('temp_deque.appendleft(555)', globals=globals())))

print('List get ' + str(timeit('temp_list[57]', globals=globals())))
print('Deque get ' + str(timeit('temp_deque[57]', globals=globals())))

'''
List fill 4.9978056
Deque fill 7.2062703
List insert 0.23152250000000052
Deque appendleft 0.19381920000000008
List get 0.1404569999999996
Deque get 0.17463979999999957

Дек заполняется и получает элемент по индексу медленее списка, но работает быстрее списка на вставку элемента. 
'''

