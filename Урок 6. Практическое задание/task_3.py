"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение
"""
from memory_profiler import profile


@profile
def odd_even_num(num, even=0, odd=0):
    if num > 0:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1
        num = num // 10
        return odd_even_num(num, even, odd)
    else:
        return print(f"В вашем числе: четных цифр {even}, нечетных {odd}")


odd_even_num(765987)

"""
При профилировании рекурсии, данная таблица будет будет отображаться каждый раз когнда в теле функции будет происходить 
рекурсивный вызов.
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    12     18.3 MiB     18.3 MiB           7   @profile
    13                                         def odd_even_num(num, even=0, odd=0):
    14     18.3 MiB      0.0 MiB           7       if num > 0:
    15     18.3 MiB      0.0 MiB           6           if num % 2 == 0:
    16     18.3 MiB      0.0 MiB           2               even += 1
    17                                                 else:
    18     18.3 MiB      0.0 MiB           4               odd += 1
    19     18.3 MiB      0.0 MiB           6           num = num // 10
    20     18.4 MiB      0.0 MiB           6           return odd_even_num(num, even, odd)
    21                                             else:
    22     18.3 MiB      0.0 MiB           1           return print(f"В вашем числе: четных цифр {even}, нечетных {odd}")
"""


@profile
def profile_recursion(num, even=0, odd=0):
    def odd_even_num(num, even=0, odd=0):
        if num > 0:
            if num % 2 == 0:
                even += 1
            else:
                odd += 1
            num = num // 10
            return odd_even_num(num, even, odd)
        else:
            return print(f"В вашем числе: четных цифр {even}, нечетных {odd}")


profile_recursion(765987)

"""
Для решения этой проблемы достаточно профилируемую функцию с рекурсией поместить в другую функцию.
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    46     18.3 MiB     18.3 MiB           1   @profile
    47                                         def profile_recursion(num, even=0, odd=0):
    48     18.3 MiB      0.0 MiB           1       def odd_even_num(num, even=0, odd=0):
    49                                                 if num > 0:
    50                                                     if num % 2 == 0:
    51                                                         even += 1
    52                                                     else:
    53                                                         odd += 1
    54                                                     num = num // 10
    55                                                     return odd_even_num(num, even, odd)
    56                                                 else:
    57                                                     return print(f"В вашем числе: четных цифр {even}, нечетных {odd}")



Process finished with exit code 0

"""

