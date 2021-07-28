"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение
"""
import memory_profiler


@memory_profiler.profile()
def wrap_get_revers_number(in_num):

    def get_revers_number(input_number, revers_number=[]):
        """
        Получение перевёрнутого числа.
        :param input_number:
        :param revers_number:
        :return:
        """
        if input_number == 0:
            return "".join(str(e) for e in revers_number)
        else:
            remainder = input_number % 10
            revers_number.append(remainder)
            input_number = input_number // 10
            return get_revers_number(input_number, revers_number)

    return get_revers_number(in_num)


my_number = 34543756756756756767897353454365776899800657670
revs_number = wrap_get_revers_number(my_number)
print(f"Перевернутое число: {revs_number}")

"""
Проблема есть, при профилировке скриптов с рекурсией. Измеряется каждый вызов.
Выход есть - оборачиваем рекурсионную функцию в ещё обёртку.

Filename: C:/Users/krole/Documents/GitHub/Algorithms/Урок 6. Практическое задание/task_3.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    11     33.2 MiB     33.2 MiB           1   @memory_profiler.profile()
    12                                         def wrap_get_revers_number(in_num):
    13                                         
    14     33.2 MiB      0.0 MiB          49       def get_revers_number(input_number, revers_number=[]):
    15                                                 
    16                                                 #Получение перевёрнутого числа.
    17                                                 #:param input_number:
    18                                                 #:param revers_number:
    19                                                 #:return:
    20                                                 
    21     33.2 MiB      0.0 MiB          48           if input_number == 0:
    22     33.2 MiB      0.0 MiB          97               return "".join(str(e) for e in revers_number)
    23                                                 else:
    24     33.2 MiB      0.0 MiB          47               remainder = input_number % 10
    25     33.2 MiB      0.0 MiB          47               revers_number.append(remainder)
    26     33.2 MiB      0.0 MiB          47               input_number = input_number // 10
    27     33.2 MiB      0.0 MiB          47               return get_revers_number(input_number, revers_number)
    28                                         
    29     33.2 MiB      0.0 MiB           1       return get_revers_number(in_num)


Перевернутое число: 07675600899867756345435379876765765765765734543

Process finished with exit code 0
"""