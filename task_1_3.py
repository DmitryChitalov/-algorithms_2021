from random import randint
import memory_profiler
from timeit import default_timer


def decor(func):
    def wrapper(*args):
        m1 = memory_profiler.memory_usage()
        start_time = default_timer()
        result = func(*args)
        m2 = memory_profiler.memory_usage()
        mem_usage = m2[0] - m1[0]
        run_time = default_timer() - start_time
        return result, mem_usage, run_time
    return wrapper


@decor
def even_func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


@decor
def even_func_2(nums):
    new_arr = list(map(lambda x: x % 2 == 0, nums))
    return new_arr


if __name__ == '__main__':
    original_list = [randint(0, 10000) for _ in range(1000000)]
    res_1, mem_diff_1, runtime_1 = even_func_1(original_list)
    res_2, mem_diff_2, runtime_2 = even_func_2(original_list)

    print(f"Выполнение через append заняло {mem_diff_1} Mib и {runtime_1} секунд")
    print(f"Выполнение через map заняло {mem_diff_2} Mib и {runtime_2} секунд")


"""
Выполнение через append заняло 19.21484375 Mib и 0.2680469000000001 секунд
Выполнение через map заняло 7.6328125 Mib и 0.3174162999999999 секунд

Получается, что функция map расходует память более экономично. 
"""
