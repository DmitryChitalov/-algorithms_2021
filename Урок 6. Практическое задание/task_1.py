"""
Задание 1.

Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 3-5 ваших РАЗНЫХ скриптов!
(хотя бы 3 разных для получения оценки отл).
На каждый скрипт вы должны сделать как минимум по две реализации.

Можно взять задачи с курса Основ
или с текущего курса Алгоритмов

Результаты профилирования добавьте в виде комментариев к коду.
Обязательно сделайте аналитику (что с памятью в ваших скриптах, в чем ваша оптимизация и т.д.)

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО

Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!
"""


import json
import random
import time
from memory_profiler import profile, memory_usage


def time_of_function(function):
    @profile()
    def wrapper(*args):
        m_1 = memory_usage()
        start_val = time.time()
        function(*args)
        end_val = time.time()
        m_2 = memory_usage()
        time_funk = end_val - start_val
        return time_funk, print(f'{m_2[0] - m_1[0]} MiB')
    return wrapper


my_list = []
my_dict = {}


@time_of_function
def list_app(i=1):
    for i in range(i):
        my_list.append(random.choice(range(1000, 1000000000)))
    return my_list


@time_of_function
def list_app_gen(i=1):
    for i in range(i):
        my_list.append(random.choice(range(1000, 1000000000)))
    yield my_list


@time_of_function
def dict_app(i=1):
    for i in range(i):
        my_dict[i] = (random.choice(range(1000, 1000000000)))
    return my_dict


@time_of_function
def dict_app_gen(i=1):
    for i in range(i):
        my_dict[i] = (random.choice(range(1000, 1000000000)))
    yield my_dict


print(list_app(100000))
print(dict_app(100000))
"""
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    31     18.4 MiB     18.4 MiB           1       @profile()
    32                                             def wrapper(*args):
    33     18.4 MiB      0.0 MiB           1           start_val = time.time()
    34     23.4 MiB      5.0 MiB           1           function(*args)
    35     23.4 MiB      0.0 MiB           1           end_val = time.time()
    36     23.4 MiB      0.0 MiB           1           time_funk = end_val - start_val
    37     23.4 MiB      0.0 MiB           1           return time_funk


0.8101818561553955
Filename: F:/progekt_py/pythonProject_lgorithm_6/task_1.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    31     23.4 MiB     23.4 MiB           1       @profile()
    32                                             def wrapper(*args):
    33     23.4 MiB      0.0 MiB           1           start_val = time.time()
    34     33.5 MiB     10.0 MiB           1           function(*args)
    35     33.5 MiB      0.0 MiB           1           end_val = time.time()
    36     33.5 MiB      0.0 MiB           1           time_funk = end_val - start_val
    37     33.5 MiB      0.0 MiB           1           return time_funk


0.8231937885284424
Filename: F:/progekt_py/pythonProject_lgorithm_6/task_1.py

Процесс добавления данных в список и словарь занимает примерно одинаковое время,
при более чем двухкратной разнице в памяти. Словарь занимает значительное колличество оперативной памяти.
"""

print(list_app_gen(100000))
print(dict_app_gen(100000))

"""
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    31     33.5 MiB     33.5 MiB           1       @profile()
    32                                             def wrapper(*args):
    33     33.5 MiB      0.0 MiB           1           start_val = time.time()
    34     33.5 MiB      0.0 MiB           1           function(*args)
    35     33.5 MiB      0.0 MiB           1           end_val = time.time()
    36     33.5 MiB      0.0 MiB           1           time_funk = end_val - start_val
    37     33.5 MiB      0.0 MiB           1           return time_funk


0.0
Filename: F:/progekt_py/pythonProject_lgorithm_6/task_1.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    31     33.5 MiB     33.5 MiB           1       @profile()
    32                                             def wrapper(*args):
    33     33.5 MiB      0.0 MiB           1           start_val = time.time()
    34     33.5 MiB      0.0 MiB           1           function(*args)
    35     33.5 MiB      0.0 MiB           1           end_val = time.time()
    36     33.5 MiB      0.0 MiB           1           time_funk = end_val - start_val
    37     33.5 MiB      0.0 MiB           1           return time_funk


0.0
Filename: F:/progekt_py/pythonProject_lgorithm_6/task_1.py


Создание генераторов решает вопрос по занимаемой памяти, 
создание генератора для списка и для словаря
занимает одиннаковое время и одинаковое колличество памяти.
"""


@time_of_function
def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


print(revers_3(15544555555464444444444444444444444444444444444444666666421111111111111111111))

"""
0.0
Filename: F:/progekt_py/pythonProject_lgorithm_6/task_1.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    31     22.6 MiB     22.6 MiB           1       @profile()
    32                                             def wrapper(*args):
    33     22.6 MiB      0.0 MiB           1           start_val = time.time()
    34     22.6 MiB      0.0 MiB           1           function(*args)
    35     22.6 MiB      0.0 MiB           1           end_val = time.time()
    36     22.6 MiB      0.0 MiB           1           time_funk = end_val - start_val
    37     22.6 MiB      0.0 MiB           1           return time_funk
    
    функции хватает выделенной памяти
"""


@time_of_function
@profile
def reed_file(file):
    my_dict_1 = {}
    firm_vs_profit = {}
    firm_vs_loss = {}
    for line in file:
        firm, profit = line.split()[0], (int(line.split()[2]) - int(line.split()[3]))
        my_dict_1.setdefault(firm, profit)
        if profit > 0:
            firm_vs_profit.setdefault(firm, profit)
        else:
            firm_vs_loss.setdefault(firm, profit)
    midl_profit = {'midl_profit': (sum(my_dict_1.values()) / len(my_dict_1))}
    rezult_list = (firm_vs_profit, midl_profit, firm_vs_loss)
    print(rezult_list)
    with open('task_7.json', 'w', encoding='utf-8') as j_f:
        json.dump(rezult_list, j_f)


with open('task_7.txt', 'r', encoding="utf-8") as f:
    reed_file(f)

"""
0.0
({'firm_1': 45000, 'firm_2': 17000, 'firm_3': 2000}, {'midl_profit': 14000.0}, {'firm_4': -8000})
Filename: F:/progekt_py/pythonProject_lgorithm_6/task_1.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    88     22.6 MiB     22.6 MiB           1   @time_of_function
    89                                         @profile
    90                                         def reed_file(file):
    91     22.6 MiB      0.0 MiB           1       my_dict = {}
    92     22.6 MiB      0.0 MiB           1       firm_vs_profit = {}
    93     22.6 MiB      0.0 MiB           1       firm_vs_loss = {}
    94     22.6 MiB      0.0 MiB           5       for line in file:
    95     22.6 MiB      0.0 MiB           4           firm, profit = line.split()[0], (int(line.split()[2])
                                                                                        - int(line.split()[3]))
    96     22.6 MiB      0.0 MiB           4           my_dict.setdefault(firm, profit)
    97     22.6 MiB      0.0 MiB           4           if profit > 0:
    98     22.6 MiB      0.0 MiB           3               firm_vs_profit.setdefault(firm, profit)
    99                                                 else:
   100     22.6 MiB      0.0 MiB           1               firm_vs_loss.setdefault(firm, profit)
   101     22.6 MiB      0.0 MiB           1       midl_profit = {'midl_profit': (sum(my_dict.values()) /
                                                                                            len(my_dict))}
   102     22.6 MiB      0.0 MiB           1       rezult_list = (firm_vs_profit, midl_profit, firm_vs_loss)
   103     22.6 MiB      0.0 MiB           1       print(rezult_list)
   104     22.6 MiB      0.0 MiB           1       with open('task_7.json', 'w', encoding='utf-8') as j_f:
   105     22.6 MiB      0.0 MiB           1           json.dump(rezult_list, j_f)

Функция не требует оптимизации, программе хватает выделенной памяти.
"""
