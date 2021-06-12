from pympler import asizeof
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


random_list = [randint(0, 100) for i in range(10000)]


@decor
def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


@decor
def func_2(nums):
    return [i for i, el in enumerate(nums) if el % 2 == 0]


@decor
def func_3(nums):
    return list(map(lambda x: x % 2 == 0, nums))


result_func_1, memory_1, run_time_1 = func_1(random_list)
result_func_2, memory_2, run_time_2 = func_2(random_list)
result_func_3, memory_3, run_time_3 = func_3(random_list)
print("Использование append")
print(f"Память: {memory_1} MiB, время: {run_time_1} сек")
print("Списковое включение")
print(f"Память: {memory_2} MiB, время: {run_time_2} сек")
print("Использование map")
print(f"Память: {memory_3} MiB, время: {run_time_3} сек")
print(f"Память, занимаемая в первом варианте: {asizeof.asizeof(func_1(random_list))} б")
print(f"Память, занимаемая во втором варианте: {asizeof.asizeof(func_2(random_list))} б")
print(f"Память, занимаемая в третьем варианте: {asizeof.asizeof(func_3(random_list))} б")

"""
Использование append
Память: 0.15234375 MiB, время: 0.10933736900000002 сек
Списковое включение
Память: 0.19140625 MiB, время: 0.10930597499999994 сек
Использование map
Память: 0.1796875 MiB, время: 0.10938747999999998 сек
Память, занимаемая в первом варианте: 203592 б
Память, занимаемая во втором варианте: 203592 б
Память, занимаемая в третьем варианте: 85344 б

При использовании функции map память расходуется меньше. Скорость выполнения скрипта не изменилась
"""