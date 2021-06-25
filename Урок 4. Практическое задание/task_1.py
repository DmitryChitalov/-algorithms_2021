"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Оптимизируйте, чтобы снизить время выполнения
Проведите повторные замеры.

Добавьте аналитику: что вы сделали и почему!!!
Без аналитики задание не принимается
"""

from timeit import repeat
import cProfile


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    return [i for i in range(len(nums)) if nums[i] % 2 == 0]


def func_3(nums):
    return [i for i, el in enumerate(nums) if el % 2 == 0]


def func_4(nums):
    new_arr = []
    append = new_arr.append
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            append(i)
    return new_arr


"""
Наилучшее время показала 3 функция, т.к. в ней напрямую через list comprehension формируется список без использования
append и вычисления длины первоначального списка в каждой итерации (заметно при профилировании через 
cProfile - см. ниже). Так же в интернете нашел интересный вариант func_4, который работает быстрее оригинально функции
за счёт вызова функции класса из переменной, а не с помощью объекта класса.
"""
# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(func_1(l))
# print(func_2(l))
# print(func_3(l))

stmt = ["func_1(nums)",
        "func_2(nums)",
        "func_3(nums)",
        "func_4(nums)"]

for st in stmt:
    print(f'на выполение функции {st} затрачено времени: '
          f'{min(repeat(st, setup="nums=range(100)", globals=globals()))}')


"""
на выполение функции func_1(nums) затрачено времени: 9.187302499999998
на выполение функции func_2(nums) затрачено времени: 8.485599100000002
на выполение функции func_3(nums) затрачено времени: 5.088985699999995
на выполение функции func_4(nums) затрачено времени: 8.929044800000014
"""

func = [func_1,
        func_2,
        func_3,
        func_4]

for f in func:
    print('-' * 30)
    print(f'Profiling: {f.__name__}')
    print('-' * 30)
    pr = cProfile.Profile()
    for i in range(10 ** 6):
        pr.runcall(f, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    pr.create_stats()
    pr.print_stats()

"""
------------------------------
Profiling: func_1
------------------------------
         8000000 function calls in 1.581 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
  1000000    1.177    0.000    1.536    0.000 task_1.py:20(func_1)
  1000000    0.054    0.000    0.054    0.000 {built-in method builtins.len}
  5000000    0.306    0.000    0.306    0.000 {method 'append' of 'list' objects}
  1000000    0.044    0.000    0.044    0.000 {method 'disable' of '_lsprof.Profiler' objects}


------------------------------
Profiling: func_2
------------------------------
         4000000 function calls in 1.057 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
  1000000    0.465    0.000    1.012    0.000 task_1.py:28(func_2)
  1000000    0.495    0.000    0.495    0.000 task_1.py:29(<listcomp>)
  1000000    0.053    0.000    0.053    0.000 {built-in method builtins.len}
  1000000    0.045    0.000    0.045    0.000 {method 'disable' of '_lsprof.Profiler' objects}


------------------------------
Profiling: func_3
------------------------------
         3000000 function calls in 0.946 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
  1000000    0.329    0.000    0.901    0.000 task_1.py:32(func_3)
  1000000    0.573    0.000    0.573    0.000 task_1.py:33(<listcomp>)
  1000000    0.045    0.000    0.045    0.000 {method 'disable' of '_lsprof.Profiler' objects}


------------------------------
Profiling: func_4
------------------------------
         8000000 function calls in 1.487 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
  1000000    1.078    0.000    1.442    0.000 task_1.py:36(func_4)
  1000000    0.055    0.000    0.055    0.000 {built-in method builtins.len}
  5000000    0.310    0.000    0.310    0.000 {method 'append' of 'list' objects}
  1000000    0.045    0.000    0.045    0.000 {method 'disable' of '_lsprof.Profiler' objects}

"""