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


# меняем цикл на list comprehension:
# избавляемся от операций создания пустого массива и аппенд
def func_2(nums):
    return [i for i in range(len(nums)) if nums[i] % 2 == 0]


# меняем меняем range(len(nums)) на enumerate(nums):
# проходит циклом сразу по элементам массива с получением номера элемента
def func_3(nums):
    return [i for i, num in enumerate(nums) if num % 2 == 0]


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 0, 9]

# по замерам вторая немного быстрее первой, в то время как третья заметно быстрее

print('func_1:', timeit('func_1(numbers)', globals=globals()))
print('func_2:', timeit('func_2(numbers)', globals=globals()))
print('func_3:', timeit('func_3(numbers)', globals=globals()))