"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение!
"""
from timeit import default_timer
from memory_profiler import memory_usage


def memory_profile(func):
    def wrapper(*args):
        start_time = default_timer()
        start_memory = memory_usage()
        func(*args)
        end_time = default_timer()
        end_memory = memory_usage()
        print(f'Временные затраты: {end_time - start_time}\nЗатраты памяти: {end_memory[0] - start_memory[0]}')

    return wrapper


@memory_profile
def even_odd_count_recur(num):
    def recur_wrap(num, even=0, odd=0):
        if num == 0:
            return f'Количество четных цифр: {even}, нечетных цифр: {odd})'
        else:
            operand = num % 10
            if operand % 2 == 0:
                even += 1
            else:
                odd += 1
            recur_wrap(num // 10, even, odd)

    return recur_wrap(num)


even_odd_count_recur(23414262765762574782987938198)

'''
Временные затраты: 0.104021543
Затраты памяти: 0.015625

Рекурсивная функция вызывает сама себя, поэтому профилировщик срабатывает на каждом вызове рекурсии.
Нужно обернуть рекурсивную функцию в ещё один слой, чтобы профиировщик сработал только единственный раз. 
'''