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

from memory_profiler import memory_usage
import timeit
from random import choice
from string import digits


def dec(func):
    def wrapper(*args, **kwargs):
        mem1 = memory_usage()
        t1 = timeit.default_timer()
        res = func(args[0])
        mem2 = memory_usage()
        t2 = timeit.default_timer()
        mem_diff = mem2[0] - mem1[0]
        time_diff = t2 - t1
        return res, mem_diff, time_diff

    return wrapper


########################################################################################################
@dec
def SumList_orig(str):
    lst_int = []
    ext = None
    str = str.split()

    for i in str:
        if i.isdigit():
            lst_int.append(int(i))
        elif i == "q":
            ext = "q"
            return lst_int, ext
    return lst_int, ext


@dec
def SumList_gen(str):
    str = str.split()
    flag = True

    for i in str:
        if flag:
            if i.isdigit():
                yield int(i)
            elif i == "q":
                flag = False
                yield "q"
        else:
            break


@dec
def SumList_tuple(str):
    flag = True
    for i in tuple(str.split(' ')):
        if flag:
            if i.isdigit():
                yield int(i)
            elif i == "q":
                flag = False
                yield "q"
        else:
            break


str = ' '.join(choice(digits) for i in range(1000000))

my_func, mem_dif, time_dif = SumList_orig(str)
print(f"Функция SumList_orig")
print(f"Память - {mem_dif}, Время - {time_dif}")
print("_" * 100)
my_gen, mem_dif, time_dif = SumList_gen(str)
print(f"Функция SumList_gen")
print(f"Память - {mem_dif}, Время - {time_dif}")
print("_" * 100)
for i in my_gen:
    pass

my_gen, mem_dif, time_dif = SumList_tuple(str)
print(f"Функция SumList_tuple")
print(f"Память - {mem_dif}, Время - {time_dif}")
print("#" * 100)
for i in my_gen:
    pass

"""
       Функция принимает список.
       Вовращает числа, если есть q, возвращает q и останавливается

Значения первой функции
mem = 7.65234375 
time = 0.3946120000000001

Во фторой функции применяется генератор, 
скорость выполнения увеличилась и нам не нужно хранить значения в памяти
mem = 0.0 
time = 0.10860009999999987

В третьей функции к генератор добавляется кортеж вместо массива, 
скорость выполнения увеличилась и нам не нужно хранить значения в памяти
mem = 0.0 
time = 0.10775480000000015

Эффективнее всего третья функция
"""


#########################################################################################################
@dec
def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


@dec
def func_2(nums):
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            yield nums[i]


@dec
def func_3(nums):
    return tuple(i for i in nums if i % 2 == 0)


numb = list(range(10000000))

my_func, mem_dif, time_dif = func_1(numb)
print(f"Функция func_1")
print(f"Память - {mem_dif}, Время - {time_dif}")
print("_" * 100)

my_gen, mem_dif, time_dif = func_2(numb)
print(f"Функция func_2")
print(f"Память - {mem_dif}, Время - {time_dif}")
print("_" * 100)
for i in my_gen:
    pass

my_func, mem_dif, time_dif = func_3(numb)
print(f"Функция func_3")
print(f"Память - {mem_dif}, Время - {time_dif}")
print("#" * 100)

"""

Значения первой функции
mem = 193.2890625
time = 1.2038887999999996

Во фторой функции применяется генератор, 
скорость выполнения увеличилась и нам не нужно хранить значения в памяти
mem = 0.0 
time = 0.10996560000000022

В третьей функции мы формируем кортеж
скорость выполнения по сравнению с первой функцией увеличилась, память уменьшилась в разы
mem = 38.15234375
time = 0.7692568000000009

Эффективнее всего вторая функция
"""


#########################################################################################################
@dec
def sum_1(lst):
    res = 0
    for l in lst:
        for val in l:
            res += val
    return res


@dec
def sum_2(lst):
    return (sum(list(map(sum, lst))))


@dec
def sum_3(lst):
    return sum(tuple(el for i in lst for el in i))


lst = list(range(10000000))
in_list = [lst, lst, lst, lst, lst]

my_func, mem_dif, time_dif = sum_1(in_list)
print(f"Функция sum_1")
print(f"Память - {mem_dif}, Время - {time_dif}")
print("_" * 100)

my_func, mem_dif, time_dif = sum_2(in_list)
print(f"Функция sum_2")
print(f"Память - {mem_dif}, Время - {time_dif}")
print("_" * 100)

my_func, mem_dif, time_dif = sum_3(in_list)
print(f"Функция sum_3")
print(f"Память - {mem_dif}, Время - {time_dif}")
print("#" * 100)

"""

Значения первой функции
mem = -0.171875
time = 2.2334727999999995

Во фторой функции применяется встроенные функции, 
скорость выполнения увеличилась, память уменьшилась
mem = 0.00390625 
time = 1.5114512999999992

В третьей функции мы объединяем списки в один список и складываем получившийся список, 
скорость выполнения по сравнению со второй функцией уменьшилась, память увеличилась
mem = 0.01171875
time = 4.9446005

Эффективнее всего вторая функция
"""
