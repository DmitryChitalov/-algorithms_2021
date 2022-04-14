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
    new_arr = [num for num in nums if num % 2 == 0]
    return new_arr


def func_3(nums):
    new_arr = list(filter(lambda x: x % 2 == 0, nums))
    return new_arr


numbers = []
for i in range(1000):
    numbers.append(i)


print(timeit('func_1(numbers)', globals=globals(), number=1000))  # замеряем на тысяче повторений

# теперь используем list comprehension вместо цикла,
# ожидание - встроенная функция имеет ту же сложность, но выполняется быстрее
print(timeit('func_2(numbers)', globals=globals(), number=1000))
# выполняется в полтора раза быстрее

# но что если использовать функциональное выражение?
print(timeit('func_3(numbers)', globals=globals(), number=1000))
# выполняется даже чуть медленнее чем свой алгоритм через цикл
