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

from timeit import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):                                                       # использование list comprehensions
    return [i for i in range(len(nums)) if nums[i] % 2 == 0]

def func_3(nums):                                                       # использование enumerate()
    return [v for k, v in enumerate(nums) if not k % 2]

def func_4(nums):                                                       # использование set comprehension (ищит уникальные элементы)
    return {i for i in range(len(nums)) if nums[i] % 2 == 0}

#numbers = [1, 2, 3, 4, 5, 6]                                           # пробовал, но выдал ошибку потому что в лямбду
#indx_numb = list(filter(lambda x: numbers[x] % 2 == 0, numbers))       # передаётся сам элемент, а не его индекс, как сделать иначе не знаю

print(f'Время выполнения функции {timeit("func_1([i for i in range(1000)])", globals=globals(), number=10000)} сек.')
print(f'Время выполнения функции {timeit("func_2([i for i in range(1000)])", globals=globals(), number=10000)} сек.')
print(f'Время выполнения функции {timeit("func_3([i for i in range(1000)])", globals=globals(), number=10000)} сек.')
print(f'Время выполнения функции {timeit("func_4([i for i in range(1000)])", globals=globals(), number=10000)} сек.')

#Получены следующие результаты:
# Время выполнения 1 функции 1.2708782 сек.
# Время выполнения 2 функции 1.0811723 сек.
# Время выполнения 3 функции 1.0350400999999998 сек.
# Время выполнения 4 функции 1.1513689 сек.
# Использование list comprehensions ускоряет работу кода, потому что это встроенный в Python механизм генерации списков,
# выдает готовый список не занимаясь созданием нового, как бы "фильтрует".
# В отличии от list comprehensions, enumerate() хотя и тоже встроена в Python, но работает всего с 2 значениями(сам элемент и индекс)
# В 4 функции использовал set comprehension, сработал дольше предыдущих кроме цикла за счет того что дополнительно преверял на дубликаты
