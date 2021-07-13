from timeit import default_timer
from memory_profiler import memory_usage


def time_memory(func):
    def wrap(*args, **kwargs):
        start_time = default_timer()
        start_mem = memory_usage()
        result = func(*args, **kwargs)
        print(f'Time: {default_timer() - start_time}\nMemory: {memory_usage()[0] - start_mem[0]}')
        return result
    return wrap


@time_memory
def reversion():
    def rev_req(number=123456782143242341231242123):
        if number < 10:
            return number
        else:
            return str(number % 10) + str(rev_req(number // 10))


@time_memory
def reversion_2(number):
    _buf_var = list(str(number))
    return ''.join(_buf_var[::-1])


reversion()
reversion_2(13456782352566353441221312312313121112534533)


"""
Time: 0.10036224699979357
Memory: 0.0
Time: 0.1004749380008434
Memory: 0.0

По использованию памяти не получилось получить данные, но решение через конвертацию в строку короче, чем решение через
использование рекурсии, хоть и занимает немногим больше времени на испольнение. 
"""
