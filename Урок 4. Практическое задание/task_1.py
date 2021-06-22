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


time_func_1 = timeit(
"""
def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr
func_1(range(10))
""", number=10000)

time_func_2 = timeit(
"""
def func_2(nums):
    return list(nums)
func_2(range(10))
""", number=10000)

time_func_3 = timeit(
"""
def func_3(nums):
    return [i for i in nums]
func_3(range(10))
""", number=1000)


print(f'\nResult append time {time_func_1}.')
print(f'Result list time {time_func_2}.')
print(f'Result comprehension time {time_func_3}.')


"""
    Как и разбирали на уроке встроинная функция list отрабатывает в разы быстрее append, но в этом случае выигрывает 
comprehension по времени. Поэтому по праву func_3 можно считать лучшим вараинтом оптимизации кода.

Result append time 0.024277899999999998.
Result list time 0.0029961000000000015.
Result comprehension time 0.00046940000000000176.

    Не стал разбирать конкатинцаию, т.к. из без тестов понятно на сколько тот проигрывает во времени.
"""
