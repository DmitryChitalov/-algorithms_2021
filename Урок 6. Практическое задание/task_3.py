"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение
"""
from memory_profiler import profile


@profile
def profile_rec_stop(*args):
    def recursion_odd(num, odd=0, even=0):
        if num == 0:
            return f'{odd}, {even}'
        if (num % 10) % 2 == 0:
            odd += 1
            return recursion_odd(num // 10, odd, even)
        else:
            even += 1
            return recursion_odd(num // 10, odd, even)
    return recursion_odd(*args)


print(profile_rec_stop(12343534535763567543734))

# Для того, чтобы @profile не отрабатывал на каждую итерацию, достаточно обернуть
# рекурсивную функцию в ещё одну функцию
