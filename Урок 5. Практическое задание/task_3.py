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

deq = deque()
ls = []
n = [i for i in range(50)]


def test_list_append(n):
    for i in n:
        ls.append(i)


def test_deq_append(n):
    for i in n:
        deq.append(i)


def test_list_pop(n):
    for _ in n:
        ls.pop()


def test_deq_pop(n):
    for _ in n:
        deq.pop()


def test_list_insert(m):
    for i in range(m):
        ls.insert(0, i)


def test_deq_append_left(m):
    for i in range(m):
        deq.appendleft(i)


def pop_first_list(m):
    for _ in range(m):
        ls.pop(0)


def pop_first_deq(m):
    for _ in range(m):
        deq.popleft()


print('test_list_append: ', timeit('test_list_append(n)', globals=globals(), number=1000))
print('test_deq_append: ', timeit('test_deq_append(n)', globals=globals(), number=1000))
print('test_list_pop: ', timeit('test_list_pop(n)', globals=globals(), number=1000))
print('test_deq_pop: ', timeit('test_deq_pop(n)', globals=globals(), number=1000))
print('test_list_insert: ', timeit('test_list_insert(20)', globals=globals(), number=1000))
print('test_deq_append_left: ', timeit('test_deq_append_left(20)', globals=globals(), number=1000))
print('pop_first_list: ', timeit('pop_first_list(20)', globals=globals(), number=1000))
print('pop_first_deq: ', timeit('pop_first_deq(20)', globals=globals(), number=1000))

"""
test_list_append:  0.0033137999999999987
test_deq_append:  0.0034575000000000022
test_list_pop:  0.0030244999999999994
test_deq_pop:  0.0029143000000000086
test_list_insert:  0.089202
test_deq_append_left:  0.0015665999999999736
pop_first_list:  0.042269100000000004
pop_first_deq:  0.0014939999999999953
Значительной оказываетеся разница, когда работа происходит с левой частью списка (в 40-90 раз). Использовать 
deque логично, когда требуется частый доступ к началу списка.
"""
