"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение
"""
from memory_profiler import profile
import math

@profile
def reverse_num(numb):
    def revers_number(num):
        if num == 0:
            return ''
        else:
            return str(num % 10) + revers_number(num // 10)

    return revers_number(numb)

@profile
def reverse_num_1(numb):
    def revers_number_1(number):
        if number == 0:
            return ''
        else:
            return str(number % 10) + revers_number_1(number // 10)

    return lambda: revers_number_1(numb)



reverse_num(math.factorial(400))
reverse_num_1(math.factorial(400))

'''
Need additional wrapper function for recursive function.
To avoid tail calls, you simply wrap all tail calls in lambda.

Нужна дополнительная оболочка-функция для рекурсивной функции.
Чтобы избежать хвостовых вызовов, вы просто оборачиваете все хвостовые вызовы в lambda.
'''
'''
C:\Users\79115\AppData\Local\Programs\Python\Python39\python.exe "C:/Users/79115/Desktop/2 Урок Алгоритмы/Урок 2. Коды примеров/Algorithm6.3.py"
Filename: C:\Users\79115\Desktop\2 Урок Алгоритмы\Урок 2. Коды примеров\Algorithm6.3.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
     4     19.3 MiB     19.3 MiB           1   @profile
     5                                         def reverse_num(numb):
     6     21.3 MiB      1.8 MiB         871       def revers_number(num):
     7     21.3 MiB      0.2 MiB         870           if num == 0:
     8     21.3 MiB      0.0 MiB           1               return ''
     9                                                 else:
    10     21.3 MiB      0.0 MiB         869               return str(num % 10) + revers_number(num // 10)
    11                                         
    12     21.3 MiB      0.0 MiB           1       return revers_number(numb)


Filename: C:\Users\79115\Desktop\2 Урок Алгоритмы\Урок 2. Коды примеров\Algorithm6.3.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    14     21.3 MiB     21.3 MiB           1   @profile
    15                                         def reverse_num_1(numb):
    16     21.3 MiB      0.0 MiB           1       def revers_number_1(number):
    17                                                 if number == 0:
    18                                                     return ''
    19                                                 else:
    20                                                     return str(number % 10) + revers_number_1(number // 10)
    21                                         
    22     21.3 MiB      0.0 MiB           1       return lambda: revers_number_1(numb)



Process finished with exit code 0


'''

