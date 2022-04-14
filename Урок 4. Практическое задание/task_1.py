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
import random

TEST_DATA = [random.randrange(0, 100) for i in range(100)]


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    return [i for i in range(len(nums)) if not nums[i] % 2]


def func_3(nums):
    return [idx for idx, num in enumerate(nums) if not num % 2]


# Демонстрация того, как распаковка ускоряет функцию
def func_4(nums):
    return [i[0] for i in enumerate(nums) if not i[1] % 2]

print(func_1(TEST_DATA) == func_2(TEST_DATA) == func_3(TEST_DATA) == func_4(TEST_DATA))

print(timeit('func_1(TEST_DATA)', globals=globals( )))
print(timeit('func_2(TEST_DATA)', globals=globals( )))
print(timeit('func_3(TEST_DATA)', globals=globals( )))
print(timeit('func_4(TEST_DATA)', globals=globals( )))
"""
Использование list comprehension в сочетании с функцией enumerate показало лучший результат.
Я воспользовался данным механизмом так как он работает быстрее, чем обычный обход и добавление значения.
Также заменил '==' в if на not, что также позволило выиграть пару десятых секунды.
"""