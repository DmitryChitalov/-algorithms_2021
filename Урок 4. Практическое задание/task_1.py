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

nums = [100, 10, 1, 200, 20, 2]



# Исходный вариант
def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


# Альтернативный вариант через стандартную функцию enumerate
def func_2(nums):
    return [k for k, v in enumerate(nums) if not k % 2]


print(timeit.timeit('func_1(nums)', globals=globals(), number=1000))
print(timeit.timeit('func_2(nums)', globals=globals(), number=1000))

# Второй вариант лаконичнее и быстрее по времени, так как стандартная функция  enumerate
# имеет наименьшее время выполнения
