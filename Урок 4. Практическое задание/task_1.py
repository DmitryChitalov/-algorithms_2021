"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Оптимизируйте, чтобы снизить время выполнения
Проведите повторные замеры

Добавьте аналитику: что вы сделали и почему!!!
Без аналитики задание считается не принятым
"""
from timeit import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(nums[i])
    return new_arr



def func_2(nums):
    new_arr = []
    while len(nums) > 0:
        last = nums.pop(0)
        if last % 2 == 0:
            new_arr.append(last)
    return new_arr


nums = [1, 2, 3, 4]

print(timeit("func_1(nums)", "from __main__ import func_1, nums"))
print(timeit("func_2(nums)", "from __main__ import func_2, nums"))


"""
В func_1 я исправил (добавлялся индекс, а не элемент массива).
Заменил цикл for (O(n)) и поставил pop (O(1)). 
Функция работает быстрей.
"""