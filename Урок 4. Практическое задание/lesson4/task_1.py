from timeit import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    return [idx for num, idx in enumerate(nums) if num % 2 == 0]


nums_list = [i for i in range(0, 100)]

print(f'Предложенная реализация: {timeit("func_1(nums_list)", globals=globals())}')
print(f'Реализация через LC: {timeit("func_2(nums_list)", globals=globals())}')

"""
Вывод:
Реализация алгоритма через  list comprehension дает прирост к скорости и 
более компактный вариант написания.
"""
