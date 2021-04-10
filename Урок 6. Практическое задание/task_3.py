"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение!
"""

from memory_profiler import profile

"""
Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
то надо вывести число 6843.
"""


@profile
def revers_number(number):
    def wrap_revers_number(n):
        if n <= 1:
            return str(n)
        return str(n % 10) + wrap_revers_number(n // 10)
    return wrap_revers_number(number)


revers_number(1234567)

"""
Чтобы избежать срабатывание декоратора при каждом вызове рекурсии необходимо сделать "обертку".
Поместить функцию с рекурсией в другую функцию.

Line #    Mem usage    Increment  Occurrences   Line Contents
============================================================
    24     19.1 MiB     19.1 MiB           1   @profile
    25                                         def revers_number(number):
    26     19.1 MiB      0.0 MiB           8       def wrap_revers_number(n):
    27     19.1 MiB      0.0 MiB           7           if n <= 1:
    28     19.1 MiB      0.0 MiB           1               return str(n)
    29     19.1 MiB      0.0 MiB           6           return str(n % 10) + wrap_revers_number(n // 10)
    30     19.1 MiB      0.0 MiB           1       return wrap_revers_number(number)
"""
