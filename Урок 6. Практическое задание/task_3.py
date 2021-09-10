"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение
"""

from memory_profiler import profile


@profile
def func(*args):
    def recursion(n):
        return str(n) if n < 10 else str(n % 10) + recursion(n // 10)

    return recursion(*args)


number = int(input('Введите число, которое требуется перевернуть: '))
print(f'Перевернутое число: {func(number)}')

# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
#     12     19.2 MiB     19.2 MiB           1   @profile
#     13                                         def func(*args):
#     14     19.2 MiB      0.0 MiB           6       def recursion(n):
#     15     19.2 MiB      0.0 MiB           5           return str(n) if n < 10 else str(n % 10) + recursion(n // 10)
#     16
#     17     19.2 MiB      0.0 MiB           1       return recursion(*args)

# Чтобы рекурсия каждый раз не вызывала профилировщик, нужно завернуть рекурсию в другую функцию.
