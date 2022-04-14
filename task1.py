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
import timeit
my = [1,2,3,4,5,6,7,8]

def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr



print('1 -- ', timeit.timeit('func_1(my)', 'from __main__ import func_1, my', number=1000))


def func_2(my):
    for i in range(0, len(my), 2):
        True


print('2 -- ', timeit.timeit('func_2(my)', 'from __main__ import func_2, my', number=1000))
func_2(my)

# 2 вариант быстрее, перебираем элементы через один, получается в 2 раза меньше