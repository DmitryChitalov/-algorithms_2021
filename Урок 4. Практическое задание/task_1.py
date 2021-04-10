"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Оптимизируйте, чтобы снизить время выполнения
Проведите повторные замеры

Добавьте аналитику: что вы сделали и почему!!!
Без аналитики задание считается не принятым
"""

from timeit import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


# Список для теста
data_list = [i for i in range(1000)]


def func_2(nums):
    return [i for i in range(len(nums)) if nums[i] % 2 == 0]


def func_3(nums):
    return [i for i, el in enumerate(nums) if el % 2 == 0]


if __name__ == '__main__':
    for execut in [1, 10, 20, 50]:
        print(f'Количество выполнений {execut}')
        print(f'Вариант_1 {timeit("func_1(data_list)", number=execut, globals=globals())}')
        print(f'Вариант_2 {timeit("func_2(data_list)", number=execut, globals=globals())}')
        print(f'Вариант_3 {timeit("func_3(data_list)", number=execut, globals=globals())}')


"""
По O-нотации все три варианта, вместе с исходным имею линейную сложность O(n), но вариант 2 "func_2" самая быстрая,
за счет быстрой реализации "List Comprehension". 3й вариант с "enumerate" и списковым включением почти 
идентичен по скорости со вторым, но чуть проигрывает. 
"""