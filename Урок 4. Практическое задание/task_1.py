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
    for i, el in enumerate(nums):
        if el % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_3(nums):
    new_arr = [i for i in range(len(nums)) if nums[i] % 2 == 0]
    return new_arr


def func_4(nums):
    new_arr = [i for i, el in enumerate(nums) if el % 2 == 0]
    return new_arr


nums = list(range(100))

print(timeit("func_1(nums)", globals=globals(),number=10000))
print(timeit("func_2(nums)", globals=globals(),number=10000))
print(timeit("func_3(nums)", globals=globals(),number=10000))
print(timeit("func_4(nums)", globals=globals(),number=10000))
"""
1-ая функция самая медленная, так как тут много 2 функции, поиск элемента , проверка и метод append.
2-ая функция быстрее, так как enumerate рваботает быстрее видимо...
3-ья функция еще быстрее так как это list comp.
4-ая функция еще быстрее так как там enumarate и list comp
