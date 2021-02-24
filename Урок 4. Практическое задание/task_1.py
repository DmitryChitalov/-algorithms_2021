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
from timeit import timeit
from random import randint


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    new_arr = []
    for i in range(len(nums), 0, -1):
        if nums.pop() % 2 == 0:
            new_arr.append(i)
    return new_arr


n = [randint(0, 100) for i in range(100)]

print(timeit("func_1(n)", globals=globals()))  # 17.412999000000003
print(timeit("func_2(n)", globals=globals()))  # 0.6184783999999972

"""
Вывод:
Обращение по индексу к элементу в списке значиетльно медленнее,
чем получение элемента из конца списка.
По-этому вторая функция отрабатывает значительно быстрее
"""
