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
        res = func(args[0])
        m2 = memory_profiler.memory_usage()
        mem_diff = m2[0] - m1[0]
        return res, mem_diff

    return wrapper


@decor
def recursive_reverse2(number):
    def recursive_reverse(number):
        if number == 0:
            return ''
        return f'{str(number % 10)}{recursive_reverse(number // 10)}'


res, mem_diff = recursive_reverse2(123)
print(f"Выполнение заняло {mem_diff} Mib")

# Для измерения памяти в функции с рекурсией нужно небходимо вложить функцию внутрь другой функции.
