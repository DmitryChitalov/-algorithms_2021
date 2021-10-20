"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение
"""
from timeit import default_timer
from memory_profiler import memory_usage


def memory_profile(func):
    def wrapper(*args,**kwargs):
        start_time = default_timer()
        start_memory = memory_usage()
        func(*args,**kwargs)
        end_time = default_timer()
        end_memory = memory_usage()
        print(f'затраты времени: {end_time - start_time}\nзатраты памяти: {end_memory[0] - start_memory[0]}')
        return func(*args,**kwargs)

    return wrapper


@memory_profile
def task_2_wrapper(number):
    def task_2(number, even=0, odd=0):
        """
        Функция подсчета четных и нечетных цифр в введенном числе
        """
        if number == 0:
            return f"Количество четных и нечетных цифр в числе равно: ({even}, {odd})"
        num = number % 10
        number = number // 10
        if num % 2 != 0:
            odd += 1
            return task_2(number, even, odd)
        else:
            even += 1
            return task_2(number, even, odd)

    return task_2(number)


print(task_2_wrapper(13013246246))
"""
Рекурсивная функция вызывает сама себя, следовательно профилировщик будет срабатывать на каждом вызове.
Чтобы этого избежать нужно сделать обертку для функции.
"""
