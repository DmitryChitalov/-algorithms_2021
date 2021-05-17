from memory_profiler import memory_usage
from timeit import default_timer


def memory_and_time_print(func):
    def wrapper(*args, **kwargs):
        m1 = memory_usage()
        t1 = default_timer()
        res = func(args[0])
        t2 = default_timer()
        m2 = memory_usage()
        time_diff = t2 - t1
        mem_diff = m2[0] - m1[0]

        print(f'Memory used: {round(mem_diff, 3)} MiB, wasted time: {round(time_diff, 3)} sec')
        return res
    return wrapper


@memory_and_time_print
def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


func_1(range(100000))


@memory_and_time_print
def optimized_func_1(nums):
    return [i for i, num in enumerate(nums) if not num % 2]


optimized_func_1(range(100000))

# Memory used: 2.074 MiB, wasted time: 0.121 sec
# Memory used: 1.285 MiB, wasted time: 0.078 sec

# Задачу решали на одном из уроков и надо было оптимизировать по времени.
# Помимо экономии времени во втором алгоритме заметно снизилась потребляемая память (почти в 2 раза)
# Этот тот случай, когда рефакторинг идёт только на пользу
