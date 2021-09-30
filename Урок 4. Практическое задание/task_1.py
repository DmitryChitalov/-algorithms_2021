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

import timeit

my_list = list(range(3000))


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


t1 = timeit.timeit(stmt='func_1(my_list)', setup='from __main__ import func_1, my_list')
print('func_1', t1, 'seconds')  # В среднем: на 1000 элементов 55 секунд, на 2000 - 117 сек, на 3000 - 164 сек


def func_2(nums):
    new_arr = []
    z = 0
    for i in nums:
        if i % 2 == 0:
            new_arr.append(z)
            z += 1
        else:
            z += 1
    return new_arr


t2 = timeit.timeit(stmt='func_2(my_list)', setup='from __main__ import func_2, my_list')
print('func_2', t2, 'seconds')  # В среднем: на 1000 элементов 60 секунд, на 2000 - 120 ,на 3000 - 191 сек


def func_3(nums):
    return [i for i in range(len(nums)) if nums[i] % 2 == 0]


t3 = timeit.timeit(stmt='func_3(my_list)', setup='from __main__ import func_3, my_list')
print('func_3', t3, 'seconds')  # В среднем: на 1000 элементов 46 секунд, на 2000 - 96 сек, на 3000 - 139 сек

'''''
Попытка индексировать элементы "в ручную" в func_2 не принесла результатов, ее контрольное время больше, 
чем у первночальной func_1.
Однако реорганизация функции с помощью list comprehension в func_3 ускорило время выполнения функции. 
Благодоря list compehension нам не нужно иницализировать лишний список, и после заполнять его с помощью append(),
из-за этого выполнение функции проходит намного быстрее.
'''''
