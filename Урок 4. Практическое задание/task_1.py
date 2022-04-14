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
    new_arr = []
    count = 0
    for i in nums:
        if not i % 2:
            new_arr.append(count)
        count += 1
    return new_arr


def func_3(nums):
    new_arr = [i for i in range(len(nums)) if nums[i] % 2 == 0]
    return new_arr


test_list = list(range(100))

print(timeit("func_1(test_list)", globals=globals()))
print(timeit("func_2(test_list)", globals=globals()))
print(timeit("func_3(test_list)", globals=globals()))

"""В алгоритме 2 Убрал поиск элемента по индексу. Индекс заменил переменной, которая нарищивается при проходе списка. 
Алгоритм стал работать немного быстрее. В алгоритме 3 избавился от метода append """
