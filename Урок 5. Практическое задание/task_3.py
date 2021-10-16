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

some_list = [i for i in range(0, 10000)]
deq_obj = deque([i for i in range(0, 10000)])

print('Тесты заполнения')
print('Список')
print(timeit('some_list = [i for i in range(0, 10000)]', number=10000))
print('Deque')
print(timeit('deq_obj = deque([i for i in range(0, 10000)])', globals=globals(), number=10000))
# Тесты времени заполения показали, что deque заполняется незначительно медленнее списка
print('*' * 50)

print('Тесты вставки в начало для списка')
print(timeit('some_list.insert(0, 10000)', globals=globals(), number=10000))
print(timeit('some_list.pop(0)', globals=globals(), number=10000))
print(timeit('for i in range(100):'
             'some_list.insert(i, 0)', globals=globals(), number=1000))
print('*' * 50)

print('Тесты вставки в начало для deque')
print(timeit('deq_obj.appendleft(10000)', globals=globals(), number=10000))
print(timeit('deq_obj.popleft()', globals=globals(), number=10000))
print(timeit('deq_obj.extendleft(i for i in range(100))', globals=globals(), number=1000))
# А тесты с выполнением операций добавления значений в начало показали, что deque
# значительно быстрее чем список
print('*' * 50)

print('Тесты для списка')
print(timeit('some_list.extend(i for i in range(100))', globals=globals(), number=10000))
print(timeit('some_list.remove(50)', globals=globals(), number=100))
print('*' * 50)

print('Тесты для deque')
print(timeit('deq_obj.extend(i for i in range(100))', globals=globals(), number=10000))
print(timeit('deq_obj.remove(50)', globals=globals(), number=100))
print('*' * 50)
# Данные тесты показали, что добавление в конец списка занимает примерно одинаковое количество времени
# а remove выполняется значительно быстрее у deque
