"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение
"""
import memory_profiler


def decor(func):
    def wrapper(*args, **kwargs):
        m1 = memory_profiler.memory_usage()
        res = func(*args, **kwargs)
        m2 = memory_profiler.memory_usage()
        mem_diff = m2[0] - m1[0]
        print(f'Выполнение заняло: {mem_diff} Mib')
        return res
    return wrapper


def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


@decor
def funct_():
    return factorial(7)


print(funct_())
