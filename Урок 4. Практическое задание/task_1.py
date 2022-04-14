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


def func_list_comp(nums):                                                       # пробуем list comprehensions
    return [i for i in range(len(nums)) if nums[i] % 2 == 0]


def func_enum(nums):                                                       # пробуем enumerate()
    return [j for i, j in enumerate(nums) if not i % 2]


def func_set_comp(nums):                                                       # пробуем set comprehension (уникальные)
    return {i for i in range(len(nums)) if nums[i] % 2 == 0}


print(f'Время выполнения функции {timeit("func_1([i for i in range(1000)])", globals=globals(), number=10000)} сек.')
print(f'Время выполнения функции {timeit("func_list_comp([i for i in range(1000)])", globals=globals(), number=10000)} сек.')
print(f'Время выполнения функции {timeit("func_enum([i for i in range(1000)])", globals=globals(), number=10000)} сек.')
print(f'Время выполнения функции {timeit("func_set_comp([i for i in range(1000)])", globals=globals(), number=10000)} сек.')

#Получены следующие результаты:
# Время выполнения func_1 функции 1.885909197 сек.
# Время выполнения func_list_comp функции 1.673692581 сек.
# Время выполнения func_enum функции 1.3836508949999997 сек.
# Время выполнения func_set_comp функции 1.708031311 сек.

# Использование list comprehensions ускоряет работу кода, потому что это встроенный в Python механизм генерации списков,
# выдает готовый список не занимаясь созданием нового, как бы "фильтрует".
# В отличии от list comprehensions, enumerate() хотя и тоже встроена в Python, но работает всего с 2 значениями(сам элемент и индекс)
# В 4 функции использовал set comprehension, сработал дольше предыдущих кроме цикла за счет того что дополнительно преверял на дубликаты