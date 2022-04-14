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


test_lst = [i for i in range(10)]
test_lst2 = [i for i in range(1000)]

print(f'На маленьком тестовом списке')
print(
    timeit(
        "func_1(test_lst)",
        setup='from __main__ import func_1, test_lst',
        number=10000))

print(
    timeit(
        "func_2(test_lst)",
        setup='from __main__ import func_2, test_lst',
        number=10000))

print(f'На большом тестовом списке')
print(
    timeit(
        "func_1(test_lst2)",
        setup='from __main__ import func_1, test_lst2',
        number=10000))

print(
    timeit(
        "func_2(test_lst2)",
        setup='from __main__ import func_2, test_lst2',
        number=10000))

# ### Результаты ###
# На маленьком тестовом списке
# 0.007425400000000006
# 0.007796299999999999
# На большом тестовом списке
# 0.6303167
# 0.48797199999999996
# Выводы: очевидно, что для оптимизации требуется заемнить цикл+append на list comprehension,
# так как списковые включения работают быстрее,
# но интересная деталь,
# что для моего компьютера на маленьком тестовом списке, прирост по скорости оказался незначительным,
# но при увеличении тестового списка прирост по скорости уже весьма значителен.
