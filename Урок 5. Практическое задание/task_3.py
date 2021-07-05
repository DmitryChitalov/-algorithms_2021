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

create_deque = deque([x for x in range(100)])
create_list = [x for x in range(100)]

print(f'Пункт 1')
print(f'Создание очереди: ', timeit(f'create_list', globals=globals(), number=10000000))
print(f'Создание простого списка: ', timeit(f'create_deque', globals=globals(), number=10000000))

print(f'Пункт 2')
print(f'Использование insert в списке: ', timeit(f'create_list.insert(0,1)', globals=globals(), number=100000))
print(f'Использование append в очереди: ', timeit(f'create_deque.append(1)', globals=globals(), number=100000))
print(f'Использование appendleft в очереди: ', timeit(f'create_deque.appendleft(1)', globals=globals(), number=100000))
print(f'Использование pop в списке: ', timeit(f'create_list.pop()', globals=globals(), number=100000))
print(f'Использование pop в очереди: ', timeit(f'create_deque.pop()', globals=globals(), number=100000))
print(f'Использование popleft в очереди: ', timeit(f'create_deque.popleft()', globals=globals(), number=100000))

# Проведенные замеры показывают что создание списка происходит быстрее, чем очереди. А insert списка происходит дольше,
# чем appendleft очереди, тоже самое наблюдается при использовании операции pop