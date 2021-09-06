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


deq = deque([i for i in range(1000)])
lst = [i for i in range(1000)]


print(timeit('deq', globals=globals(), number=100000))                                          # 0.002197600000000001
print(timeit('lst', globals=globals(), number=100000))                                          # 0.0019526999999999947
print(timeit('deq.appendleft(0)', globals=globals(), number=100000))                            # 0.0057597999999999955
print(timeit('lst.insert(0, 0)', globals=globals(), number=100000))                             # 2.6567113
print(timeit('deq.popleft()', globals=globals(), number=100000))                                # 0.00479850000000015
print(timeit('lst.pop(0)', globals=globals(), number=100000))                                   # 1.8219268000000004
print(timeit('deq.extendleft(["a", "b", "c"])', globals=globals(), number=100000))              # 0.014374899999999968
print(timeit("[lst.insert(0, i) for i in ['a', 'b', 'c']]", globals=globals(), number=100000))  # 24.1793473

"""
Все операции с модулем deque выполняются быстрее, кроме создания но разница там не существенная.
"""
