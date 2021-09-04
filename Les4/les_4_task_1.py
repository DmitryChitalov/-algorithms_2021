import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    return [i for i in range(len(nums)) if nums[i] % 2 == 0]


print(timeit.timeit("func_2([i for i in range(10000, 100000)])", setup="from __main__ import func_2", number=1000))  # 7.6743883

"""
list comprehension работает быстрее, чем большое кол-во append().
"""
