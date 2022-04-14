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

from timeit import timeit
from collections import deque


def input_lst_1(n):  # Сложность O(n)
    lst1 = list()
    for i in range(n):
        lst1.append(i)
    return lst1


def input_lst_2(n1, n2):  # Сложность O(n)
    lst2 = [chr(i) for i in range(n1, n2)]
    return lst2


def input_lst_3():  # Сложность O(n^2)
    lst3 = list()
    for i in lst2:
        for j in lst2:
            lst3.append(i + j)
    return lst3


def input_dq_1(n):  # Сложность O(n)
    dq1 = deque()
    for i in range(n):
        dq1.append(i)
    return dq1


def input_dq_2(n1, n2):  # Сложность O(n)
    dq2 = deque([chr(i) for i in range(n1, n2)])
    return dq2


def input_dq_3():  # Сложность O(n^2)
    dq3 = deque()
    for i in dq2:
        for j in dq2:
            dq3.append(i + j)
    return dq3


num = 1000000
num1 = 32
num2 = 128
lst2 = input_lst_2(num1, num2)
dq2 = input_dq_2(num1, num2)

print(timeit("input_lst_1(num)", globals=globals(), number=10))  # 1.3521545480000001
print(timeit("input_dq_1(num)", globals=globals(), number=10))  # 0.9888004940000001
print(timeit("input_lst_2(num1, num2)", globals=globals(), number=100000))  # 0.8389473400000003
print(timeit("input_dq_2(num1, num2)", globals=globals(), number=100000))  # 0.9729706610000002
print(timeit("input_lst_3()", globals=globals(), number=100))  # 0.18920708000000008
print(timeit("input_dq_3()", globals=globals(), number=100))  # 0.18695990999999967

# Скорость заполнения deque выше, чем у списка. При сложности O(n) разница достигает 35-40 %.
# Посредством list comprehensions - deque проигрывает, поскольку сначала заполняется сам список.
# При сложности O(n^2) разница во времени небольшая, но всё же, в пользу deque.


def lst2_insert(idx, val):    # Сложность O(1)
    lst2.insert(idx, val)
    return


def lst2_pop(idx):              # Сложность O(1)
    return lst2.pop(idx)


def lst2_extend_0(idx, lst):    # Сложность O(n)
    for i in lst:
        lst2.insert(idx, i)
    return


def dq2_appendleft(val):    # Сложность O(1)
    dq2.appendleft(val)
    return


def dq2_popleft():              # Сложность O(1)
    return dq2.popleft()


def dq2_extendleft(lst):    # Сложность O(1)
    dq2.extendleft(lst)
    return


i = 0
v = 'qwerty'
l = ['q', 'w', 'e', 'r', 't', 'y']

print(timeit("lst2_insert(i, v)", globals=globals(), number=100000))  # 6.702448069000001
print(timeit("lst2_pop(i)", globals=globals(), number=100000))  # 3.9516338710000003
print(timeit("lst2_extend_0(i, l)", globals=globals(), number=10000))  # 2.4794051390000007

print(timeit("dq2_appendleft(v)", globals=globals(), number=100000))  # 0.044544014999999604
print(timeit("dq2_popleft()", globals=globals(), number=100000))  # 0.023641264000001883
print(timeit("dq2_extendleft(l)", globals=globals(), number=10000))  # 0.004756475999997178

# По всем операциям с начальными элементами объекта (appendleft, popleft, extendleft для дека и аналогам для списка)
# дек во много раз превосходит по скорости списки (дек быстрее!).
