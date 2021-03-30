"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение!
"""
from timeit import default_timer
from memory_profiler import memory_usage, profile
from functools import wraps


def memory_time_profiler(func):
    def inner(*args, **kwargs):
        start_time = default_timer()
        start_memory = memory_usage()
        result = func(*args, **kwargs)
        print(f'Затраты времени: {default_timer() - start_time}')
        print(f'Затраты памяти: {memory_usage()[0] - start_memory[0]}')
        return result
    return inner


def even_count(number, even=0, not_even=0):
    if number % 2 == 1:
        not_even += 1
    else:
        even += 1
    if abs(number) > 9:
        return even_count(abs(number)//10, even, not_even)
    else:
        print(f'Кол-во четных чисел: {even}, нечетных: {not_even}')
        return


# Таким образом обертываем функцию только один раз, далее рекурсивно вызывается функция без обертки:

my_func = memory_time_profiler(even_count)
my_func(-122341330)

# Следовательно, можно обернуть рекурсивную функцию нерекурсивной:


@memory_time_profiler
def rec_even_count(number):
    return even_count(number)


rec_even_count(-122341330)



"""Не уверен что решение правильное, т.к. отличаются результаты:
even_count:
    Кол-во четных чисел: 4, нечетных: 5
    Затраты времени: 0.1030083
    Затраты памяти: 0.01171875
second_even_count:
    Кол-во четных чисел: 4, нечетных: 5
    Затраты времени: 0.10964750000000001
    Затраты памяти: 0.0
"""