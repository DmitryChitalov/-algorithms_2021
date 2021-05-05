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
import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    return [i for i in range(len(nums)) if nums[i] % 2 == 0]


lstlow = [i for i in range(100)]
lstmax = [i for i in range(10000)]


print(f'Функция 1 (100) {timeit.timeit("func_1(lstlow)", setup="from __main__ import func_1, lstlow", number=10000)}')
print(f'Функция 2 (100){timeit.timeit("func_2(lstlow)", setup="from __main__ import func_2, lstlow", number=10000)}')
print(f'Функция 1 (10000){timeit.timeit("func_1(lstmax)", setup="from __main__ import func_1, lstmax", number=10000)}')
print(f'Функция 2 (10000){timeit.timeit("func_2(lstmax)", setup="from __main__ import func_2, lstmax", number=10000)}')

# func_2 быстрее за счет реализации "List Comprehension" которая не использует append