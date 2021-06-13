﻿"""
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

my_list = []
my_deque = deque()


def fill_list():
    my_list = []
    my_list = [i for i in range(1000)]
    return my_list


def fill_deque():
    my_deque = deque()
    my_deque = [i for i in range(1000)]
    return deque(my_deque)


print("Заполнение списка и дека (1000 элементов, 10^4 повторов):")
print("Список	-	", timeit("my_list = fill_list()", globals=globals(), number=10000))
print("Дек  	-	", timeit("my_deque = fill_deque()", globals=globals(), number=10000))

my_list = fill_list()
my_deque = fill_deque()

print("\nПолучение произвольного элемента списка и дека (10^4 повторов):")
print("Список	-	", timeit("a = my_list[10]", globals=globals(), number=10000))
print("Дек  	-	", timeit("a = my_deque[10]", globals=globals(), number=10000))

print("\nВставка элемента в начало (10^5 повторов):")
print("Список	-	", timeit("my_list.insert(0, 100)", globals=globals(), number=100000))
print("Дек  	-	", timeit("my_deque.appendleft(100)", globals=globals(), number=100000))

print("\nДобавление элемента в конец (10^5 повторов):")
print("Список	-	", timeit("my_list.append(100)", globals=globals(), number=100000))
print("Дек  	-	", timeit("my_deque.append(100)", globals=globals(), number=100000))

print("\nИзвлечение элемента с начала (10^5 повторов):")
print("Список	-	", timeit("my_list.pop(0)", globals=globals(), number=100000))
print("Дек  	-	", timeit("my_deque.popleft()", globals=globals(), number=100000))

print("\nИзвлечение элемента с конца (10^5 повторов):")
print("Список	-	", timeit("my_list.pop(len(my_list) - 1)", globals=globals(), number=100000))
print("Дек  	-	", timeit("my_deque.pop()", globals=globals(), number=100000))

"""

На основе результатов замеров ниже можно сделать следующие выводы:
1. Заполнение и добавление вставкой элементов в конец осуществляется немного быстрее для дека, чем для списка, но не
    существенно (в обоих случаях сложность константная)
2. Получение произвольного элемента происходит немного быстрее для списка, но не существенно (в обоих случаях сложность
    линейная) 
3. Добавление элементов в начало/конец, извлечение с начала/конца осуществляются намного быстрее для дека (сложность 
    для дека - константная, для списка - линейная)

Заполнение списка и дека (1000 элементов, 10^4 повторов):
Список	-	 0.609742431
Дек  	-	 0.6630648490000001

Получение произвольного элемента списка и дека (10^4 повторов):
Список	-	 0.0005518210000001744
Дек  	-	 0.0005683189999998728

Вставка элемента в начало (10^5 повторов):
Список	-	 1.756546191
Дек  	-	 0.008834826999999823

Добавление элемента в конец (10^5 повторов):
Список	-	 0.015335507000000081
Дек  	-	 0.010949383000000257

Извлечение элемента с начала (10^5 повторов):
Список	-	 1.6738776990000002
Дек  	-	 0.006793658000000313

Извлечение элемента с конца (10^5 повторов):
Список	-	 0.025362722999999754
Дек  	-	 0.00661559499999953

"""
