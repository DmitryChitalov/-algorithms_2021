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

nums = [x for x in range(1, 101)]

def func_1(nums):
    """" Сложность O(n) """
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr

def func_2(nums):
    """ Какую сложность будет иметь LC? В нем конструкция for in
    Это будет линейная? """
    new_arr = [x for x in nums if x % 2 == 0]
    return new_arr

print(f'Результат func_1: {timeit("func_1(nums)", globals=globals(), number=1000000)}')
print(f'Результат func_2: {timeit("func_2(nums)", globals=globals(), number=1000000)}')
"""
Результат func_1: 14.085936761000001
Результат func_2: 7.9410723359999995
LC - работает заметно быстрее
"""

