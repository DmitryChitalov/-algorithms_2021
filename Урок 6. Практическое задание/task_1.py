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

import copy
from sys import getrefcount
from random import randint
import memory_profiler
from timeit import default_timer
from memory_profiler import memory_usage, profile

'''Скрипт 1'''
def decor(func):
    def wrapper(*args):
        start_time = default_timer()
        m1 = memory_usage()
        res = func(*args)
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        end_time = default_timer()
        print(f'Затраты времени: {end_time - start_time} сек.')
        return res, mem_diff
    return wrapper
@decor
def lst_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


@decor
def generator_2(nums):
    return (i for i in range(len(nums)) if nums[i] % 2 == 0)


lst_p = [el for el in range(0,10000000)]
res1, mem_1 = lst_1(lst_p)
print(f"lst_1 Выполнение заняло {mem_1} Mib")
res2, mem_2 = generator_2(lst_p)
print(f"generator_2 Выполнение заняло {mem_2} Mib")

'''
Скрипт  1:
Затраты времени: 1.1529747000000001 сек.
lst_1 Выполнение заняло 193.23046875 Mib
Затраты времени: 0.21964589999999973 сек.
generator_2 Выполнение заняло 0.0 Mib

Генератор позволяет сократить память путем последовательного вывода 
данных вместо записи всех вычислений в память'''


'''Скрипт 2'''


def memory_time_profiler(func):
    def wraper(*args):
        memory = memory_usage()
        timer = default_timer()
        result = func(*args)
        memory = memory_usage()[0] - memory[0]
        timer = default_timer() - timer
        print(f'Время выполнения: {timer}\nИспользуемая память: {memory}')
        return result
    return wraper
class Complex_Number:
    @memory_time_profiler
    def __init__(self, com_num_1, com_num_2):
        self.number = complex(com_num_1, com_num_2)

    def __str__(self):
        return str(self.number)

    def __add__(self, other):
        return self.number + other.number

    def __mul__(self, other):
        return self.number * other.number
class Complex_Number_2:
    __slots__ = ('number')
    @memory_time_profiler
    def __init__(self, com_num_1, com_num_2):
        self.number = complex(com_num_1, com_num_2)

    def __str__(self):
        return str(self.number)

    def __add__(self, other):
        return self.number + other.number

    def __mul__(self, other):
        return self.number * other.number


com_num_1 = Complex_Number(42, 67)
com_num_2 = Complex_Number_2(42, 67)

'''
Скрипт 2:

Время выполнения: 0.19888139999999987
Используемая память: 0.0
Время выполнения: 0.10012409999999994
Используемая память: 0.0

Выводы по скрипту 2:
Создание слотов класса позволяет уменьшить время выполнения.
По использованию памяти разницы не заметил
'''

'''Скрипт 3'''
# Решение без оптимизации
@profile
def my_func_1():
    x = list(range(1000000))
    y = copy.deepcopy(x)
    return x

# Решение с оптимизацией
@profile
def my_func_2():
    x = list(range(1000000))
    print(getrefcount(x))
    y = copy.deepcopy(x)
    print(getrefcount(y))
    del x
    y = None
    return y
if __name__ == "__main__":
    my_func_1()
    my_func_2()

''' Скрипт 3:
Filename: D:\PyProject\first\-algorithms_2021\Урок 6. Практическое задание\task_1.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   131    599.3 MiB    599.3 MiB           1   @profile
   132                                         def my_func_1():
   133    637.9 MiB     38.6 MiB           1       x = list(range(1000000))
   134    645.6 MiB      7.7 MiB           1       y = copy.deepcopy(x)
   135    645.6 MiB      0.0 MiB           1       return x


3
3
Filename: D:\PyProject\first\-algorithms_2021\Урок 6. Практическое задание\task_1.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   138    599.9 MiB    599.9 MiB           1   @profile
   139                                         def my_func_2():
   140    638.0 MiB     38.1 MiB           1       x = list(range(1000000))
   141    638.0 MiB      0.0 MiB           1       print(getrefcount(x))
   142    647.4 MiB      9.4 MiB           1       y = copy.deepcopy(x)
   143    647.4 MiB      0.0 MiB           1       print(getrefcount(y))
   144    639.8 MiB     -7.6 MiB           1       del x
   145    601.9 MiB    -37.9 MiB           1       y = None
   146    601.9 MiB      0.0 MiB           1       return y

Удаление неиспользуемого списка позволяет сэкономить память'''




def decor_1(func):
    def wrapper(*args):
        m1 = memory_profiler.memory_usage()
        start_time = default_timer()
        result = func(*args)
        m2 = memory_profiler.memory_usage()
        mem_usage = m2[0] - m1[0]
        run_time = default_timer() - start_time
        return result, mem_usage, run_time
    return wrapper


@decor_1
def even_func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


@decor_1
def even_func_2(nums):
    new_arr = list(map(lambda x: x % 2 == 0, nums))
    return new_arr


if __name__ == '__main__':
    original_list = [randint(0, 10000) for _ in range(1000000)]
    res_1, mem_diff_1, runtime_1 = even_func_1(original_list)
    res_2, mem_diff_2, runtime_2 = even_func_2(original_list)

    print(f"Выполнение через append заняло {mem_diff_1} Mib и {runtime_1} секунд")
    print(f"Выполнение через map заняло {mem_diff_2} Mib и {runtime_2} секунд")

'''
Выполнение через append заняло 19.3828125 Mib и 0.18485479999999987 секунд
Выполнение через map заняло 7.671875 Mib и 0.20068979999999992 секунд
Функция map позволяет сократить потребление памяти,но незначительно увеличивает время
'''