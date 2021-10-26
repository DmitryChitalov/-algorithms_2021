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

lst_obj = [1,2,3]
deq_obj = deque(lst_obj)

def fill_lst():
    lst_obj = [x for x in range(10000)]
    return lst_obj

def fill_deq():
    deq_obj = [x for x in range(10000)]
    return deq_obj

def lst_in():
    lst_obj.insert(0, 12)
    return lst_obj

def deq_al():
    deq_obj.appendleft(12)
    return deq_obj

def lst_pop():
    lst_obj.pop(0)
    return lst_obj

def deq_pop():
    deq_obj.popleft()
    return deq_obj

def lst_extl():
    a = [1,2,3]
    for i in range(len(a)):
       lst_obj.insert(0,a[i])
    return lst_obj

def deq_extl():
    deq_obj.extendleft([1,2,3])
    return deq_obj



print(
    timeit(
        "fill_lst()",
        setup="from __main__ import fill_lst", number=10000))

print(
    timeit(
        "fill_deq()",
        setup="from __main__ import fill_deq", number=10000))

print(
    timeit(
        "lst_in()",
        setup="from __main__ import lst_in", number=10000))

print(
    timeit(
        "deq_al()",
        setup="from __main__ import deq_al", number=10000))

print(
    timeit(
        "lst_pop()",
        setup="from __main__ import lst_pop", number=10000))

print(
    timeit(
        "deq_pop()",
        setup="from __main__ import deq_pop", number=10000))

print(
    timeit(
        "lst_extl()",
        setup="from __main__ import lst_extl", number=10000))
print(
    timeit(
        "deq_extl()",
        setup="from __main__ import deq_extl", number=10000))

'''
Заполнение 10 000 повторений:
LIST - 4.2736143
DEQUE - 4.669486899999999

Добавление элемента в начало 10 000 повторов:
lst_in - 0.03999349999999957
deq_al - 0.010175800000000734
LIST дольше вставляет элемент в начало списка

Удаление элемент из начала 10 000 повторов:
lst_pop - 0.026750599999999736
deq_pop - 0.0018686999999992793
LIST дольше удаляет элемент из начало списка

Добавление списка элементов в начало 10 000 повторов:
lst_extl - 0.5119787999999996
deq_extl - 0.003945200000000426
LIST на 8603% дольше добавляет список элементов в начало
'''