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
from memory_profiler import profile
from random import randint


@profile()
def my_min1(z):
    return print('myMin1:', min(z))      #O(1)


@profile()
def my_min2(z):
    s = [z[a] for a in range(len(z)) if z[a] == min(z)]
    return print('myMin2:', s[:1])      #O(1)


@profile()
def my_min3(z):
    s = 0                           #O(1)
    for x in range(len(z)):         #O(n)
        if z[x] > s:                #O(1)
            s = z[x]                #O(1)
    for a in range(len(z)):         #O(n)
        if z[a] < s:                #O(1)
            s = z[a]                #O(1)
    return print('myMin3:', s)      #O(1)


@profile()
def my_min4(f):
    f.sort()                                #0(n log n)
    return print('myMin4:', f.pop(0))       #O(1)


z = [randint(1, 1000) for i in range(10000)]  #O(1)

my_min1(z) #O(1)
my_min2(z) #O(1)
my_min3(z) #O(1)
my_min4(z) #O(1)

"""
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    22     19.0 MiB     19.0 MiB           1   @profile()
    23                                         def my_min1(z):
    24     19.0 MiB      0.0 MiB           1       return print('myMin1:', min(z))      #O(1)


myMin2: [1]
Filename: C:\Users\User\Downloads\Урок 3. Коды примеров\Урок 3. Коды примеров\111.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    27     19.0 MiB     19.0 MiB           1   @profile()
    28                                         def my_min2(z):
    29     19.0 MiB      0.0 MiB       10003       s = [z[a] for a in range(len(z)) if z[a] == min(z)]
    30     19.0 MiB      0.0 MiB           1       return print('myMin2:', s[:1])      #O(1)


myMin3: 1
Filename: C:\Users\User\Downloads\Урок 3. Коды примеров\Урок 3. Коды примеров\111.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    33     19.0 MiB     19.0 MiB           1   @profile()
    34                                         def my_min3(z):
    35     19.0 MiB      0.0 MiB           1       s = 0                           #O(1)
    36     19.0 MiB      0.0 MiB       10001       for x in range(len(z)):         #O(n)
    37     19.0 MiB      0.0 MiB       10000           if z[x] > s:                #O(1)
    38     19.0 MiB      0.0 MiB           9               s = z[x]                #O(1)
    39     19.0 MiB      0.0 MiB       10001       for a in range(len(z)):         #O(n)
    40     19.0 MiB      0.0 MiB       10000           if z[a] < s:                #O(1)
    41     19.0 MiB      0.0 MiB          11               s = z[a]                #O(1)
    42     19.0 MiB      0.0 MiB           1       return print('myMin3:', s)      #O(1)


myMin4: 1
Filename: C:\Users\User\Downloads\Урок 3. Коды примеров\Урок 3. Коды примеров\111.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    45     19.0 MiB     19.0 MiB           1   @profile()
    46                                         def my_min4(f):
    47     19.1 MiB      0.0 MiB           1       f.sort()                                #0(n log n)
    48     19.1 MiB      0.0 MiB           1       return print('myMin4:', f.pop(0))       #O(1)



    
=========================================================
далее идут запуски из отдельных файлов для сравнения
========================================================




myMin1: 1
Filename: C:\Users\User\Downloads\Урок 3. Коды примеров\Урок 3. Коды примеров\115.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
     5     18.9 MiB     18.9 MiB           1   @profile()
     6                                         def my_min1(z):
     7     18.9 MiB      0.0 MiB           1       return print('myMin1:', min(z))      #O(1)
     
myMin2: [1]
Filename: C:\Users\User\Downloads\Урок 3. Коды примеров\Урок 3. Коды примеров\112.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
     5     19.1 MiB     19.1 MiB           1   @profile()
     6                                         def my_min2(z):
     7     19.1 MiB      0.0 MiB       10003       s = [z[a] for a in range(len(z)) if z[a] == min(z)]
     8     19.1 MiB      0.0 MiB           1       return print('myMin2:', s[:1])      #O(1)
     
myMin3: 1
Filename: C:\Users\User\Downloads\Урок 3. Коды примеров\Урок 3. Коды примеров\113.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
     5     19.2 MiB     19.2 MiB           1   @profile()
     6                                         def my_min3(z):
     7     19.2 MiB      0.0 MiB           1       s = 0                           #O(1)
     8     19.2 MiB      0.0 MiB       10001       for x in range(len(z)):         #O(n)
     9     19.2 MiB      0.0 MiB       10000           if z[x] > s:                #O(1)
    10     19.2 MiB      0.0 MiB           5               s = z[x]                #O(1)
    11     19.2 MiB      0.0 MiB       10001       for a in range(len(z)):         #O(n)
    12     19.2 MiB      0.0 MiB       10000           if z[a] < s:                #O(1)
    13     19.2 MiB      0.0 MiB           7               s = z[a]                #O(1)
    14     19.2 MiB      0.0 MiB           1       return print('myMin3:', s)      #O(1)
    
myMin4: 1
Filename: C:\Users\User\Downloads\Урок 3. Коды примеров\Урок 3. Коды примеров\114.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
     5     19.2 MiB     19.2 MiB           1   @profile()
     6                                         def my_min4(f):
     7     19.2 MiB      0.0 MiB           1       f.sort()                                #0(n log n)
     8     19.2 MiB      0.0 MiB           1       return print('myMin4:', f.pop(0))       #O(1)
     
вывод: не удалось убедительно выйти за диапазон выделенной памяти чтобы получить прирост инкремента,
но вариант с использованием встроенной функции дал лучший показатель по скорости и при выполнении в отдельном файле
использовал меньше памяти
"""
