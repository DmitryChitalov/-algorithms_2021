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
from timeit import timeit, repeat, default_timer


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    """
    Решение через LC, но что-то существенно быстрее оно не стало,
    скорее всего из-за использования функции enumerate, но как без нее
    до меня не доходит (
    идея оптимизация в уходе от явного цикла и агрегирующих функций
    :param nums:
    :return:
    """
    return [idx for idx, elem in enumerate(nums) if elem % 2 == 0]


setup = "from __main__ import func_1"

print("Замеры по базовому решению")
print(func_1([1, 2, 2, 3, 6, 5, 4, 5, 5, 7]))
print(timeit("func_1([1,2,2,3,6,5,4,5,5,7])", "from __main__ import func_1"))
print(min(repeat("func_1([1,2,2,3,6,5,4,5,5,7])", setup, default_timer, 3)))

print("\nЗамеры по решению через LC")
print(func_2([1, 2, 2, 3, 6, 5, 4, 5, 5, 7]))
print(timeit("func_2([1,2,2,3,6,5,4,5,5,7])", "from __main__ import func_2"))
print(min(repeat("func_2([1,2,2,3,6,5,4,5,5,7])", "from __main__ import func_2", default_timer, 3)))
