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


lst_obj = list(range(10))
deq_obj = deque(lst_obj)

lst_obj.append(10)
deq_obj.append(10)

lst_obj.insert(0, 55)
deq_obj.appendleft(55)

lst_obj.pop()
deq_obj.pop()

lst_obj.pop(0)
deq_obj.popleft()

print(f"Добавление в конец list = {timeit('lst_obj.append(10)', globals=globals(), number=100000)}")
print(f"Добавление в конец deque = {timeit('deq_obj.append(10)', globals=globals(), number=100000)}")

print(f"Добавление в начало list = {timeit('lst_obj.insert(0, 55)', globals=globals(), number=100000)}")
print(f"Добавление в начало deque = {timeit('deq_obj.appendleft(55)', globals=globals(), number=100000)}")

print(f"Удалить последний эл-т list = {timeit('lst_obj.pop()', globals=globals(), number=100000)}")
print(f"Удалить последний эл-т deque = {timeit('deq_obj.pop()', globals=globals(), number=100000)}")

print(f"Удалить первый эл-т list = {timeit('lst_obj.pop(0)', globals=globals(), number=100000)}")
print(f"Удалить первый эл-т deque = {timeit('deq_obj.popleft()', globals=globals(), number=100000)}")

'''
Добавление в конец list = 0.026078616000000006
Добавление в конец deque = 0.024904678
Добавление в начало list = 18.664222191
Добавление в начало deque = 0.024516783999999348
Удалить последний эл-т list = 0.02257090599999856
Удалить последний эл-т deque = 0.02295110600000072
Удалить первый эл-т list = 3.8998901720000028
Удалить первый эл-т deque = 0.023004962000001683
'''