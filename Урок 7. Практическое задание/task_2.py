"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Хотя в примерах к уроку уже есть вариант реализации слияния,
попробуйте предложить другой (придумать или найти).

И попытаться сделать замеры на массивах разной длины: 10, 100, 1000, ...

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""

from timeit import timeit
from random import uniform


def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result


def merge_sort(lst):
    if len(lst) < 2:
        return lst[:]
    else:
        middle = int(len(lst) / 2)
        left = merge_sort(lst[:middle])
        right = merge_sort(lst[middle:])

        return merge(left, right)


orig_list = [uniform(0, 50) for i in range(5)]
print(orig_list)
print(merge_sort(orig_list))

# замеры 10
orig_list_10 = [uniform(0, 50) for _ in range(10)]
print()
print(f'замеры 10')
print(
    timeit(
        "merge_sort(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list_100 = [uniform(0, 50) for _ in range(100)]
# замеры 100
print()
print(f'замеры 100')
print(
    timeit(
        "merge_sort(orig_list[:])",
        globals=globals(),
        number=1000))

# замеры 1000
orig_list_1000 = [uniform(0, 50) for _ in range(1000)]
print()
print(f'замеры 1000')
print(
    timeit(
        "merge_sort(orig_list[:])",
        globals=globals(),
        number=1000))


"""
[43.095011251352524, 24.185556409293017, 15.975941293839597, 12.469394241049681, 21.126611972889602]
[12.469394241049681, 15.975941293839597, 21.126611972889602, 24.185556409293017, 43.095011251352524]

замеры 10
0.005598299999999997

замеры 100
0.005607499999999994

замеры 1000
0.0128377
"""