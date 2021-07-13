"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение
"""
from timeit import timeit
from memory_profiler import memory_usage


def time_memory(func):
    def wrap(*args, **kwargs):
        start_time = timeit()
        start_mem = memory_usage()
        result = func(*args, **kwargs)
        print(f'Time: {start_time - timeit()}\nMemory: {memory_usage()[0] - start_mem[0]}')
        return result
    return wrap


@time_memory
def ascii_table_main():
    def ascii_table(_ascii_code=32, count=0):
        if _ascii_code <= 127:
            if count == 10:
                print()
                count = 0
            print('{0:4} - {1:4}'.format(_ascii_code, chr(_ascii_code)), end="| ")
            ascii_table(_ascii_code + 1, count + 1)


ascii_table_main()

"""
Профилировка рекурсивных функций возможна в случае обертки рекурсивной функции в другую функцию. В том случае данные 
профилировки будут точными. В обратном случае, мы будем получать данные на каждый вызов рекурсивной функции.
"""
