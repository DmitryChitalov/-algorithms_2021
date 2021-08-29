from timeit import timeit

num_list = [el for el in range(3000)]


def func_1(nums):
    """O(n) – линейная сложность"""
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    # O(n) - линейная
    return [i for i, el in enumerate(nums) if el % 2 == 0]


# 3000 элементов

print(
    timeit('func_1(num_list)', globals=globals(), number=1000)
)  # 0.21701310000000001
print(
    timeit('func_2(num_list)', globals=globals(), number=1000)
)  # 0.1765642

# 30 000 элементов
num_list = [el for el in range(30000)]

print(
    timeit('func_1(num_list)', globals=globals(), number=1000)
)  # 2.1562010000000003
print(
    timeit('func_2(num_list)', globals=globals(), number=1000)
)  # 1.9729044000000004

# 300 000 элементов
num_list = [el for el in range(300000)]

print(
    timeit('func_1(num_list)', globals=globals(), number=1000)
)  # 23.4906299
print(
    timeit('func_2(num_list)', globals=globals(), number=1000)
)  # 19.7763741

"""
ИТОГ: обычный перебор итератором с методом append работает медленней чем списковое включение
"""
