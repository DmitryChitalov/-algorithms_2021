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

        
def list_index(m):
    for _ in range(m):
        x = ls.index(m)
    

def deque_index(m):
    for _ in range(m):
        x = deq.index(m)
        

print('test_list_append: ', timeit('test_list_append(n)', globals=globals(), number=1000))
print('test_deq_append: ', timeit('test_deq_append(n)', globals=globals(), number=1000))
print('test_list_pop: ', timeit('test_list_pop(n)', globals=globals(), number=1000))
print('test_deq_pop: ', timeit('test_deq_pop(n)', globals=globals(), number=1000))
print('test_list_insert: ', timeit('test_list_insert(20)', globals=globals(), number=1000))
print('test_deq_append_left: ', timeit('test_deq_append_left(20)', globals=globals(), number=1000))
print('list_index: ', timeit('list_index(10)', globals=globals(), number=1000))
print('deque_index: ', timeit('deque_index(10)', globals=globals(), number=1000))
print('pop_first_list: ', timeit('pop_first_list(20)', globals=globals(), number=1000))
print('pop_first_deq: ', timeit('pop_first_deq(20)', globals=globals(), number=1000))

"""
test_list_append:  0.003658462082967162
test_deq_append:  0.0031735708471387625
test_list_pop:  0.002907297108322382
test_deq_pop:  0.002836200874298811
test_list_insert:  0.1248625151347369
test_deq_append_left:  0.0025537859182804823
list_index:  0.0031424430198967457
deque_index:  0.008274677908048034
pop_first_list:  0.04268808709457517
pop_first_deq:  0.0016381689347326756
Заполнение дека происходит быстрее, как и операции взятия первого/последнего элемента. В этих случаях разница во времени не критична, однако когда 
мы работаем с левой частью списка на добавление/удаление, она становится критичной. Insert существенно проигрывает в скорости appendleft, а pop с
аргументом 1 - popleft. 
Обратной оказывается ситуация, когда речь заходит об операции поиска индекса элемента. Обычный список отрабатывает в 2-2,5 раза быстрее.
"""
