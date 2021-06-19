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


# Сделал через лист коприхеншен и range, оба варианта оказались лучше(примерно одинаковы по скорости)
# Range потому что выборка изначально идёт только по чётным числам и это встроенная функция,
# Лист комприхеншен, может, потому что код короче и нет append
from timeit import timeit

print('По умолчанию')


def func_1(nums=range(1, 101)):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


print(timeit('func_1', globals=globals()))
print('С помощью list comprehension')
func_2 = []
func_2 = [el for el in func_2 if el % 2 == 0]
print(timeit('func_2', globals=globals()))
print('С помощью range')
func_3 = []
for el in range(0, 100, 2):
    func_3.append(el)
print(timeit('func_3', globals=globals()))

