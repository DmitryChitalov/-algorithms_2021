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


nums = list(range(100))


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr

print(func_1(nums))

print(
    timeit(
        "func_1(nums)",
        globals=globals(),
        number=1000))




def func_2(nums):
    new_arr = []
    for i in range(0, len(nums), 2):
            new_arr.append(i)
    return new_arr

print(func_2(nums))

print(
    timeit(
        "func_2(nums)",
        globals=globals(),
        number=1000
    )
)


def func_3(nums):
    new_arr = [i for i in range(0, len(nums), 2)]
    return new_arr


print(func_3(nums))

print(
    timeit(
        "func_3(nums)",
        globals=globals(),
        number=1000
    )
)
# По сравнению с функцией №1 было упрощено условие проверки (if) что привело к ускорению кода,
# в 3-ем примере убрали функцию append, что позволило ускорить процесс

