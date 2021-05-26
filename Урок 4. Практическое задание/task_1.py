"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Оптимизируйте, чтобы снизить время выполнения
Проведите повторные замеры.

Добавьте аналитику: что вы сделали и почему!!!
Без аналитики задание не принимается
"""

from timeit import timeit


# test_list = list((int(n)) for n in range(1000))
test_list = list(range(100000))


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    new_arr = [i for i in nums if i % 2 == 0]
    return new_arr


print(
    timeit(
        "func_1(test_list)",
        globals=globals(),
        number=1000))
print(
    timeit(
        "func_2(test_list)",
        globals=globals(),
        number=1000))

# Итератор с функцией append был заменён на списковое включение; счетчик,
# идущий по по индексу с дальнейшим обращением к элементу по полученному
# индексу был заменен на прямое обращение к элементу во время пербора списка в цикле.
# По итогу: время выполнения задачи уменьшилось примерно вдвое.
