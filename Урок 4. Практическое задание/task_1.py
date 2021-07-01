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
    ''' Задание по умолчанию имеет O(n) '''
    new_arr = []
    for i in range (len (nums)):
        if nums[i] % 2 == 0:
            new_arr.append (i)
    return new_arr


def func_2(nums):
    '''Оптимизированное решение, сделанное через списковое включение O(n),
    всегда работает чуть быстрее'''
    return [index for index, element in enumerate (nums) if (element % 2) == 0]


if __name__ == '__main__':
    some_list = [element for element in range (10)]
    print (some_list)
    print (timeit ("func_1(some_list)", globals = globals ()))
    print (timeit ("func_2(some_list)", globals = globals ()))

    some_list = [element for element in range (100)]
    print (some_list)
    print (timeit ("func_1(some_list)", globals = globals ()))
    print (timeit ("func_2(some_list)", globals = globals ()))

""" Результаты
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
0.8041491000000001
0.7414396999999999
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21,
 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41,
  42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61,
   62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81,
    82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
5.551125900000001
5.034822299999999
"""
