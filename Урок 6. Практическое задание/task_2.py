"""
Задание 2.*
Предложить еще какие-либо варианты (механизмы, подходы, библиотеки, идеи)
для оптимизации памяти и
доказать!!! (наглядно, кодом) их эффективность (на примере профилировщика).
"""

# !!! Помогает значительно оптимизировать память, использование, наравне с map, иных встроенных функций,
# например, filter(). Как и в map(), существенная экономия памяти происходит с увеличением количества данных.
# Пример замеров экономии памяти и времени выполнения приведен после кода функций.

from memory_profiler import memory_usage
from timeit import default_timer


def memory_and_time(func):
    def wrapper(*args, **kwargs):
        start_time = default_timer()
        m1 = memory_usage()
        res = func(*args)
        m2 = memory_usage()
        time_diff = default_timer() - start_time
        mem_diff = m2[0] - m1[0]
        res = func(*args)
        print(f"m1 = {m1} Mib, m2 = {m2} Mib\nВыполнение заняло {mem_diff} Mib, {time_diff} sec")
        return res

    return wrapper


@memory_and_time
def check_even_1(lst):
    new_list = [i for i in lst if i % 2 == 0]
    return new_list

@memory_and_time
def check_even_2(lst):
    new_list = filter(lambda x: x % 2 == 0, lst)
    return new_list


check_even_1(list(range(5000000)))
check_even_2(list(range(5000000)))

# m1 = [211.69140625] Mib, m2 = [231.68359375] Mib
# Выполнение заняло 19.9921875 Mib, 0.654576508 sec

# m1 = [212.54296875] Mib, m2 = [212.54296875] Mib
# Выполнение заняло 0.0 Mib, 0.19939353900000012 sec
