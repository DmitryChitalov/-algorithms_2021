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

#тест лист:
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

#поменяли на list comprehension:
# как факт минус по созданию пустого массива и добавления-append
def func_2(nums):
    return [i for i in range(len(nums)) if nums[i] % 2 == 0]

#поменяли на enumerate(nums):
#как факт проходим циклом сразу по эл. массива , не нужно получать длину, запрашивать доп. элементы из массива
def func_3(nums):
    return [i for i, num in enumerate(nums) if nums[i] % 2 == 0]

# замеры:
print('func_1: ', timeit('func_1(nums)', globals=globals()))
print('func_2: ', timeit('func_2(nums)', globals=globals()))
print('func_3: ', timeit('func_3(nums)', globals=globals()))

'''
Итоги:
func_1:  2.2565408999999996
func_2:  2.1562788999999998
func_3:  2.0954363773733477
С каждой оптимизацией скорость работы сокращается. Самый скоростной 3ий вариант (быстрый) 
'''