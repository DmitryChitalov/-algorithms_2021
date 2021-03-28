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

import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


# Оптимизируем функцию с ипользованием list comprehension
def func_2(nums):
    return [i for i in nums if i%2 == 0]


n = [1, 2, 3, 4, 5, 6, 7]

for num in [1000, 10000, 100000]:
    t_func_1 = timeit.timeit('func_1(n)', 'from __main__ import func_1, n', number=num)
    t_func_2 = timeit.timeit('func_2(n)', 'from __main__ import func_2, n', number=num)
    print(f"{num}\t attempts ---> FUNC1 = {t_func_1:2f} FUNC2 = {t_func_2:2f} --- {'FUN1' if t_func_1 < t_func_2 else 'FUN2'}")

# Результаты показывают что func_2 быстрее func_1
