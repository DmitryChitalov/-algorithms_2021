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


# Я оптимизировала второй код за счет лист комприхеншн и энумирейт (на код уходит меньше времени и замеры это доказали)

from timeit import timeit


test_code = '''
def func_1(nums=[1,2,3,4,5,6]):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr
'''
print(f'Время работы 1 кода -')
print(timeit(test_code, globals=globals()))

test_code_2 = '''
def func_2(nums=[1,2,3,4,5,6]):
    return [v for k, v in enumerate(nums) if not k%2]
'''

print(f'Время работы 2 кода -')
print(timeit(test_code_2, globals=globals()))



