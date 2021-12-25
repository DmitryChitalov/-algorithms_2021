"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Оптимизируйте, чтобы снизить время выполнения
Проведите повторные замеры.

Добавьте аналитику: что вы сделали и почему!!!
Без аналитики задание не принимается

И прошу вас обратить внимание, что то, что часто ошибочно называют генераторами списков,
на самом деле к генераторам отношения не имеет. Это называется "списковое включение" - list comprehension.
"""
import timeit
el_1 = 0
num_list = [el_1 for el in range(100)]


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


print('v1', timeit.timeit('func_1(num_list)', globals=globals()))


def func_3(nums):
    nums_1 = [nums.index(el) for el in nums if el % 2 == 0]
    return nums_1


print('list_comprehension', timeit.timeit('func_3(num_list)', globals=globals()))


def func_4(nums):
    nums_1 = []
    for el in nums:
        if el % 2 == 0:
            nums_1.append(nums.index(el))
    return nums_1


print('for_cycle', timeit.timeit('func_4(num_list)', globals=globals()))
# В func_3 варианте я просто сделал перебор массива по элементам, а не
# по индексам, скорость возрасла, по сравнению с первой функцией, в конце при помощи функции index я добавляю индекс
# четного элемента в новый массив.
# В func_4 варианте я повторил действия третьего, но он оказался быстрее только на малых объёмах массива, при больших
# объёмах массива он медленнее.
