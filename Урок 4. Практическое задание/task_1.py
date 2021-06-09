"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Оптимизируйте, чтобы снизить время выполнения
Проведите повторные замеры.

Добавьте аналитику: что вы сделали и почему!!!
Без аналитики задание не принимается
"""
from timeit import timeit

def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr

# list comprehension
def func_2(nums):
    return [i for i in range(len(nums)) if nums[i] % 2 == 0]


# filter(function, iterable)
def func_3(nums):
    new_arr = filter(lambda i: nums[i] % 2 == 0, range(len(nums)))
    return new_arr


n = [i for i in range(100000)]

print(timeit("func_1(n)", globals=globals(), number=10000))
print(timeit("func_2(n)", globals=globals(), number=10000))
print(timeit("func_3(n)", globals=globals(), number=10000))


'''
98.1770606 классический for
85.81944730000001 - list comprehension справляется лучше,чем просто цикл for,но проигрывает функции filter
0.004345700000015995 - функция filter справляется в разы быстрее

'''