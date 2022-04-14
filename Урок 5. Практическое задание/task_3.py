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


deque_obj = deque([x for x in range(10)])
simple_list = [x for x in range(10)]

print(timeit('deque_obj = deque([x for x in range(100)])', globals=globals()))  # 2.973447119
print(timeit('simple_list = [x for x in range(100)]', globals=globals()))  # 2.2823517059999996
# deque заполняется чуть дольше чем список
#
print(timeit('deque_obj.appendleft(1)', globals=globals(), number=100000))  # 0.004599749999999996
print(timeit('simple_list.insert(0,1)', globals=globals(), number=100000))  # 1.9185675610000001
# Вставка по индексу в список была на столько долго, что пришлось снизить кол-во операций
# Вставка в deque в начало работет очень быстро

deque_obj = deque([x for x in range(100001)])
simple_list = [x for x in range(100001)]

print(timeit('deque_obj.popleft()', globals=globals(), number=100000))  # 0.004548834000000002
print(timeit('simple_list.pop(0)', globals=globals(), number=100000))  # 0.992870971
# Удаление из начала списка значительно дольше, чем из deque

deque_obj = deque([x for x in range(10)])
simple_list = [x for x in range(10)]

extend_list = [1, 2, 3]


def extendleft_list(simple_list, extend_list):
    for i in extend_list:
        simple_list.insert(0, i)


print(timeit('deque_obj.extendleft(extend_list)', globals=globals(), number=100000))  # 0.008598752999999997
print(timeit('extendleft_list(simple_list, extend_list)', globals=globals(), number=100000))  # 17.676073337000002
# В случае со вставкой итерируемого аргумента пришлось создать фунецию для списка, т.к. встроенного механизма нет
# разница во времени очень большая, в пользу deque

deque_obj = deque([x for x in range(100000)])
simple_list = [x for x in range(100000)]

print(timeit('deque_obj[50000] += 1', globals=globals()))  # 8.617607789
print(timeit('simple_list[50000] += 1', globals=globals()))  # 0.06164279099999881

print(timeit('deque_obj[1] += 1', globals=globals()))  # 0.06943400699999991
print(timeit('simple_list[1] += 1', globals=globals()))  # 0.05621900599999918

print(timeit('deque_obj[99999] += 1', globals=globals()))  # 0.07586330300000022
print(timeit('simple_list[99999] += 1', globals=globals()))  # 0.06275838200000017
# а вот тут очень интересное поведение, если мы обращаемся по индексу то чем ближу к любому из краев deque
# тем быстрее идёт выполнение, а чем ближе к середине тем дольше


print(timeit('deque_obj.count(500)', globals=globals(), number=10000))  # 10.63636917
print(timeit('simple_list.count(500)', globals=globals(), number=10000))  # 10.054846277999998
# операция count почти равны, список всегда незначительно быстрее
