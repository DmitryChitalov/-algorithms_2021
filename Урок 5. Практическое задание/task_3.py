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
import cProfile
from collections import deque

def list_app_func(num):
    lst = []
    for i in num:
        lst.append(i)

def deque_app_func(num):
    lst = deque()
    for i in num:
        lst.append(i)

def list_ins_func(num):
    lst = []
    for i in num:
        lst.insert(0, i)

def deque_ins_func(num):
    lst = deque()
    for i in num:
        lst.appendleft(i)

def deque_popleft_func(num):
    lst = deque()
    for i in num:
        lst.popleft(i)

def deque_extendleft_func(num):
    lst = deque()
    for i in num:
        lst.extendleft(i)

def main():
    my_nums = [i for i in range(100000)]

    list_app_func(my_nums)
    deque_app_func(my_nums)
    list_ins_func(my_nums)
    deque_ins_func(my_nums)
    #deque_popleft_func(my_nums)
    #deque_extendleft_func(my_nums)

cProfile.run('main()')

'''
C:\Users\79115\AppData\Local\Programs\Python\Python39\python.exe "C:/Users/79115/Desktop/2 Урок Алгоритмы/Урок 2. Коды примеров/Algorithm5.3.3.py"
         400009 function calls in 1.736 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.001    0.001    1.736    1.736 <string>:1(<module>)
        1    0.022    0.022    1.672    1.672 Algorithm5.3.3.py:14(list_ins_func)     
        1    0.010    0.010    0.017    0.017 Algorithm5.3.3.py:19(deque_ins_func)
        1    0.002    0.002    1.735    1.735 Algorithm5.3.3.py:34(main)
        1    0.004    0.004    0.004    0.004 Algorithm5.3.3.py:35(<listcomp>)
        1    0.013    0.013    0.021    0.021 Algorithm5.3.3.py:4(list_app_func)
        1    0.012    0.012    0.020    0.020 Algorithm5.3.3.py:9(deque_app_func)
        1    0.000    0.000    1.736    1.736 {built-in method builtins.exec}
   100000    0.008    0.000    0.008    0.000 {method 'append' of 'collections.deque' objects}
   100000    0.008    0.000    0.008    0.000 {method 'append' of 'list' objects}
   100000    0.006    0.000    0.006    0.000 {method 'appendleft' of 'collections.deque' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
   100000    1.650    0.000    1.650    0.000 {method 'insert' of 'list' objects}



Process finished with exit code 0

The most effective way would be to use deque**Наиболее эффектиным будет использование deque
Populating the list is 9.8 times slower**Заполнение списка работает медленнее в 9,8 раза
Changing the list is pretty much the same**Изменение списка практически одинаково

'''




