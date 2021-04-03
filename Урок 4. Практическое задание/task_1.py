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


numbers_list = [1, 2, 3, 4, 5, 6, 7]


def func_1(nums):

    new_list = []

    for i in range(len(nums)):

        if nums[i] % 2 == 0:

            new_list.append(i)

    return new_list


print('1 -- ', timeit.timeit('func_1(numbers_list)', 'from __main__ import func_1, numbers_list', number=1000))


def func_2(numbers_list):

    total = [i for j, i in enumerate(numbers_list) if not j % 2]


print('2 -- ', timeit.timeit('func_2(numbers_list)', 'from __main__ import func_2, numbers_list', number=1000))


def func_3(numbers_list):

   numbers_list[::2]


print('3 -- ', timeit.timeit('func_3(numbers_list)', 'from __main__ import func_3, numbers_list', number=1000))


def func_4(numbers_list):

    for i in range(0, len(numbers_list), 2):

        True


print('4 -- ', timeit.timeit('func_4(numbers_list)', 'from __main__ import func_4, numbers_list', number=1000))

func_2(numbers_list)

"""

1ый вариант медленнее 4го, потому чтоу  нас просиходит перебор абсолютно всех элементов и только потом проверка
деления на остаток. В 4ом варианте мы перебираем по одному, из-за этого перебор становится в 2 раза меньше.
3ий вариант тоже быстрее исходного, так как мы береа по каждому 2ому элементу (не перебираем все, поэтому и быстрее).
2ой вариант тоже быстрее исходного, так как enumerate сам перебирает индексы, а потом идет
обычная проверка на четность (этот варинт самый быстрый).

Значения с моего компьюетра:
1 --  0.0006564000000000014
2 --  0.0005964999999999998
3 --  0.00012090000000000017
4 --  0.0002488000000000004
с помощью их, можно проверить точность моей аналитики.

"""

