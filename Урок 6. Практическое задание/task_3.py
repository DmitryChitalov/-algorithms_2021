"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение!
"""
from memory_profiler import memory_usage
import timeit


def dec(func):
    def wrapper(*args, **kwargs):
        mem1 = memory_usage()
        t1 = timeit.default_timer()
        res = func(args[0])
        mem2 = memory_usage()
        t2 = timeit.default_timer()
        mem_diff = mem2[0] - mem1[0]
        time_diff = t2 - t1
        return res, mem_diff, time_diff

    return wrapper


@dec
def recursive_reverse_mem(number):
    if number == 0:
        return ''
    return f'{str(number % 10)}{recursive_reverse_mem(number // 10)}'


@dec
def func_rev(number):
    def recursive_reverse_mem(number):
        if number == 0:
            return ''
        return f'{str(number % 10)}{recursive_reverse_mem(number // 10)}'

    return recursive_reverse_mem(number)


rev_func, mem_dif, time_dif = recursive_reverse_mem(5555672)
print(f"Память - {mem_dif}, Время - {time_dif}")

rev_func, mem_dif, time_dif = func_rev(5555672462523534763453463786786345645645623423523523526661)
print(f"Память - {mem_dif}, Время - {time_dif}")

"""
Напрямую функцию с рекурсией профилировать не возможно, 
так как декоратор вызывается каждый раз при вызове функции в  рекурсии.
Можно обернуть функцию рекурсии в другую функцию и сделать профилировку этой функциии

Первые значнния без обертки с малым числом - выполняется долго
Память - 0.01953125
Время - 1.6401173

Вторые значения функция в обертке
Память - 0.02734375
Время - 0.10813230000000029
"""
