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
from timeit import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    new_arr = [num for num in range(len(nums)) if nums[num] % 2 == 0]
    return new_arr


list_for_fun = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f'Функция - 1, время: {timeit("func_1(list_for_fun)", globals=globals(), number=10000)}')
print(f'Функция - 1, время: {timeit("func_1(list_for_fun)", globals=globals(), number=100000)}')
print(f'Функция - 2, время: {timeit("func_1(list_for_fun)", globals=globals(), number=10000)}')
print(f'Функция - 2, время: {timeit("func_1(list_for_fun)", globals=globals(), number=100000)}')

"""
Результат работы на моем пк:
Функция - 1, время: 0.012027200000000002
Функция - 1, время: 0.1166905
Функция - 2, время: 0.009281099999999987
Функция - 2, время: 0.0934728

Функция - 2, была переделана, а именно, замена инерируемого списка с функцией
добавления append, на лист компрехеншн с условием.

Вывод:
Списковое включение работает быстрее, чем интерируемый список с фукнций добавления.
Тесты показали, что данная оптимизация кода имеет место быть.

"""
