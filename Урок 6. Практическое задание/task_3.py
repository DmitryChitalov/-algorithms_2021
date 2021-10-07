"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение
"""
import memory_profiler
import time

def my_decor(func):
    def wrapper(*args, **kwargs):
        m1, t1 = memory_profiler.memory_usage(), time.perf_counter()
        res = func(args[0])
        m2, t2 = memory_profiler.memory_usage(), time.perf_counter()
        mem_diff = m2[0] - m1[0]
        time_diff = t2 - t1
        return res, mem_diff, time_diff
    return wrapper


@my_decor
def fib_rec(n):
    return fib_rec1(n)


def fib_rec1(n):
    if n <= 1:
        return n
    return fib_rec1(n-1) + fib_rec1(n-2)


res, mem_dif, time_diff = fib_rec(10)
print('Выполнение заняло {}  Mib памяти и {:.8} секунд времени.'.format(mem_dif, time_diff))
# в среднем 0.0078125 mib и 20.929222 сек (именно для 30 числа)
del res, mem_dif, time_diff
"""
Если закрепить декоратор к самой рекурсивной функции, то при каждом повторном вызове ркурсии будет вместе с ней
будет происходить запуск декортаора. Из-за этого и потребление памяти, и время на выполнение увеличиваются в несколько
раз, тестирование перестает быть объективным.
Решение создать 'функцию-посредника', которая просто запускает функцию с рекурсией, показалось мне хорошим решением 
проблемы.
"""