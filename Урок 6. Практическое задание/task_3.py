from memory_profiler import memory_usage
from timeit import default_timer


def memory_time(func):
    def wrapper(*args):
        t_1 = default_timer()
        mem_1 = memory_usage()
        result = func(*args)
        print(f'Время: {default_timer() - t_1}\nПамять: {memory_usage()[0] - mem_1[0]}')
        return result

    return wrapper


@memory_time
def for_measuring():
    def ascii_symbols(n=1):
        return str(n) + ' - ' + chr(n) + ('\n' if n % 10 == 1 else ' ') + ascii_symbols(
            n + 1) if n < 255 else '255 - ' + chr(255)


print(for_measuring())

'''
Время: 0.10997049999999997
Память: 0.015625

Для проведения профилировки для скриптов с рекурсией рекурсию нужно вложить в другую функцию. Без этого 
декоратор будет измерять каждую итерацию отдельно.
'''
