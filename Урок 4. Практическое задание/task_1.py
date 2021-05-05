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
from timeit import timeit, default_timer

nums_list = [100, 100, 123, 1429, 1, 31, 341, 342, 2523, 63, 100, 100, 12, 2345124, 1243]


def deco(n=10000):  # функция декоратор для подсчёта среднего времени выполнения n запусков
    def time_it(func):
        print(f'{func.__name__}:', end=' ')

        def wrapper(numb):
            sum_time = []
            for i in range(n):
                start_time = default_timer()
                func(numb)
                sum_time.append(default_timer() - start_time)
            average_time = sum(sum_time)/n
            return average_time
        return wrapper
    return time_it


@deco()
def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


# print(func_1(nums_list))
time1 = timeit(
        "func_1(nums_list)",
        setup="from __main__ import func_1, nums_list",
        number=10)
print(f'{round(time1, 3)} сек.')


@deco()
def optimized_func_1(nums):
    """
        Используем списковое включение,
        итерируемся с помощью специальной функции enumerate для получения элемента и его индекса,
        заменяем логическое выражение, оставляя его без сравнивания с нулём
    """
    return [i for i, num in enumerate(nums) if not num % 2]


# print(optimized_func_1(nums_list))
time2 = timeit(
        "optimized_func_1(nums_list)",
        setup="from __main__ import optimized_func_1, nums_list",
        number=10)
print(f'{round(time2, 3)} сек.')

print(f'Как видно из результатов, производительность выросла на {round((time1-time2)/time1*100, 1)} процентов')
