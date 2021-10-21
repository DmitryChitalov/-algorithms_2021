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
from itertools import islice

def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr

arr = [i for i in range(100)]

def func_2(nums):
    new_arr = [i for i in range(100) if nums[i] % 2 == 0]
    return new_arr

def func_3(nums):
    new_arr = list(filter(lambda i: nums[i] % 2 == 0, nums))
    return new_arr

def func_4(nums):
    new_arr = (i for i in range(100) if nums[i] % 2 == 0)
    return new_arr


print(func_1(arr))
print(func_2(arr))
print(func_3(arr))
print(*islice(func_4(arr), 100))

print(
    timeit(
        "func_1(arr)",
        globals=globals(),
        setup="from __main__ import func_1",
        number=1000),
    timeit(
        "func_2(arr)",
        globals=globals(),
        setup="from __main__ import func_2",
        number=1000),
    timeit(
        "func_3(arr)",
        globals=globals(),
        setup="from __main__ import func_3",
        number=1000),
    timeit(
        "func_4(arr)",
        globals=globals(),
        setup="from __main__ import func_4",
        number=1000), sep='\n'
)

"""
list comprehension выигрывает по скорости обычный цикл, так как мы избегает добавление элементов в новый список.
lambda- функция тоже особо не выигрывает(чуть хуже обычного цикла) из-за использования list().
Генератор по скорости выигрывает всех, но он не выводит список, что не удовлетворяет условию задачи. 
Если реализовать добавление элементов генератора в список, то по скорости мы не выиграем, т.к. будет добавление элементов как в func_1.
Вывод: lc - маст хэв
"""