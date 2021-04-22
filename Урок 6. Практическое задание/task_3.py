"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение!
"""

from memory_profiler import profile



def sum_n(n):
    if n == 0:
        return 0
    else:
        return n + sum_n(n-1)


print(sum_n(5))


@profile()
def alt(n):
    def sum_n1(*args):
        if n == 0:
            return 0
        else:
            return n + sum_n1(n - 1)
    return alt, print(sum_n(n))


print(alt(5))
