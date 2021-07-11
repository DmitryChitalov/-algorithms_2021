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
import random
from timeit import timeit

def merge(left_list, right_list):
    sorted_list = []
    left_list_index = right_list_index = 0
    for _ in range(len(left_list) + len(right_list)):
        if left_list_index < len(left_list) and right_list_index < len(right_list):
            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1
        elif left_list_index == len(left_list):
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1
        elif right_list_index == len(right_list):
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1
    return sorted_list

def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left_list = merge_sort(lst[:mid])
    right_list = merge_sort(lst[mid:])
    return merge(left_list, right_list)

n = int(input('Введите число элементов:'))
lst = [random.uniform(0, 50) for _ in range(n)]

lst_10 = [random.uniform(0, 50) for _ in range(10)]
print(
    timeit(
        "merge_sort(lst_10[:])",
        globals=globals(),
        number=1000))

lst_100 = [random.uniform(0, 50) for _ in range(100)]
print(
    timeit(
        "merge_sort(lst_100[:])",
        globals=globals(),
        number=1000))

lst_1000 = [random.uniform(0, 50) for _ in range(1000)]
print(
    timeit(
        "merge_sort(lst_1000[:])",
        globals=globals(),
        number=1000))

print(lst)
print(merge_sort(lst))