"""
Задание 1.
Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 3-5 ваших РАЗНЫХ скриптов!
(хотя бы 3 разных для получения оценки отл).
На каждый скрипт вы должны сделать как минимум по две реализации.
Можно взять только домашние задания с курса Основ
или с текущего курса Алгоритмов
Результаты профилирования добавьте в виде комментариев к коду.
Обязательно сделайте аналитику (что с памятью в ваших скриптах, в чем ваша оптимизация и т.д.)
ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!
"""
from memory_profiler import profile, memory_usage


#  1  Сумма ряда 1 -0.5 0.25 -0.125 ...
# рекурсия
def math_series(n):
    return [1, 1] if n == 1 else [math_series(n - 1)[0] * -0.5, (math_series(n - 1)[1] + math_series(n - 1)[0] * -0.5)]


@profile
def recur(n):
    return math_series(n)


# цикл
@profile
def math_series2(n):
    curr_el = 1
    while n != 0:
        if curr_el == 1:
            summ = 1
        else:
            summ += curr_el
        curr_el *= -0.5
        n -= 1
    return summ


# recur(5)
# math_series2(5)
"""
Рекурсия
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    27     19.4 MiB     19.4 MiB           1   @profile
    28                                         def recur(n):
    29     19.4 MiB      0.0 MiB           1       return math_series(n)

Цикл
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    33     19.5 MiB     19.5 MiB           1   @profile
    34                                         def math_series2(n):
    35     19.5 MiB      0.0 MiB           1       curr_el = 1
    36     19.5 MiB      0.0 MiB           6       while n != 0:
    37     19.5 MiB      0.0 MiB           5           if curr_el == 1:
    38     19.5 MiB      0.0 MiB           1               summ = 1
    39                                                 else:
    40     19.5 MiB      0.0 MiB           4               summ += curr_el
    41     19.5 MiB      0.0 MiB           5           curr_el *= -0.5
    42     19.5 MiB      0.0 MiB           5           n -= 1
    43     19.5 MiB      0.0 MiB           1       return summ

В плане потребляемой памяти разницы между реккурсивным решением и решением через цикл разницы не наблюдается, 
не смотря на значительную разницу во времени выполнения программы. Использование циклов вместо рекурсии для 
уменьшенеия затрат на память не эффективно. Хотя возможно это не самый удачный пример
"""

#  2  Сравнение потребляемой памяти обычным словарем и OrderedDict
from collections import OrderedDict

# origin_dict = {}
# ordered_dict = OrderedDict([])
# user_list = []
# for i in range(100000):
#     user_list.append(i)

@profile
def filler(user_dict, seq):
    for i in seq:
        user_dict[i] = i
    return user_dict

def generator(n):
    num = 0
    while num < n:
        yield num
        num += 1

#filler(origin_dict, user_list)
#filler(origin_dict, range(100000))
#filler(origin_dict, generator(100000))
#filler(ordered_dict, range(100000))
"""
Обычный словарь c пользовательским списком
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    85     24.0 MiB     24.0 MiB           1   @profile
    86                                         def filler(user_dict, seq):
    87     28.4 MiB      0.0 MiB      100001       for i in seq:
    88     28.4 MiB      4.5 MiB      100000           user_dict[i] = i
    89     28.4 MiB      0.0 MiB           1       return user_dict

Обычный словарь с функцией range
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    85     19.5 MiB     19.5 MiB           1   @profile
    86                                         def filler(user_dict, seq):
    87     27.6 MiB      0.0 MiB      100001       for i in seq:
    88     27.6 MiB      8.1 MiB      100000           user_dict[i] = i
    89     27.6 MiB      0.0 MiB           1       return user_dict

Обычный словарь с генераторной функцией
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    85     19.6 MiB     19.6 MiB           1   @profile
    86                                         def filler(user_dict, seq):
    87     27.7 MiB      0.0 MiB      100002       for i in seq:
    88     27.7 MiB      8.1 MiB      100001           user_dict[i] = i
    89     27.7 MiB      0.0 MiB           1       return user_dict
    
При использовании словаря с функцией range или с генераторной функцией для наполнения словаря
памяти расходуется чуть меньше, чем при использовании готового списка в качестве последовательности для наполнения.
Это объесняется хранением списка значений до того, как заполнение словаря начнется, что требует дополнительной памяти

OrderedDict
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    82     19.5 MiB     19.5 MiB           1   @profile
    83                                         def filler(user_dict):
    84     32.7 MiB      0.0 MiB      100001       for i in range(100000):
    85     32.7 MiB     13.1 MiB      100000           user_dict[i] = i
    86     32.7 MiB      0.0 MiB           1       return user_dict

Использование памяти в случае с OrderedDict с функцией range больше, чем при использовании обычного словаря c этой же функцией. 
Всё таки OrderedDict не дает совсем никаких приемуществ перед обычным словарём, а я так надеялся ((((
"""

#  3  сохранение в массиве индексов четных элементов другого массива
# Решение с низким быстродействием
@profile
def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


# Решение с большим быстродействием
@profile
def func_1_modern(nums):
    new_arr = [i for i, val in enumerate(nums) if not val % 2]
    return new_arr

@profile
def func_1_modern2(nums):
    new_arr = (i for i, val in enumerate(nums) if not val % 2)
    return new_arr


user_list = []
for i in range(10):
    user_list.append(i)

# func_1(user_list)
# func_1_modern(user_list)
# func_1_modern2(user_list)

'''
Решение с помощью func_1
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   148     24.1 MiB     24.1 MiB           1   @profile
   149                                         def func_1(nums):
   150     24.1 MiB      0.0 MiB           1       new_arr = []
   151     25.7 MiB      0.0 MiB      100001       for i in range(len(nums)):
   152     25.7 MiB      1.5 MiB      100000           if nums[i] % 2 == 0:
   153     25.7 MiB      0.1 MiB       50000               new_arr.append(i)
   154     25.7 MiB      0.0 MiB           1       return new_arr

Решение с помощью func_1_modern   
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   158     24.8 MiB     24.8 MiB           1   @profile
   159                                         def func_1_modern(nums):
   160     26.3 MiB      1.5 MiB      100003       new_arr = [i for i, val in enumerate(nums) if not val % 2]
   161     26.3 MiB      0.0 MiB           1       return new_arr

Решение с помощью func_1_modern2
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   163     24.0 MiB     24.0 MiB           1   @profile
   164                                         def func_1_modern2(nums):
   165     24.0 MiB      0.0 MiB           1       new_arr = (i for i, val in enumerate(nums) if not val % 2)
   166     24.0 MiB      0.0 MiB           1       return new_arr
   
Замена списка в func_1_modern на генератор (func_1_modern2) значительно уменьшило потребление памяти 
(хоть и немного изменило логику работы функции). Теперь она выдает генераторное выражение, и потому использует мало памяти
'''