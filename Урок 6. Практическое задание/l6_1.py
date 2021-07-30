"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение!
"""
from time import time
from memory_profiler import memory_usage


def timer_upd(func):
    def temporary(*args, **kwargs):
        start_time = time()
        start_memory = memory_usage()
        result = func(*args, **kwargs)
        memory = memory_usage()
        delta_memory = memory[0] - start_memory[0]
        delta_time = time() - start_time
        print(f'Время выполнения функции {func.__name__} = {delta_time}')
        print(f'Объём затраченной папяти на выполнение функции {func.__name__} = {delta_memory}')
        return result

    return temporary


@timer_upd
def inverse(n):

    def inverse_sub(number):

        if number == 0:
            return ''
        else:
            return str(number % 10) + inverse_sub(number // 10)

    return inverse_sub(n)


print(inverse(5698741230))

# Для замеров всей рекурсии необходимо изначальную функцию вставить внутрь другой,
# чтобы замеры делались не для каждой итерации, а после выполнения всех.
# Есть небольшой нюанс при работе с параметрами, чтобы работа функции оставалась корректной необходимо
# возвращать определяемую внутри функции с аргументом, который берётся из параметров внешней функции.
