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
    new_arr = []  # O(1)
    for i in range(len(nums)):  # O(n)
        if nums[i] % 2 == 0:  # O(1)
            new_arr.append(i)  # O(1)
    return new_arr


def func_1_modern(nums):
    new_arr = [i for i, val in enumerate(nums) if not val % 2]  # O(n)
    return new_arr


massive = range(50)
print(f"{timeit.timeit('func_1(massive)', globals=globals())} сек.")
print(f"{timeit.timeit('func_1_modern(massive)', globals=globals())} сек.")

# Функция func_1_modern работает быстрее func_1 (2.4326635 против 6.9827586 с., соответственно)
# При модификации функции использовал enumerate(). Эта встроенная функция работает быстрее,
# чем написанная непосредственно в Python, не смотря не то, что имеет такую же сложность O(n), как и цикл for
