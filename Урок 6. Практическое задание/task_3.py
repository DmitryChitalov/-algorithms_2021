"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение
"""
from memory_profiler import profile


@profile
def recursive_reverse(number):
    if number == 0:
        return ''
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


print('Вызываем рекурсивную функцию.')
recursive_reverse(123)


@profile
def recur_test():
    def recursive_reverse_1(number):
        if number == 0:
            return ''
        return f'{str(number % 10)}{recursive_reverse_1(number // 10)}'


print('Вызываем рекурсивную функцию внутри другой функции.')
recur_test()

"""
При попытке профилирования рекрсивных функций
с помощью декоратора, декоратор срабатывает на каждый вызов функции
и выводит таблицу.
Что бы этого избежать необходимо обернуть рекурсивную функцию 
в другую, и профилировать внешнюю.
Пример работы профилирования на рекурсивной функции 
вывода цифр числа в обратном порядке:
Вызываем рекурсивную функцию.
Filename: C:\Desktop\-algorithms_2021\Урок 6. Практическое задание\task_3.py
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    12     19.0 MiB     19.0 MiB           1   @profile
    13                                         def recursive_reverse(number):
    14     19.0 MiB      0.0 MiB           1       if number == 0:
    15     19.0 MiB      0.0 MiB           1           return ''
    16                                             return f'{str(number % 10)}{recursive_reverse(number // 10)}'
Filename: C:\Desktop\-algorithms_2021\Урок 6. Практическое задание\task_3.py
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    12     19.0 MiB     19.0 MiB           2   @profile
    13                                         def recursive_reverse(number):
    14     19.0 MiB      0.0 MiB           2       if number == 0:
    15     19.0 MiB      0.0 MiB           1           return ''
    16     19.0 MiB      0.0 MiB           1       return f'{str(number % 10)}{recursive_reverse(number // 10)}'
Filename: C:\Desktop\-algorithms_2021\Урок 6. Практическое задание\task_3.py
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    12     19.0 MiB     19.0 MiB           3   @profile
    13                                         def recursive_reverse(number):
    14     19.0 MiB      0.0 MiB           3       if number == 0:
    15     19.0 MiB      0.0 MiB           1           return ''
    16     19.0 MiB      0.0 MiB           2       return f'{str(number % 10)}{recursive_reverse(number // 10)}'
Filename: C:\Desktop\-algorithms_2021\Урок 6. Практическое задание\task_3.py
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    12     19.0 MiB     19.0 MiB           4   @profile
    13                                         def recursive_reverse(number):
    14     19.0 MiB      0.0 MiB           4       if number == 0:
    15     19.0 MiB      0.0 MiB           1           return ''
    16     19.0 MiB      0.0 MiB           3       return f'{str(number % 10)}{recursive_reverse(number // 10)}'
Вызываем рекурсивную функцию внутри другой функции.
Filename: C:\Desktop\-algorithms_2021\Урок 6. Практическое задание\task_3.py
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    23     19.0 MiB     19.0 MiB           1   @profile
    24                                         def recur_test():
    25                                         
    26     19.0 MiB      0.0 MiB           1       def recursive_reverse_1(number):
    27                                                 if number == 0:
    28                                                     return ''
    29                                                 return f'{str(number % 10)}{recursive_reverse_1(number // 10)}'
"""
