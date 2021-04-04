"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение!
"""

from memory_profiler import profile


@profile
def extra_wrapper(number):
    got_number = number

    def reverse_number(x):
        if x == 0:
            return ""
        else:
            current_number = x % 10
            x = x // 10
            return str(current_number) + reverse_number(x)
    return reverse_number(got_number)


string_to_process = 1234560
print(extra_wrapper(string_to_process))

"""
Подводный камень заклбючается в том, что при каждом вызове функции профайлер будет выводить новую таблицу
потребления памяти.

Для профилирования рекурсивных функций можно дополнительно оберунуть ее в обычную функцию и применять декоратор
к обертке. Данный подход позволяет увидеть сколько раз на самом деле рекурсия вызвает сама себя.


Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    12     16.1 MiB     16.1 MiB           1   @profile
    13                                         def extra_wrapper(number):
    14     16.1 MiB      0.0 MiB           1       got_number = number
    15                                         
    16     16.1 MiB      0.0 MiB           9       def reverse_number(x):
    17     16.1 MiB      0.0 MiB           8           if x == 0:
    18     16.1 MiB      0.0 MiB           1               return ""
    19                                                 else:
    20     16.1 MiB      0.0 MiB           7               current_number = x % 10
    21     16.1 MiB      0.0 MiB           7               x = x // 10
    22     16.1 MiB      0.0 MiB           7               return str(current_number) + reverse_number(x)
    23     16.1 MiB      0.0 MiB           1       return reverse_number(got_number)


0654321
"""