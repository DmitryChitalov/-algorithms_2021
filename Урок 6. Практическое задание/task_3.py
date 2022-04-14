"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение
"""
from memory_profiler import profile


@profile
def reciprocate(num_in='', num_out=''):
    if num_in == '':
        try:
            num_in = int(input('Введите число для зеркалирования: '))
        except:
            return reciprocate(num_in='', num_out='')
    if num_in == 0:
        return num_out
    else:
        return reciprocate(num_in // 10, num_out + str(num_in % 10))


@profile
def call_reciprocate(num):
    return reciprocate(num)

print(reciprocate(1234567890))
print(call_reciprocate(1234567890))

'''
 При профилировании в лоб профилируется каждый вызов функции, поэтому введу специальную функцию, 
 чтобы профилировать общий вызов. Результаты одинаковы. 
 
 Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    11     18.7 MiB     18.7 MiB           1   @profile
    12                                         def reciprocate(num_in='', num_out=''):
    13     18.7 MiB      0.0 MiB           1       if num_in == '':
    14                                                 try:
    15                                                     num_in = int(input('Введите число для зеркалирования: '))
    16                                                 except:
    17                                                     return reciprocate(num_in='', num_out='')
    18     18.7 MiB      0.0 MiB           1       if num_in == 0:
    19     18.7 MiB      0.0 MiB           1           return num_out
    20                                             else:
    21                                                 return reciprocate(num_in // 10, num_out + str(num_in % 10))


Filename: D:\IT\!Study Projects\-algorithms_2021\Урок 6. Практическое задание\task_3.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    11     18.7 MiB     18.7 MiB           2   @profile
    12                                         def reciprocate(num_in='', num_out=''):
    13     18.7 MiB      0.0 MiB           2       if num_in == '':
    14                                                 try:
    15                                                     num_in = int(input('Введите число для зеркалирования: '))
    16                                                 except:
    17                                                     return reciprocate(num_in='', num_out='')
    18     18.7 MiB      0.0 MiB           2       if num_in == 0:
    19     18.7 MiB      0.0 MiB           1           return num_out
    20                                             else:
    21     18.7 MiB      0.0 MiB           1           return reciprocate(num_in // 10, num_out + str(num_in % 10))


Filename: D:\IT\!Study Projects\-algorithms_2021\Урок 6. Практическое задание\task_3.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    11     18.7 MiB     18.7 MiB           3   @profile
    12                                         def reciprocate(num_in='', num_out=''):
    13     18.7 MiB      0.0 MiB           3       if num_in == '':
    14                                                 try:
    15                                                     num_in = int(input('Введите число для зеркалирования: '))
    16                                                 except:
    17                                                     return reciprocate(num_in='', num_out='')
    18     18.7 MiB      0.0 MiB           3       if num_in == 0:
    19     18.7 MiB      0.0 MiB           1           return num_out
    20                                             else:
    21     18.7 MiB      0.0 MiB           2           return reciprocate(num_in // 10, num_out + str(num_in % 10))


Filename: D:\IT\!Study Projects\-algorithms_2021\Урок 6. Практическое задание\task_3.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    11     18.7 MiB     18.7 MiB           4   @profile
    12                                         def reciprocate(num_in='', num_out=''):
    13     18.7 MiB      0.0 MiB           4       if num_in == '':
    14                                                 try:
    15                                                     num_in = int(input('Введите число для зеркалирования: '))
    16                                                 except:
    17                                                     return reciprocate(num_in='', num_out='')
    18     18.7 MiB      0.0 MiB           4       if num_in == 0:
    19     18.7 MiB      0.0 MiB           1           return num_out
    20                                             else:
    21     18.7 MiB      0.0 MiB           3           return reciprocate(num_in // 10, num_out + str(num_in % 10))


Filename: D:\IT\!Study Projects\-algorithms_2021\Урок 6. Практическое задание\task_3.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    11     18.7 MiB     18.7 MiB           5   @profile
    12                                         def reciprocate(num_in='', num_out=''):
    13     18.7 MiB      0.0 MiB           5       if num_in == '':
    14                                                 try:
    15                                                     num_in = int(input('Введите число для зеркалирования: '))
    16                                                 except:
    17                                                     return reciprocate(num_in='', num_out='')
    18     18.7 MiB      0.0 MiB           5       if num_in == 0:
    19     18.7 MiB      0.0 MiB           1           return num_out
    20                                             else:
    21     18.7 MiB      0.0 MiB           4           return reciprocate(num_in // 10, num_out + str(num_in % 10))


Filename: D:\IT\!Study Projects\-algorithms_2021\Урок 6. Практическое задание\task_3.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    11     18.7 MiB     18.7 MiB           6   @profile
    12                                         def reciprocate(num_in='', num_out=''):
    13     18.7 MiB      0.0 MiB           6       if num_in == '':
    14                                                 try:
    15                                                     num_in = int(input('Введите число для зеркалирования: '))
    16                                                 except:
    17                                                     return reciprocate(num_in='', num_out='')
    18     18.7 MiB      0.0 MiB           6       if num_in == 0:
    19     18.7 MiB      0.0 MiB           1           return num_out
    20                                             else:
    21     18.7 MiB      0.0 MiB           5           return reciprocate(num_in // 10, num_out + str(num_in % 10))


Filename: D:\IT\!Study Projects\-algorithms_2021\Урок 6. Практическое задание\task_3.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    11     18.7 MiB     18.7 MiB           7   @profile
    12                                         def reciprocate(num_in='', num_out=''):
    13     18.7 MiB      0.0 MiB           7       if num_in == '':
    14                                                 try:
    15                                                     num_in = int(input('Введите число для зеркалирования: '))
    16                                                 except:
    17                                                     return reciprocate(num_in='', num_out='')
    18     18.7 MiB      0.0 MiB           7       if num_in == 0:
    19     18.7 MiB      0.0 MiB           1           return num_out
    20                                             else:
    21     18.7 MiB      0.0 MiB           6           return reciprocate(num_in // 10, num_out + str(num_in % 10))


Filename: D:\IT\!Study Projects\-algorithms_2021\Урок 6. Практическое задание\task_3.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    11     18.7 MiB     18.7 MiB           8   @profile
    12                                         def reciprocate(num_in='', num_out=''):
    13     18.7 MiB      0.0 MiB           8       if num_in == '':
    14                                                 try:
    15                                                     num_in = int(input('Введите число для зеркалирования: '))
    16                                                 except:
    17                                                     return reciprocate(num_in='', num_out='')
    18     18.7 MiB      0.0 MiB           8       if num_in == 0:
    19     18.7 MiB      0.0 MiB           1           return num_out
    20                                             else:
    21     18.7 MiB      0.0 MiB           7           return reciprocate(num_in // 10, num_out + str(num_in % 10))


Filename: D:\IT\!Study Projects\-algorithms_2021\Урок 6. Практическое задание\task_3.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    11     18.7 MiB     18.7 MiB           9   @profile
    12                                         def reciprocate(num_in='', num_out=''):
    13     18.7 MiB      0.0 MiB           9       if num_in == '':
    14                                                 try:
    15                                                     num_in = int(input('Введите число для зеркалирования: '))
    16                                                 except:
    17                                                     return reciprocate(num_in='', num_out='')
    18     18.7 MiB      0.0 MiB           9       if num_in == 0:
    19     18.7 MiB      0.0 MiB           1           return num_out
    20                                             else:
    21     18.7 MiB      0.0 MiB           8           return reciprocate(num_in // 10, num_out + str(num_in % 10))


Filename: D:\IT\!Study Projects\-algorithms_2021\Урок 6. Практическое задание\task_3.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    11     18.7 MiB     18.7 MiB          10   @profile
    12                                         def reciprocate(num_in='', num_out=''):
    13     18.7 MiB      0.0 MiB          10       if num_in == '':
    14                                                 try:
    15                                                     num_in = int(input('Введите число для зеркалирования: '))
    16                                                 except:
    17                                                     return reciprocate(num_in='', num_out='')
    18     18.7 MiB      0.0 MiB          10       if num_in == 0:
    19     18.7 MiB      0.0 MiB           1           return num_out
    20                                             else:
    21     18.7 MiB      0.0 MiB           9           return reciprocate(num_in // 10, num_out + str(num_in % 10))


Filename: D:\IT\!Study Projects\-algorithms_2021\Урок 6. Практическое задание\task_3.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    11     18.7 MiB     18.7 MiB          11   @profile
    12                                         def reciprocate(num_in='', num_out=''):
    13     18.7 MiB      0.0 MiB          11       if num_in == '':
    14                                                 try:
    15                                                     num_in = int(input('Введите число для зеркалирования: '))
    16                                                 except:
    17                                                     return reciprocate(num_in='', num_out='')
    18     18.7 MiB      0.0 MiB          11       if num_in == 0:
    19     18.7 MiB      0.0 MiB           1           return num_out
    20                                             else:
    21     18.7 MiB      0.0 MiB          10           return reciprocate(num_in // 10, num_out + str(num_in % 10))


0987654321

//------------------------------------------------------------------------ профилирование со спецфункцией
Filename: D:\IT\!Study Projects\-algorithms_2021\Урок 6. Практическое задание\task_3.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    24     18.7 MiB     18.7 MiB           1   @profile
    25                                         def call_reciprocate(num):
    26     18.7 MiB      0.0 MiB           1       return reciprocate(num)


0987654321

'''