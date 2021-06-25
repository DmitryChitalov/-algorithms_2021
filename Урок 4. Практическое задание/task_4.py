"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.

Без аналитики задание считается не принятым!
"""

from timeit import repeat
import cProfile
import random

array = [1, 3, 1, 3, 4, 5, 1]


def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


def func_3():
    elem = max(array, key=array.count)
    count = array.count(elem)
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {count} раз(а)'


print(func_1())
print(func_2())
print(func_3())

stmt = ["func_1()",
        "func_2()",
        "func_3()"]


for st in stmt:
    print(f'на выполение функции {st} затрачено времени: '
          f'{min(repeat(st, globals=globals()))}')

func = [func_1,
        func_2,
        func_3]

for f in func:
    print('-' * 30)
    print(f'Profiling: {f.__name__}')
    print('-' * 30)
    pr = cProfile.Profile()
    for i in range(10 ** 5):
        pr.runcall(f)
    pr.create_stats()
    pr.print_stats()


"""
По результатам замеров меньше всего времени ушло на выполнение первой функции, однако, при увеличении кол-ва элементов
n в массиве эффективнее всего работает функция 3, т.к. в нем сразу определяется максимально встречающийся элемент.
Первый вариант менее предпочтителен из-за наличия цикла. Второй вариант самый медленный из-за наличия цикла, 
создания и заполнения нового массива и затем поиска максимального значения в новом массиве.

на выполение функции func_1() затрачено времени: 0.9196177999999997
на выполение функции func_2() затрачено времени: 1.2238440000000006
на выполение функции func_3() затрачено времени: 1.0079244999999997
------------------------------
Profiling: func_1
------------------------------
         900000 function calls in 0.193 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   100000    0.117    0.000    0.189    0.000 task_4.py:22(func_1)
   700000    0.071    0.000    0.071    0.000 {method 'count' of 'list' objects}
   100000    0.004    0.000    0.004    0.000 {method 'disable' of '_lsprof.Profiler' objects}


------------------------------
Profiling: func_2
------------------------------
         1800000 function calls in 0.370 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   100000    0.218    0.000    0.365    0.000 task_4.py:34(func_2)
   100000    0.018    0.000    0.018    0.000 {built-in method builtins.max}
   700000    0.044    0.000    0.044    0.000 {method 'append' of 'list' objects}
   700000    0.077    0.000    0.077    0.000 {method 'count' of 'list' objects}
   100000    0.005    0.000    0.005    0.000 {method 'disable' of '_lsprof.Profiler' objects}
   100000    0.008    0.000    0.008    0.000 {method 'index' of 'list' objects}


------------------------------
Profiling: func_3
------------------------------
         400000 function calls in 0.139 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   100000    0.057    0.000    0.134    0.000 task_4.py:46(func_3)
   100000    0.068    0.000    0.068    0.000 {built-in method builtins.max}
   100000    0.010    0.000    0.010    0.000 {method 'count' of 'list' objects}
   100000    0.005    0.000    0.005    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""