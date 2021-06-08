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

import timeit


# for, append
def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


# enumerate - list comprehension
def func_2(nums):
    return [i for i, numeral in enumerate(nums) if numeral % 2 == 0]


# lambda
def func_3(nums):
    return [lambda i: nums[i] % 2 == 0, range(len(nums))]


# list comprehension
def func_4(nums):
    return [i for i in range(len(nums)) if i % 2 == 0]


n = [el for el in range(10000)]
print(f'func_1 - {timeit.timeit("func_1(n)", globals=globals(), number=1000)} сек.')
print(f'func_2 - {timeit.timeit("func_2(n)", globals=globals(), number=1000)} сек.')
print(f'func_3 - {timeit.timeit("func_3(n)", globals=globals(), number=1000)} сек.')
print(f'func_4 - {timeit.timeit("func_4(n)", globals=globals(), number=1000)} сек.')

'''
Результат
func_1 - 0.7926532 сек. 
func_2 - 0.6320608999999999 сек. list comprehension c enumerate более быстрый, но уступает list comprehension
func_3 - 0.00037519999999990894 сек.
func_4 - 0.5321589 сек.
Выводы
Цикл for самый медленный. Функция с list comprehension c enumerate дала более быстрые результаты, 
но уступила list comprehension. Во всех этих трех фукциях оспользуется цикл for. Фукция с lambda оказалась самой бстрой, 
по все   видимости это из за анонимного вызова.

'''
