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

from timeit import timeit
from collections import deque

simple_lst1 = []
simple_lst2 = []
deq_obj = deque(simple_lst1)


def func_1_1():
    deq_obj.append(1)
    return deq_obj


def func_1_2():
    simple_lst2.append(1)
    return simple_lst2


simple_lst1 = []
simple_lst2 = []
deq_obj = deque(simple_lst1)


def func_2_1():
    deq_obj.appendleft(1)
    return deq_obj


def func_2_2():
    simple_lst2.insert(0, 1)
    return simple_lst2


simple_lst1 = [[i * i for i in range(100000)]]
simple_lst2 = [[i * i for i in range(100000)]]
deq_obj = deque(simple_lst1)


def func_3_1():
    deq_obj.pop()
    return deq_obj


def func_3_2():
    simple_lst2.pop()
    return simple_lst2


lst = [x for x in range(1, 100)]
DEQUE_OBJ = deque(lst)


def func_4_1(lst):
    for x in lst:
        print(x, end=' ')
    print()


def func_4_2(lst):
    print(lst, end=' ')
    return None


def func_5_1(DEQUE_OBJ):
    for x in DEQUE_OBJ:
        print(x, end=' ')
    print()
    return None


def func_5_2(DEQUE_OBJ):
    print(DEQUE_OBJ, end=' ')
    return None


def func_6_1(DEQUE_OBJ):
    while len(DEQUE_OBJ) > 0:
        DEQUE_OBJ.popleft()


print('append(deque)', timeit("func_1_1()", number=2500000, globals=globals()))
print('append(list)', timeit("func_1_2()", number=2500000, globals=globals()))

print('appendleft(deque)', timeit("func_2_1()", number=1000, globals=globals()))
print('insert(list)', timeit("func_2_2()", number=1000, globals=globals()))

print('pop(deque)', timeit("func_3_1()", number=1000, globals=globals()))
print('pop(list)', timeit("func_3_2()", number=1000, globals=globals()))

print('iter(list)', timeit("func_4_1(lst)", globals=globals(), number=10000))
print('print(list)', timeit("func_4_2(lst)", globals=globals(), number=10000))

print('iterr(deque)', timeit("func_5_1(DEQUE_OBJ)", globals=globals(), number=10000))
print('print(deque)', timeit("func_5_2(DEQUE_OBJ)", globals=globals(), number=10000))

print('popleft(deque)', timeit("func_6_1(DEQUE_OBJ)", globals=globals(), number=1000000))

# Вывод: Заполнение элементами списка и очереди через метод append по времени практически одинаково,
# Вставка с помощью insert у списка происходит медленнее, чем у очереди appendleft, я думаю, из-за того
# что при вставке в простой список в начало элемента, все элементы сдвигаются, по логике, вставка в конец
# у списка будет более быстрая, чем вставка в начало.
# Далее я сделал итеррацию листа и дека, а так просто вывод.
# Итеррация списка медленнее, чем у очереди, а вот вывод заначений у списка быстрее.
# Извлечение значений у очереди намного быстрее, чем у списка с любой стороны.
