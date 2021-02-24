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
            new_arr.append(i)
    return new_arr


def func_2(nums):
    new_arr = [i for i in range(len(nums)) if nums[i] % 2 == 0]
    return new_arr


user_lst = [i for i in range(100)]
print(timeit("func_1(user_lst)", globals=globals()))  # 5.1447363

print(timeit("func_2(user_lst)", globals=globals()))  # 4.1955155

"""
Аналитика.
Для ускорения было использована конструкция спискового включения.
Списковое включение выполняется быстрее цикла с условием и наполнением списка.
"""