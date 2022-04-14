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


def func_2(nums):
    return filter(lambda i: nums[i] % 2 == 0, range(len(nums)))


def func_3(nums):
    return [i for i in range(len(nums)) if nums[i] % 2 == 0]


n = [i for i in range(1000)]

print(f'func_1(n): {timeit("func_1(n)", globals=globals(), number=1000)}')
print(f'func_2(n): {timeit("func_2(n)", globals=globals(), number=1000)}')
print(f'func_3(n): {timeit("func_3(n)", globals=globals(), number=1000)}')


"""
func_1(n): 0.21222499999999997 - цикл for это самый медленный вариант из.
func_2(n): 0.001156299999999999 - использование встроенной функции позволяет многократно ускорь работу функции
func_3(n): 0.1531964 - при сравнении list comprehension и функции append, list comprehension работает быстрее
"""
