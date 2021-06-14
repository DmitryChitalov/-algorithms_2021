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


def lst_app():
    lst = [i for i in range(50)]
    return lst


def dqe_app():
    dqe = deque([i for i in range(50)])
    return dqe


lst = lst_app()
dqe = dqe_app()

print("Замеры времени для функций создания списка и деки: ")
lst_time = timeit("lst_app()", globals=globals(), number=100)
print(f"List: {lst_time}")
dqe_time = timeit("dqe_app()", globals=globals(), number=100)
print(f"Deque: {dqe_time}")

print("Замеры времени для функции append: ")
lst_time = timeit("lst.append('ghjk')", globals=globals(), number=100)
print(f"List: {lst_time}")
dqe_time = timeit("dqe.append('ghjk')", globals=globals(), number=100)
print(f"Deque: {dqe_time}")

print("Замеры времени для функции remove: ")
lst_time = timeit("lst.remove('ghjk')", globals=globals(), number=100)
print(f"List: {lst_time}")
dqe_time = timeit("dqe.remove('ghjk')", globals=globals(), number=100)
print(f"Deque: {dqe_time}")

print("Замеры времени для функции count: ")
lst_time = timeit("lst.count(6)", globals=globals(), number=100)
print(f"List: {lst_time}")
dqe_time = timeit("dqe.count(6)", globals=globals(), number=100)
print(f"Deque: {dqe_time}")

print("Замеры времени для функции reverse: ")
lst_time = timeit("lst.reverse()", globals=globals(), number=100)
print(f"List: {lst_time}")
dqe_time = timeit("dqe.reverse()", globals=globals(), number=100)
print(f"Deque: {dqe_time}")

print("Замеры времени для функции insert, appendleft: ")
lst_time = timeit("lst.insert(0, 5)", globals=globals(), number=100)
print(f"List: {lst_time}")
dqe_time = timeit("dqe.appendleft(5)", globals=globals(), number=100)
print(f"Deque: {dqe_time}")

"""
Замеры времени для функций создания списка и деки: 
List: 0.00011919999999999986
Deque: 0.00016399999999999748

Замеры времени для функции append: 
List: 7.699999999999374e-06
Deque: 5.699999999997374e-06

Замеры времени для функции remove: 
List: 7.680000000000187e-05
Deque: 0.0001010999999999998

Замеры времени для функции count: 
List: 4.7699999999997744e-05
Deque: 5.039999999999906e-05

Замеры времени для функции reverse: 
List: 5.299999999999749e-06
Deque: 7.000000000000062e-06

Замеры времени для функции insert, appendleft: 
List: 1.1999999999998123e-05
Deque: 4.299999999998749e-06

У списков быстрее выполняются такие операции, как reverse, remove и count, также, список быстрее создается
Для деки быстрее выполняются функции append и appendleft
"""
