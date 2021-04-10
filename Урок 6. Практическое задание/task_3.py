"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение!
"""
from memory_profiler import profile


@profile
def fix_profile(numb):
    def revers_method(numb):
        rest_number, numeral = divmod(numb, 10)
        if rest_number != 0:
            return str(numeral) + revers_method(rest_number)
        else:
            return str(numeral)
    return revers_method(numb)


try:
    number = int(input("введите число: "))
    print("число ", number, " в обратном порядке равно: ", fix_profile(number))
except ValueError:
    print("введено не число")
    
"""
обернули рекурсивную функцию другой функцией и произвели замеры на внешней тем самым избавившись от генерации множества
таблиц от memory_profiler в рекурсии

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    11     18.5 MiB     18.5 MiB           1   @profile
    12                                         def fix_profile(numb):
    13     18.5 MiB      0.0 MiB           6       def revers_method(numb):
    14     18.5 MiB      0.0 MiB           5           rest_number, numeral = divmod(numb, 10)
    15     18.5 MiB      0.0 MiB           5           if rest_number != 0:
    16     18.5 MiB      0.0 MiB           4               return str(numeral) + revers_method(rest_number)
    17                                                 else:
    18     18.5 MiB      0.0 MiB           1               return str(numeral)
    19     18.5 MiB      0.0 MiB           1       return revers_method(numb)


число  12345  в обратном порядке равно:  54321
"""
