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

lst = [x for x in range(1, 100)]
DEQUE_OBJ = deque(lst)

def create_list_comprehension(n):
    lst = [x for x in range(1, n)]
    return lst

def create_list_append(n):
    lst = []
    for x in range(1, n):
        lst.append(x)
    return lst

def create_list_insert(n):
    lst = []
    for x in range(1, n):
        lst.insert(1, x)
    return lst

def deque_appendleft(lst):
    for x in lst:
        DEQUE_OBJ.appendleft(x)
    return DEQUE_OBJ

def deque_append(lst):
    for x in lst:
        DEQUE_OBJ.append(x)
    return DEQUE_OBJ

def iterr_list(lst):
    """Итеррация листа"""
    for x in lst:
        print(x, end=' ')
    print()

def print_list(lst):
    """Вывод листа"""
    print(lst, end=' ')

def print_deque(DEQUE_OBJ):
    """Итеррация дека"""
    for x in DEQUE_OBJ:
        print(x, end=' ')
    print()

def iterr_deque(DEQUE_OBJ):
    """Вывод дека"""
    print(DEQUE_OBJ, end=' ')

def pop_list(lst):
    for num, x in enumerate(lst):
        lst.pop(num)

def pop_deque(DEQUE_OBJ):
    while len(DEQUE_OBJ) > 0:
        DEQUE_OBJ.pop()

def popleft_deque(DEQUE_OBJ):
    while len(DEQUE_OBJ) > 0:
        DEQUE_OBJ.popleft()


print(timeit("create_list_comprehension(n=100)", globals=globals(), number=1000000))
print(timeit("create_list_append(n=100)", globals=globals(), number=1000000))
print(timeit("create_list_insert(n=100)", globals=globals(), number=1000000))

print(timeit("deque_append(lst)", globals=globals(), number=1000000))
print(timeit("deque_appendleft(lst)", globals=globals(), number=1000000))

print(timeit("iterr_list(lst)", globals=globals(), number=10000))
print(timeit("print_list(lst)", globals=globals(), number=10000))

print(timeit("iterr_deque(DEQUE_OBJ)", globals=globals(), number=10000))
print(timeit("print_deque(DEQUE_OBJ)", globals=globals(), number=10000))

print(timeit("pop_list(lst)", globals=globals(), number=1000000))
print(timeit("pop_deque(DEQUE_OBJ)", globals=globals(), number=1000000))

print(timeit("popleft_deque(DEQUE_OBJ)", globals=globals(), number=1000000))
print(timeit("popleft_deque(DEQUE_OBJ)", globals=globals(), number=1000000))

"""
Результат выполнения ф-й:

    5.196888704 - Наполнение LC
    10.807711992000002 - Наполнение листа append
    19.753582452999996 - Наполнение листа insert
    9.691727071999999 - Наполнение дека append
    10.008746659 - Наполнение дека appendleft
    15.933591641 - Итеррация листа при number=10000
    0.385838235 - Принт листа при number=10000
    0.429816674 - Итеррация дека при number=10000
    15.294591536999999 принт дека при number=10000
    0.397302085 - Извлечение pop у листа
    0.20178788099999995 - Извлечение pop у дека
    0.231328906 - Извлечение popleft у дека

Вывод: Наполнение листа и дека через метод append примерно за одно и тоже время происходит,
а вот insert у листа значительно возврастает - в два раза. Быстрее всего наполнение LC -
в двараза быстрее append. Далее я сделал итеррацию листа и дека, а так просто вывод.
Тут вышло все наоборот: итеррация листа 15 сек, а у дека 0,5 сек, но с выводом картина
меняет с наоборот print list 0.3 сек, а print дека - 15 сек. Извлечение эл-ов у дека 
происходит почти в 2 раза быстрее, чем у листа, что слева, что справа
"""