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


def func_1(nums):   # Первая не оптимизированная функция
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):       # Вторая оптимизированная функция с помощью comprehension
    new_arr = [i for i in range(len(nums)) if i % 2 == 0]
    return new_arr


setup = """
from __main__ import func_1
nums = list(range(100))
"""
setup2 = """
from __main__ import func_2
nums = list(range(100))
"""
print(timeit('func_1(nums)', setup, number=100000))
print(timeit('func_2(nums)', setup2, number=100000))

# Время выполнения первого замера 3.22
# Время выполнения второго замера 2.02
# Для оптимизации использовали comprehension, так как он более оптимизирован
# и выдает более быстрые результаты
