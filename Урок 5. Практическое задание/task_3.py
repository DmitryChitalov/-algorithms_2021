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
list_2 = deque(list_1)


def func_full(lis):
    for x in range(100):
        lis.append(x)


print("Заполнение списка", timeit("func_full(list_1)", globals=globals(), number=10000))
print("Заполнение очерди", timeit("func_full(list_2)", globals=globals(), number=10000))
"""Время заполнение больше у списка, чем у очереди исходя из замеров"""


def func_1(lis):
    lis.insert(0, "ok")


def func_2(deq):
    deq.appendleft("ok")


def func_3(lis):
    lis.pop(0)


def func_4(deq):
    deq.popleft()


def func_5(deq):
    deq.insert(len(deq) // 2, "not ok")


print("Добавление в начало списока", timeit("func_1(list_1)", globals=globals(), number=10000))
print("Добавление в начало очердь", timeit("func_2(list_2)", globals=globals(), number=10000))
print("удаление в начале списка", timeit("func_3(list_1)", globals=globals(), number=10000))
print("удаление в начале очерди", timeit("func_4(list_2)", globals=globals(), number=10000))
"""Время выполнения различных операций больше у списка, чем у очереди исходя из замеров"""
print("взятие среднего элемента списка", timeit("func_5(list_1)", globals=globals(), number=10000))
print("взятие среднего элемента очереди", timeit("func_5(list_2)", globals=globals(), number=10000))
"""Но если брать не с конца и начала, а произвольное то скорость очереди ниже, чем списка"""

"""Вывод: для быстрого заполнения лудшее использовать очередь, а для быстрого поиска список"""
