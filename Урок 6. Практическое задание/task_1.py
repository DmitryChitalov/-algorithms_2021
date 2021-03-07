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

Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage + из memory_profiler
С одновременным замером времени (timeit.default_timer())!
"""

from memory_profiler import memory_usage, profile
import timeit
from functools import reduce


# скрипт 1 скрипт вернёт сумму двух наибольших чисел из трёх


@profile
def sum_num_1():
    my_list = [700, 300, 900]
    my_list.remove(min(my_list))
    return sum(my_list)


@profile
def sum_num_2():
    my_list = [700, 300, 900]
    result = sum(sorted(my_list)[1:])
    del my_list
    return result


@profile
def sum_num_3():
    my_list = list(range(500000))
    num_1 = 0
    num_2 = 0

    for i in my_list:
        if i > num_1:
            num_1 = i
    for i in my_list:
        if i > num_2 and i != num_1:
            num_2 = i
    del my_list
    return num_1 + num_2


if __name__ == '__main__':
    sum_num_1()
    sum_num_2()
    sum_num_3()

'''
Для запуска программы выделено 17.5 MiB
При создании списка my_list выделелось ещё 0.0 MiB
Как мы видим в Increment везде ноль кроме старта. Нет дополнительных
растрат памяти.
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    46     17.4 MiB     17.4 MiB           1   @profile
    47                                         def sum_num_1():
    48     17.4 MiB      0.0 MiB           1           my_list = [700, 300, 900]
    49     17.4 MiB      0.0 MiB           1           my_list.remove(min(my_list))
    50     17.4 MiB      0.0 MiB           1           return sum(my_list)
Смотрим на результаты работы моего декоратора измерителя и видим что

Для запуска программы выделено 17.5 MiB
При создании списка my_list выделелось ещё 0.0 MiB
Как мы видим в Increment везде ноль кроме старта. Нет дополнительных
растрат памяти. Удаление списка после использования не привело к освобождению
памяти. Отсюда вывод если объект малого размера например список, то на
память влиять нет смысла, но можно удалить ненужные ссылки на объект.
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    54     17.5 MiB     17.5 MiB           1   @profile
    55                                         def sum_num_2():
    56     17.5 MiB      0.0 MiB           1       my_list = [700, 300, 900]
    57     17.5 MiB      0.0 MiB           1       result = sum(sorted(my_list)[1:])
    58     17.5 MiB      0.0 MiB           1       del my_list
    59     17.5 MiB      0.0 MiB           1       return result
Смотрим на результаты работы моего декоратора измерителя и видим что

В третьем скрипте нагрузим наш список суть программы будет та же, но программа
будет выбирать 2 максимальных числа не из трёх, а более колличества чисел.
Для запуска программы выделено 17.6 MiB
При создании списка my_list выделелось ещё 19.3 MiB
После выполнения программы удалил список my_list этим освободил 19.0 MiB.
И так мы видим что есть смысл освобождать память если спискок или другой
объект большой по колличеству данных.
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    63     17.6 MiB     17.6 MiB           1   @profile
    64                                         def sum_num_3():
    65     36.9 MiB     19.3 MiB           1       my_list = list(range(500000))
    66     36.9 MiB      0.0 MiB           1       num_1 = 0
    67     36.9 MiB      0.0 MiB           1       num_2 = 0
    68                                             
    69     36.9 MiB      0.0 MiB      500001       for i in my_list:
    70     36.9 MiB      0.0 MiB      500000           if i > num_1:
    71     36.9 MiB      0.0 MiB      499999               num_1 = i
    72     36.9 MiB      0.0 MiB      500001       for i in my_list:
    73     36.9 MiB      0.0 MiB      500000           if i > num_2 and i != num_1:
    74     36.9 MiB      0.0 MiB      499998               num_2 = i
    75     17.9 MiB    -19.0 MiB           1       del my_list
    76     17.9 MiB      0.0 MiB           1       return num_1 + num_2
'''


# скрипт 2 реверс числа


@profile
def revers_num_1(num):
    quotient = num // 10
    mudulo = num % 10
    if quotient == 0:
        return str(mudulo)
    else:
        return str(mudulo) + str(revers_num_1(quotient))


@profile
def revers_num_2():
    num = 43848347347347374347378473478374384834734734737434737847347837
    my_list = reversed(list(str(num)))
    result = reduce(lambda x, y: x + y, my_list)
    del num
    del my_list
    return result


@profile
def revers_num_3():
    num = 43848347347347374347378473478374384834734734737434737847347837
    return str(num)[::-1]


if __name__ == '__main__':
    revers_num_1(4384834734734737)
    revers_num_2()
    revers_num_3()

'''
Выдилилось памяти 17.6 MiB.
Профилирование памяти у рекурсии приводит к тому что эта таблица запустилась
15 раз для числа 4384834734734737. Видимо в соответствии с рекурсивным вызовом
функции. В Increment quotient = num // 10 выделяется 0.1 MiB каждом вызове что
не является существенным для памяти. К тому же ссылки используются при return
и их не следует удалять. Так же рекурсия требует чуть больше памяти так как при её
работе хранится стек вызовов.
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   150     17.6 MiB     17.5 MiB          16   @profile
   151                                         def revers_num_1(num):
   152     17.6 MiB      0.1 MiB          16       quotient = num // 10
   153     17.6 MiB      0.0 MiB          16       mudulo = num % 10
   154     17.6 MiB      0.0 MiB          16       if quotient == 0:
   155     17.6 MiB      0.0 MiB           1           return str(mudulo)
   156                                             else:
   157     17.6 MiB      0.0 MiB          15           return str(mudulo) + str(revers_num_1(quotient))

Для запуска программы выделено 17.5 MiB
При создании списка my_list не выделилась доп память
После выполнения программы удалил ненужные ссылки что не повлияло на
память. Использование большого числа тоже неповлияло на память.
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   161     17.5 MiB     17.5 MiB           1   @profile
   162                                         def revers_num_2():
   163     17.5 MiB      0.0 MiB           1       num = 43848347347347374347378473478374384834734734737434737847347837
   164     17.5 MiB      0.0 MiB           1       my_list = reversed(list(str(num)))
   165     17.5 MiB      0.0 MiB         123       result = reduce(lambda x,y: x+y, my_list)
   166     17.5 MiB      0.0 MiB           1       del num
   167     17.5 MiB      0.0 MiB           1       del my_list
   168     17.5 MiB      0.0 MiB           1       return result

Для запуска программы выделено 17.5 MiB.
Дополнительно памяти не было выделено.
В скрипте нет ссылок которые стоит удалить. Удалять что-то для освобождения
памяти не требуется.
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   171     17.5 MiB     17.5 MiB           1   @profile
   172                                         def revers_num_3():
   173     17.5 MiB      0.0 MiB           1       num = 43848347347347374347378473478374384834734734737434737847347837
   174     17.5 MiB      0.0 MiB           1       return str(num)[::-1]
'''


# скрипт 3 находим минимальное число


@profile
def min_num_1():
    my_list = list(range(500000))

    result = my_list[-1]
    count = 0
    for el_1 in my_list:
        for el_2 in my_list:
            if el_1 >= el_2 and result > el_2:
                result = el_2
        count = 1
        if count == 1:
            break
    del el_1
    del el_2
    del my_list
    return result


@profile
def min_num_2():
    my_list = list(range(500000))

    result = my_list[0]
    for i in my_list:
        if result >= i:
            result = i
    del i
    del my_list
    return result


@profile
def min_num_3():
    my_tup = tuple(range(500000))
    result = reduce(lambda x, y: x if x < y else y, my_tup[1:], my_tup[0])
    del my_tup
    return result


if __name__ == '__main__':
    min_num_1()
    min_num_2()
    min_num_3()

'''
Для запуска программы выделено 17.5 MiB
При создании списка my_list выделелось ещё 19.3 MiB
После выполнения программы удалил список my_list этим освободил 19.1 MiB
Также удалил ненужные ссылки
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   156     17.5 MiB     17.5 MiB           1   @profile
   157                                         def min_num_1():
   158     36.8 MiB     19.3 MiB           1       my_list = list(range(500000))
   159                                             
   160     36.8 MiB      0.0 MiB           1       result = my_list[-1]
   161     36.8 MiB      0.0 MiB           1       count = 0
   162     36.8 MiB      0.0 MiB           1       for el_1 in my_list:
   163     36.8 MiB      0.0 MiB      500001           for el_2 in my_list: 
   164     36.8 MiB      0.0 MiB      500000               if el_1 >= el_2 and result > el_2:
   165     36.8 MiB      0.0 MiB           1                   result = el_2
   166     36.8 MiB      0.0 MiB           1           count = 1
   167     36.8 MiB      0.0 MiB           1           if count == 1:
   168     36.8 MiB      0.0 MiB           1               break
   169     36.8 MiB      0.0 MiB           1       del el_1
   170     36.8 MiB      0.0 MiB           1       del el_2
   171     17.8 MiB    -19.1 MiB           1       del my_list
   172     17.8 MiB      0.0 MiB           1       return result

Для запуска программы выделено 17.6 MiB
При создании списка my_list выделелось ещё 19.3 MiB
После выполнения программы удалил список my_list этим освободил 19.0 MiB
Также удалил ненужные ссылки
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   173     17.6 MiB     17.6 MiB           1   @profile
   174                                         def min_num_2():
   175     36.9 MiB     19.3 MiB           1       my_list = list(range(500000))
   176                                         
   177     36.9 MiB      0.0 MiB           1       result = my_list[0]
   178     36.9 MiB      0.0 MiB      500001       for i in my_list:
   179     36.9 MiB      0.0 MiB      500000           if result >= i:
   180     36.9 MiB      0.0 MiB           1               result = i
   181     36.9 MiB      0.0 MiB           1       del i
   182     17.9 MiB    -19.0 MiB           1       del my_list
   183     17.9 MiB      0.0 MiB           1       return result

Для запуска программы выделено 17.5 MiB
При создании кортежа выделелось ещё 19.3 MiB
После выполнения программы удалил кортеж этим освободил 22.6 MiB
Я испоьзовал кортеж потому что он должен быть эффективнее в работе с памятью.
Правда размер в итоге у списка и кортежа оказался одинаковым.
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   187     17.5 MiB     17.5 MiB           1   @profile
   188                                         def min_num_3():
   189     36.8 MiB     19.3 MiB           1       my_tup = tuple(range(500000))
   190     40.4 MiB      0.0 MiB      999999       result = reduce(lambda x,y: x if x < y else y, my_tup[1:], my_tup[0])
   191     17.8 MiB    -22.6 MiB           1       del my_tup
   192     17.8 MiB      0.0 MiB           1       return result
'''


# напишем декоратор, который будет измерять память и время выполнения

def decor_meter(func):
    def wrap(*args):
        start = timeit.default_timer()
        mem_1 = memory_usage()
        func(args[0])
        mem_2 = memory_usage()
        end = timeit.default_timer()
        mem_differ = mem_2[0] - mem_1[0]
        time_differ = end - start
        return mem_differ, time_differ

    return wrap


@decor_meter
def sum_num_4(*args):
    my_list = list(range(500000))
    num_1 = 0
    num_2 = 0

    for i in my_list:
        if i > num_1:
            num_1 = i
    for i in my_list:
        if i > num_2 and i != num_1:
            num_2 = i
    del my_list
    return num_1 + num_2


mem_diff, time = sum_num_4(0, 0)
print(f'Выполнение заняло: {mem_diff} MiB, {time} time')

'''
Есть небольшие издержки памяти, которые не пофиксились удалением ссылки на список
Время выполнения быстрое для списка.
Выполнение заняло: 0.3359375 MiB, 0.3076682209975843 time
'''


@decor_meter
def revers_num_4(num):
    my_list = reversed(list(str(num)))
    result = reduce(lambda x, y: x + y, my_list)
    del num
    del my_list
    return result


mem_diff, time = revers_num_4(43848347347347374347378473478374384834734734737434737847347837)
print(f'Выполнение заняло: {mem_diff} MiB, {time} time')

'''
Излишков памяти нет, использование встроенных функций хорошо сказывается
на скорости работы скрипта.
Выполнение заняло: 0.0 MiB, 0.20080745900122565 time
'''


@decor_meter
def min_num_4(*args):
    my_list = list(range(500000))

    result = my_list[-1]
    count = 0
    for el_1 in my_list:
        for el_2 in my_list:
            if el_1 >= el_2 and result > el_2:
                result = el_2
        count = 1
        if count == 1:
            break
    del el_1
    del el_2
    del my_list
    return result


mem_diff, time = revers_num_4(0, 0)
print(f'Выполнение заняло: {mem_diff} MiB, {time} time')

'''
Излишков памяти нет, скорость выполнения быстрая.
Выполнение заняло: 0.0 MiB, 0.2012890910009446 time
'''
