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
        print(f'затраты времени: {end_time - start_time}\nзатраты памяти: {end_memory[0] - start_memory[0]}')

    return wrapper


@memory_profile
def even_odd_count_recur(usr_num):
    def recur_wrap(num, even=0, odd=0):
        if num == 0:
            return f'Количество четных и нечетных цифр в числе равно: ({even}, {odd})'
        else:
            operand = num % 10
            if operand % 2 == 0:
                even += 1
            else:
                odd += 1
            recur_wrap(num // 10, even, odd)

    return recur_wrap(usr_num)


testing_num = 123456789987654321
even_odd_count_recur(testing_num)

'''
Т.к. рекурсивная функция вызывает сама себя, профилировщик будет срабатывать на каждом вызове внутри рекурсии.
Чтобы этого избежать необходимо обернуть рекурсивную функцию в дополнительный слой. 
Так профилировщик будет вызан только 1 раз.
'''