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


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


test_arr = [i for i in range(100)]

print(timeit.timeit('func_1(test_arr)', globals=globals(), number=100000))
# 1.2354482629999999


def func_2(nums):
    new_arr = [i for i in range(len(nums)) if nums[i] % 2 == 0]
    return new_arr


print(timeit.timeit('func_2(test_arr)', globals=globals(), number=100000))
# 0.9334593440000001
# Попробовал использовать lc, увидел значительную прибавку к скорости выполнения


def func_3(nums):
    new_arr = []
    test = new_arr.append
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            test(i)
    return new_arr


print(timeit.timeit('func_3(test_arr)', globals=globals(), number=100000))
# 1.047493346
# Попробовал вынести функцию append в отдельную переменную, заметил увеличение скорости


def func_4(nums):
    new_arr = []
    test = new_arr.append
    for idx, val in enumerate(nums):
        if val % 2 == 0:
            test(idx)
    return new_arr


print(timeit.timeit('func_4(test_arr)', globals=globals(), number=100000))
# 0.923437748
# функция enumerate и вынесение функции append дают прибавку к скорости на уровне lc


def func_5(nums):
    new_arr = [i for i, val in enumerate(nums) if val % 2 == 0]
    return new_arr


print(timeit.timeit('func_5(test_arr)', globals=globals(), number=100000))
# 0.8308847449999996
# объединил два лучших варианта, получил оптимальное значение
