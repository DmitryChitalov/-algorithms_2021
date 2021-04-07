"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.

Операции равные по семантике (по смыслу)
Но разные по используемым ф-циям

И добавить аналитику, так ли это или нет.!
"""
from collections import deque
import timeit

list1 = [i for i in range(1000)]
de = deque([i for i in range(1000)])
# print(list1)
# print(de)



def l_append(lvar):
    for i in range(1000):
        lvar.append(i)

def d_append(dvar):
    for i in range(1000):
        dvar.append(i)

def l_insert(lvar):
    for i in range(100):
        lvar.insert(0, i)

def d_apleft(dvar):
    for i in range(100):
        dvar.appendleft(i)

def l_pop(lvar):
    for i in range(100):
        a = lvar.pop()

def d_pop(dvar):
    for i in range(100):
        a = dvar.pop()

def l_popleft(lvar):
    for i in range(100):
        a = lvar.pop(0)

def d_popleft(dvar):
    for i in range(100):
        a = dvar.popleft()

def l_reverse(lvar):
    lreversed = lvar.reverse()

def d_reverse(dvar):
    dreversed = dvar.reverse()

num = 10000

# print("Measurments for the append command")
# print("List: ", timeit.timeit('l_append(list1)', globals = globals(), number = num))
# print("Deque: ", timeit.timeit('d_append(de)', globals = globals(), number = num))
# print("Measurments for the insert command")
# print("List: ", timeit.timeit('l_insert(list1)', globals = globals(), number = num))
# print("Deque: ", timeit.timeit('d_apleft(de)', globals = globals(), number = num))
print("Measurments for the pop command")
print("List: ", timeit.timeit('l_pop(list1)', globals = globals(), number = num))
print("Deque: ", timeit.timeit('d_pop(de)', globals = globals(), number = num))
print("Measurments for the popleft command")
print("List: ", timeit.timeit('l_popleft(list1)', globals = globals(), number = num))
print("Deque: ", timeit.timeit('d_popleft(de)', globals = globals(), number = num))
print("Measurments for the reverse command")
print("List: ", timeit.timeit('l_reverse(list1)', globals = globals(), number = num))
print("Deque: ", timeit.timeit('d_reverse(de)', globals = globals(), number = num))


'''
на коммандах добавления в начало списка/очереди очередь гораздо быстрее (для чего она и используется), предполагаю что на popleft была бы пожая картина.


Measurments for the append command
List:  0.7916738
Deque:  0.5679875000000001

Measurments for the insert command:
List:  394.4995175
Deque:  0.047056100000000003

Measurments for the reverse command
List:  0.0038516999999999996
Deque:  0.009213599999999999







'''
