from collections import deque
from timeit import timeit
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


"""
Создание deque слегка ступает по скорости соданию списка, это компенсируется удобством и скоростью
в дельнейшей работе с deque.
Под удобством подразумевается наличие отдельных функций для вставки в начало, не прибегая к индексу.
"""


num = 1000
num_insert = 555
iter_object = [333, 444, 555]
counter = 10000

create_dq = deque(range(num))
create_lst = list(range(num))

print('*' * 50)
print(timeit('deque(range(num))', globals=globals(), number=counter), '- create deque')
print(timeit('list(range(num))', globals=globals(), number=counter), '- create list')
print('*' * 50)
print(timeit('create_dq.appendleft(num_insert)', globals=globals(), number=1), '- appendleft')
print(timeit('create_lst.insert(0, num_insert)', globals=globals(), number=1), '- insert(0)')
print('*' * 50)
print(timeit('create_dq.popleft()', globals=globals(), number=1), '- popleft')
print(timeit('create_lst.pop(0)', globals=globals(), number=1), '- pop(0)')
print('*' * 50)
print(timeit('create_dq.extendleft(iter_object[::-1])', globals=globals(), number=1), '- extendleft')
print(timeit('iter_object + create_lst', globals=globals(), number=1), '- конкатенация')
print('*' * 50)
