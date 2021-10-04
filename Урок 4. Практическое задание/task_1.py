import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    return [i for i in range(len(nums)) if i % 2 == 0]


if __name__ == '__main__':
    little = [el for el in range(1000)]
    medium = [el for el in range(10000)]
    big = [el for el in range(100000)]
    print(f"Минимальный массив: {timeit.timeit('func_1(little)', globals=globals(), number=1000)}")
    print(f"Минимальный массив (lc): {timeit.timeit('func_2(little)', globals=globals(), number=1000)}")
    print(f"Средний массив: {timeit.timeit('func_1(medium)', globals=globals(), number=1000)}")
    print(f"Средний массив (lc): {timeit.timeit('func_2(medium)', globals=globals(), number=1000)}")
    print(f"Большой массив: {timeit.timeit('func_1(big)', globals=globals(), number=1000)}")
    print(f"Большой массив (lc): {timeit.timeit('func_2(big)', globals=globals(), number=1000)}")

    """
    List comprehension(func2) работает быстрее чем обычный цикл с append.
    """