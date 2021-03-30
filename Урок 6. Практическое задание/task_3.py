"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение!
"""
from timeit import default_timer

from memory_profiler import memory_usage, profile


def decor(func):
    def wrapper(*args, **kwargs):
        start = default_timer()
        memory = memory_usage()
        result = func(*args, **kwargs)
        print(f'Затрачено памяти {memory_usage()[0] - memory[0]}')
        print(f'Время выполнения: {default_timer() - start}')
        return result
    return wrapper


def rec(number):
    if number <= 1:
        return number
    return rec(number - 1) + rec(number - 2)


fact = decor(rec)
print(fact(19))


@profile(precision=4)
def give_number(number):
    def rec(number):
        if number <= 1:
            return number
        return rec(number - 1) + rec(number - 2)
    return rec(number)


print(give_number(19))

"""
Сделал 2 варианта реализации.
В первом случае сделал свой декоратор и в него как аргумент записал функцию. 
Второй вариант, обернул рекурсивную функцию в обычную- и декоратор выполняется на обучную функцию, не вызываясь рекурсивно.

"""
