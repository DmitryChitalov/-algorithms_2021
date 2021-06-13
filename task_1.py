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
from random import randint
from timeit import timeit, repeat, default_timer


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_simplified(nums):
    new_arr = [number for number, el in enumerate(nums) if el % 2 == 0]
    return new_arr


nums = [randint(1, 10000) for el in range(1, 100000)]

print(timeit("func_1(nums)", globals=globals(), number=100))
print(timeit("func_simplified(nums)", globals=globals(), number=100))


setup = """
from random import randint
nums = [randint(1, 10000) for el in range(1, 100000)]
def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr
def func_simplified(nums):
    new_arr = [number for number, el in enumerate(nums) if el % 2 == 0]
    return new_arr
"""

statements = ["func_1(nums)", "func_simplified(nums)"]

for st in statements:
    print(repeat(st, setup, default_timer, 3, 100))

"""
Запуск 1:
0.7034294999999999
0.5823429
[0.6568506000000003, 0.6559984000000001, 0.6493831000000001]
[0.5730233000000005, 0.5733457, 0.5736523]

Запуск 2:
0.706507
0.5646665000000001
[0.6496501999999997, 0.7308712000000002, 0.6764063999999999]
[0.6501956000000004, 0.6623153000000004, 0.5641611000000006]

Запуск 3:
0.6644796000000001
0.568535
[0.6459163000000001, 0.6473067000000001, 0.6440108000000002]
[0.5721562999999996, 0.5641093000000001, 0.5643495999999999]

В 3 из 3 запусков функция с генератором выполняется быстрее, чем функция с итератором, 
так как намного эффективнее используют память при работе с большими наборами данных.
Также, была попытка написать код через лямбду, но применение данной функии потребовало использование еще 
встроенных функций list и filter, что значительно увеличивало время работы функции.
"""