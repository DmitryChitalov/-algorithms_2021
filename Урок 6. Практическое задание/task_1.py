"""
Задание 1.

Выполните профилирование памяти в скриптах.
Проанализируйте результат и определите программы с
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
from memory_profiler import profile
import random
import functools

#Пример 1

print("Задача 5. Генерация списка из четных цифр от 100 до 1000001 и перемножение всех элементов.")


@profile
def my_func():
    my_list = [i for i in range(100,100001) if i % 2 == 0]
    #print(f"Исходный список из четных элементов от 100 до 1000001\n{my_list}")
    def my_func_comp(prev_el, el):
        return prev_el*el
    return functools.reduce(my_func_comp, my_list)#print(functools.reduce(my_func_comp, my_list))


@profile
def my_func_ver2():
    def calc_my_list():
        my_list = []
        for i in range(100,100001):
            if i % 2 == 0:
                yield i
    #print(f"Исходный список из четных элементов от 100 до 1000001\n{my_list}")
    def my_func_comp(prev_el, el):
        return prev_el*el
    return functools.reduce(my_func_comp, calc_my_list())#print(functools.reduce(my_func_comp, calc_my_list()))

my_func()
my_func_ver2()

"""
Вывод
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    64     25.7 MiB     25.7 MiB           1   @profile
    65                                         def my_func():
    66     27.6 MiB  -3211.6 MiB       99904       my_list = [i for i in range(100,100001) if i % 2 == 0]
    67     27.6 MiB      0.0 MiB           1       print(f"Исходный список из четных элементов от 100 до 1000\n{my_list}")
    68     28.3 MiB  -2414.9 MiB       49951       def my_func_comp(prev_el, el):
    69     28.3 MiB  -1540.7 MiB       49950           return prev_el*el
    70     28.3 MiB      0.0 MiB           1       return functools.reduce(my_func_comp, my_list)


Filename: C:/Users/miair/PycharmProjects/-algorithms_2021/Урок 6. Практическое задание/task_1.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    76     26.5 MiB     26.5 MiB           1   @profile
    77                                         def my_func_ver2():
    78     26.5 MiB      0.0 MiB           2       def calc_my_list():
    79     26.5 MiB      0.0 MiB           1           my_list = []
    80     26.5 MiB -14613.8 MiB       99902           for i in range(100,100001):
    81     26.5 MiB -14614.2 MiB       99901               if i % 2 == 0:
    82     26.5 MiB -14613.9 MiB       99902                   yield i
    83                                             #print(f"Исходный список из четных элементов от 100 
                                                                                    до 1000\n{my_list}")
    84     26.5 MiB  -7540.8 MiB       49951       def my_func_comp(prev_el, el):
    85     26.5 MiB  -7140.8 MiB       49950           return prev_el*el
    86     26.4 MiB     -0.1 MiB           1       return functools.reduce(my_func_comp, calc_my_list())
Заменил создание списка целиком через итератор генератором с yield, возвращающим по 1 элементу, удовлетворяющему                            
условию задачи, для дальнейших расчетов. Это и дало экономию памяти
"""


#Пример 2


print("Задача 2. Создать не программно файл, сохранить в нем несколько строк, считать эти строки,\n"
      "вывести количество строк и количество символов в каждой строке.\n")


@profile
def calc_words():
    with open("task-2.txt", "r", encoding = "utf-8") as f_obj:
        my_str = f_obj.read()
        #print(my_str)
        f_obj.seek(0)
        for my_str in f_obj:
            f_obj.seek(0)
            my_str = f_obj.readlines()
        print(f"Количество строк в файле: {len(my_str)}")
        for i in range(len(my_str)):
            tmp_str = my_str[i].split()
            print(f"Количество слов в {i+1} строке: {len(tmp_str)}")
    return

@profile
def calc_words_ver2():
    with open("task-2.txt", "r", encoding = "utf-8") as f_obj:
        for my_str in f_obj:
            f_obj.seek(0)
            my_str = f_obj.readlines()
        print(f"Количество строк в файле: {len(my_str)}")
        for i in range(len(my_str)):
            tmp_str = my_str[i].split()
            print(f"Количество слов в {i+1} строке: {len(tmp_str)}")
        del my_str
    return

calc_words()
calc_words_ver2()

"""
Вывод

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    98     25.7 MiB     25.7 MiB           1   @profile
    99                                         def calc_words():
   100     25.7 MiB      0.0 MiB           1       with open("task-2.txt", "r", encoding = "utf-8") as f_obj:
   101     30.0 MiB      4.3 MiB           1           my_str = f_obj.read()
   102                                                 #print(my_str)
   103     30.0 MiB      0.0 MiB           1           f_obj.seek(0)
   104     31.4 MiB     -4.3 MiB           2           for my_str in f_obj:
   105     25.8 MiB      0.0 MiB           1               f_obj.seek(0)
   106     31.4 MiB      5.7 MiB           1               my_str = f_obj.readlines()
   107     31.4 MiB      0.0 MiB           1           print(f"Количество строк в файле: {len(my_str)}")
   108     31.5 MiB   -434.0 MiB       10066           for i in range(len(my_str)):
   109     31.5 MiB   -434.0 MiB       10065               tmp_str = my_str[i].split()
   110                                                     #print(f"Количество слов в {i+1} строке: {len(tmp_str)}")
   111     31.4 MiB     -0.0 MiB           1       return


Количество строк в файле: 10065
Filename: C:/Users/miair/PycharmProjects/-algorithms_2021/Урок 6. Практическое задание/task_1.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   113     26.7 MiB     26.7 MiB           1   @profile
   114                                         def calc_words_ver2():
   115     26.7 MiB      0.0 MiB           1       with open("task-2.txt", "r", encoding = "utf-8") as f_obj:
   116     31.4 MiB      0.0 MiB           2           for my_str in f_obj:
   117     26.8 MiB      0.0 MiB           1               f_obj.seek(0)
   118     31.4 MiB      4.6 MiB           1               my_str = f_obj.readlines()
   119     31.4 MiB      0.0 MiB           1           print(f"Количество строк в файле: {len(my_str)}")
   120     31.4 MiB   -133.4 MiB       10066           for i in range(len(my_str)):
   121     31.4 MiB   -133.3 MiB       10065               tmp_str = my_str[i].split()
   122                                                     #print(f"Количество слов в {i+1} строке: {len(tmp_str)}")
   123     27.0 MiB     -4.4 MiB           1           del my_str
   124     27.0 MiB      0.0 MiB           1       return

Удалось освободить память за счет удаления переменной, в которую были считаны данные из файла
"""

#Пример 3
"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
"""
@profile
def help_func(count):
    def calc(count,n=None):
        if n is None:
            n = 1
        #print(n)
        if count == 0:
            return n
        else:
            count -= 1
        return n+calc(count,n/2*(-1))
    print(f'Сумма чисел в последовательности составит {calc(count - 1)}')

count = 600

help_func(count)

@profile
def calc_ver2(count):
    n = 1
    summa = 0
    i = 0
    while i <= count:
        summa = summa + n
        n = n/2*(-1)
        i += 1
    return summa


print(f'Сумма чисел в последовательности составит {calc_ver2(count - 1)}')

"""
Вывод:
Сумма чисел в последовательности составит 0.6666666666666666
Filename: C:/Users/miair/PycharmProjects/-algorithms_2021/Урок 6. Практическое задание/task_1.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   212     26.0 MiB     26.0 MiB           1   @profile
   213                                         def help_func(count):
   214     26.9 MiB     -2.7 MiB         601       def calc(count,n=None):
   215     26.9 MiB     -3.6 MiB         600           if n is None:
   216     26.0 MiB      0.0 MiB           1               n = 1
   217                                                 #print(n)
   218     26.9 MiB     -4.4 MiB         600           if count == 0:
   219     26.9 MiB      0.0 MiB           1               return n
   220                                                 else:
   221     26.9 MiB     -3.7 MiB         599               count -= 1
   222     26.9 MiB      0.0 MiB         599           return n+calc(count,n/2*(-1))
   223     26.9 MiB      0.0 MiB           1       print(f'Сумма чисел в последовательности составит {calc(count - 1)}')


Filename: C:/Users/miair/PycharmProjects/-algorithms_2021/Урок 6. Практическое задание/task_1.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   229     26.9 MiB     26.9 MiB           1   @profile
   230                                         def calc_ver2(count):
   231     26.9 MiB      0.0 MiB           1       n = 1
   232     26.9 MiB      0.0 MiB           1       summa = 0
   233     26.9 MiB      0.0 MiB           1       i = 0
   234     26.9 MiB      0.0 MiB         601       while i <= count:
   235     26.9 MiB      0.0 MiB         600           summa = summa + n
   236     26.9 MiB      0.0 MiB         600           n = n/2*(-1)
   237     26.9 MiB      0.0 MiB         600           i += 1
   238     26.9 MiB      0.0 MiB           1       return summa


Сумма чисел в последовательности составит 0.6666666666666667

Process finished with exit code 0

Было интересно третьим вариантом попробовать замену рекурсии простым циклом. 
Пробовал переделать разные задачи из урока 2, но везде был такой же результат -
при старте функция с рекурсией занимаем меньше памяти, чем функция со списком. 
Но при этом функция со списком, даже при подстановке бОльших значений, больше
изначально занятой памяти не занимает. А вот функция с рекурсией, изначально  
замимая меньше места, в процессе работы выбирает дополнительное место из па-
мяти. 

"""

