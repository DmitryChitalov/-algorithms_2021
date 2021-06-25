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
from timeit import default_timer


def decorator(n):
    def time_it(func):
        def wrapper(numb):
            res = 0
            for el in range(n):
                start_time = default_timer()
                func(numb)
                res += default_timer() - start_time
            print(res)

        return wrapper

    return time_it


@decorator(10)
def func_1(nums):
    # O(n)
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


@decorator(10)
def func_2(nums):
    # O(n)
    return [el for el in nums if el % 2 == 0]


my_array = [el * el for el in range(100000)]

print("Cycle: ")
func_1(my_array)
print("List comprehension: ")
func_2(my_array)

'''
Что сделал: 
    заменил цикл на List Comprehension.

Cycle: 
0.37147135800000003
List comprehension: 
0.18428766699999988

List Comprehension заточен на скорость исполнения и поэтому отрабатывает быстрее цикла.
'''
