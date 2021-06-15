import sys
from memory_profiler import profile


@profile
def func():
    """
    В одномерном массиве целых чисел определить два наименьших элемента.
    Они могут быть как равны между собой (оба являться минимальными),
    так и различаться.
    """

    a = list(range(500000))

    min_num = a[0]
    min_num2 = a[1]

    if min_num > min_num2:
        min_num, min_num2 = min_num2, min_num

    for i in range(len(a)):
        if a[i] < min_num:
            min_num2 = min_num
            min_num = a[i]
        elif a[i] < min_num2:
            min_num2 = a[i]
    del a
    print("Два наименьших элемента:", min_num, min_num2)
    print(f"Два наименьших элемента: {min_num}, {min_num2}")


func()

'''
Для запуска программы было выделено 13.5 MiB.
При создании списка "a" было выделено еще 9.6 MiB.
После выполнения программы удалил список "a" , тем самым
освободил память (9.6 MiB).
Line #    Mem usage    Increment   Line Contents
================================================
    16     13.5 MiB     13.5 MiB   @profile
    17                             def func():
    18     23.1 MiB      9.6 MiB       a = list(range(500000))
    19
    20     23.1 MiB      0.0 MiB       min_num = a[0]
    21     23.1 MiB      0.0 MiB       min_num2 = a[1]
    22
    23     23.1 MiB      0.0 MiB       if min_num > min_num2:
    24                                     min_num, min_num2 
                                            = min_num2, min_num
    25
    26     23.2 MiB      0.0 MiB       for i in range(len(a)):
    27     23.2 MiB      0.0 MiB           if a[i] < min_num:
    28                                         min_num2 = min_num
    29                                         min_num = a[i]
    30     23.2 MiB      0.0 MiB           elif a[i] < min_num2:
    31     23.1 MiB      0.0 MiB               min_num2 = a[i]
    32
    33     23.2 MiB      0.0 MiB       print("Два наименьших элемента:", 
                                                    min_num, min_num2)
    34     13.8 MiB      0.0 MiB       del a
'''
