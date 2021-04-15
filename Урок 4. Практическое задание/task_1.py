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
    return [i for i in range(len(nums)) if nums[i] % 2 == 0]


data = [i for i in range(1000)]

print(f'Вариант_1 {timeit("func_1(data)", number=1000, globals=globals())}')
print(f'Вариант_2 {timeit("func_2(data)", number=1000, globals=globals())}')

#вариант 2 "func_2" быстрее, чем 1, так как реализация не использует append 
