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


from timeit import Timer
from random import randint

n = [randint(1, 1000) for i in range(20)]

def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


"""
оптимизации:
1. цикл на основе enumerate, чтобы повторно не обращаться к списку
2. результат операции (i%2) использую как готовое условие, т.к. равен 0 или 1
3. если бы, было много повторов в списке, то можно было бы сделать мемоизацию
"""


def func_2(nums):
    new_arr = []
    for c, i in enumerate(nums):
        if not i % 2:
            new_arr.append(c)
    return new_arr


print(n)
print(func_1(n))
print(func_2(n))


t1 = Timer("func_1(n)", "from __main__ import func_1, n")
print("func_1=", t1.timeit(10000), "milliseconds")

t2 = Timer("func_2(n)", "from __main__ import func_2, n")
print("func_2=", t2.timeit(10000), "milliseconds")