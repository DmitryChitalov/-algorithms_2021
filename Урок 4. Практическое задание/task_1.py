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


# Сложность: O(N)
def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


# Сложность: O(N); Однако элемент ищется не по индексу
# (просто рассматривается каждый элемент из списка на факт соответствия условию),
# что упрощает функцию и делает время её выполнения короче
def func_2(nums):
    new_arr = []
    for i in nums:
        if i % 2 == 0:
            new_arr.append(i)
    return new_arr


# Сложность: O(N)
# Время выполнения уменьшается за счёт того,
# что list comprehension отрабатывает значительно быстрее обычной реализации итератора
def func_3(nums):
    new_arr = [i for i in nums if i % 2 == 0]
    return new_arr


n = [i for i in range(10)]


print(func_1(n))
print(timeit("func_1(n)", globals=globals()))

print(func_2(n))
print(timeit("func_2(n)", globals=globals()))

print(func_3(n))
print(timeit("func_3(n)", globals=globals()))
