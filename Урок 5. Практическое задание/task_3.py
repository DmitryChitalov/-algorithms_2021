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

list_1 = list()
deq_1 = deque(list_1)

def fill_fun(cur_list):
    for x in range(1000):
        cur_list.append(x)


def fun_list_1(cur_list):
    cur_list.insert(0, 500)


def fun_deq_1(cur_deq):
    cur_deq.appendleft(500)


def fun_list_2_1(cur_list):
    cur_list.pop(0)

def fun_list_2_2(cur_list):
    cur_list.pop()

def fun_deq_2_1(cur_deq):
    cur_deq.popleft()

def fun_deq_2_2(cur_deq):
    cur_deq.pop()

print("Заполнение списка", timeit("fill_fun(list_1)", globals=globals(), number=10000))
print("Заполнение очереди", timeit("fill_fun(deq_1)", globals=globals(), number=10000))
print("Добавление в начало списка", timeit("fun_list_1(list_1)", globals=globals(), number=10000))
print("Добавление в начало очердь", timeit("fun_deq_1(deq_1)", globals=globals(), number=10000))
print("Удаление из начала списка", timeit("fun_list_2_1(list_1)", globals=globals(), number=10000))
print("Удаление с конца списка", timeit("fun_list_2_2(list_1)", globals=globals(), number=10000))
print("Удаление из начала очереди", timeit("fun_deq_2_1(deq_1)", globals=globals(), number=10000))
print("Удаление с конца очереди", timeit("fun_deq_2_1(deq_1)", globals=globals(), number=10000))

# Заполнение списка 0.6838525
# Заполнение очереди 0.5866668999999999
# ---Наполнение элементами списка длится чуть дольше, но не критично---

# Добавление в начало списка 70.7593818
# Добавление в начало очердь 0.0009275999999971418
# ---Тяжело списку вставить элемент вначало. Время отличается на несколько порядков---

# Удаление из начала списка 86.0461768
# Удаление с конца списка 0.0013219999999876109
# Удаление из начала очереди 0.001155299999993531
# Удаление с конца очереди 0.0011632000000076914
# ---Удаление первого элемента из списка - тоже очень долго. Очередь на несколько порядков быстрее---