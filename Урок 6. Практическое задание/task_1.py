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

from sys import getrefcount
from memory_profiler import profile, memory_usage
import gc
from timeit import default_timer


#Функция, позволяющая сохранить в массиве индексы четных элементов другого массива
@profile
def even_1(num):
    new_arr = []
    for i in range(len(num)):
        if num[i] % 2 == 0:
            new_arr.append(i)
    return new_arr

@profile
def even_2(num):
    new_arr = filter(lambda i: num[i] % 2 == 0, range(len(num)))
    return new_arr


num_1 = [el for el in range(1000000)]

#Результаты замера памяти функции even_1()
#Line #    Mem usage    Increment  Occurences   Line Contents
#============================================================
#   32     57.8 MiB     57.8 MiB           1   @profile
#    33                                         def even_1(num):
#    34     57.8 MiB      0.0 MiB           1       new_arr = []
#    35     77.7 MiB -17096.4 MiB     1000001       for i in range(len(num)):
#    36     77.7 MiB -17080.9 MiB     1000000           if num[i] % 2 == 0:
#    37     77.7 MiB  -8543.5 MiB      500000               new_arr.append(i)
#    38     77.7 MiB      0.0 MiB           1       return new_arr

#Результаты замера памяти функции even_2()
#Line #    Mem usage    Increment  Occurences   Line Contents
#============================================================
#    40     58.6 MiB     58.6 MiB           1   @profile
#    41                                         def even_2(num):
#    42     58.6 MiB      0.0 MiB           1       new_arr = filter(lambda i: num[i] % 2 == 0, range(len(num)))
#    43     58.6 MiB      0.0 MiB           1       return new_arr


#Вывод: функция even_1(num) использует значительно больше памяти ввиду наличия большего количества ссылок на переменные.
#Оптимизация данной функции может быть за счет применения генератора вместо цикла for.

#Функция, формирующая из введенного числа обратное по порядку входящих в него цифр.

@profile
def revers_1(enter_num):
    simple_list = list(str(enter_num))
    simple_list.reverse()
    revers_num = "".join(simple_list)
    return revers_num

num_2 = [el for el in range(1000000)]

@profile
def revers_2(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num



#Результаты замера памяти функции revers_2()
#Line #    Mem usage    Increment  Occurences   Line Contents
#============================================================
#    69     57.8 MiB     57.8 MiB           1   @profile
#    70                                         def revers_1(enter_num):
#    71     65.4 MiB      7.5 MiB           1       enter_num = str(enter_num)
#    72     72.9 MiB      7.5 MiB           1       revers_num = enter_num[::-1]
#    73     72.9 MiB      0.0 MiB           1       return revers_num

#Результаты замера памяти функции revers_1()
#Line #    Mem usage    Increment  Occurences   Line Contents
#============================================================
#    75     57.9 MiB     57.9 MiB           1   @profile
#    76                                         def revers_2(enter_num):
#    77    118.0 MiB     60.2 MiB           1       simple_list = list(str(enter_num))
#    78    118.0 MiB      0.0 MiB           1       simple_list.reverse()
#    79    125.6 MiB      7.5 MiB           1       revers_num = "".join(simple_list)
#   80    125.6 MiB      0.0 MiB           1       return revers_num

#Вывод: вариант применения функции revers_2() является более предпочтительным с точки зрения используемой памяти ввиду
#наличия большего количества ссылок на переменные. Оптимизировать можно применением вместо
# простого списка simple_list = list(str(enter_num)) numpy array

#Функция, реализующая алгоритм поиска числа, которое встречается в массиве чаще всего.

def decor(func):
    def wrapper(*args, **kwargs):
        m1 = memory_usage()
        start = default_timer()
        res = func(*args, **kwargs)
        end = default_timer()
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        time_diff = end - start
        return res, f'Время замера составляет {time_diff}', f'Память составляет {mem_diff}'
    return wrapper

array = [el for el in range(50000)]

@decor
def frequent_1():
    max_3 = max(array, key = array.count)
    count = array.count(max_3)
    return f'Чаще всего встречается число {max_3}, ' \
           f'оно появилось в массиве {count} раз(а)'

@decor
def frequent_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'

#Результаты замера памяти функции frequent_1()
#('Чаще всего встречается число 0, оно появилось в массиве 1 раз(а)', 'Время замера составляет 19.506253400000002',
# 'Память составляет 0.00390625')
#Результаты замера памяти функции frequent_2()
#('Чаще всего встречается число 0, оно появилось в массиве 1 раз(а)', 'Время замера составляет 19.4511004',
# 'Память составляет 0.05078125')

#Выводы: несмотря на то, что скорость выполнения двух функций сопоставимая, функция frequent_2() расходует более чем в
#10 раз больше памяти. При анализе можно увидеть, что функция frequent_2() иммеет значительно большее количество ссылок
#на основную переменную array а также большее количество операций с данной переменной. Оптимизация может быть достигнута
#в результате применения numpy array, замены цикла на генератор.


if __name__ == '__main__':
    even_1(num_1)
    even_2(num_1)
    revers_1(num_2)
    revers_2(num_2)
    print(frequent_1())
    print(frequent_2())