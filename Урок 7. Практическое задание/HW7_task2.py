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

from random import uniform
from timeit import timeit


def merge_list(some_list):
    sorted_list = []
    if len(some_list) <= 1:
        return some_list
    middle_of_list = len(some_list) // 2
    left_list = (some_list[:middle_of_list])
    right_list = (some_list[middle_of_list:])

    left_index = right_index = 0

    left_length, right_length = len(left_list), len(right_list)
    summarylength = left_length + right_length
    i = 0
    while i <= summarylength:
        if left_index < left_length and right_index < right_length:
            if left_list[left_index] <= right_list[right_index]:
                sorted_list.append(left_list[left_index])
                left_index += 1
            else:
                sorted_list.append(right_list[right_index])
                right_index += 1
        elif left_index >= left_length and right_index < right_length:
            sorted_list.append(right_list[right_index])
            right_index += 1
        elif right_index >= right_length and left_index < left_length:
            sorted_list.append(left_list[left_index])
            left_index += 1

        i += 1
    return sorted_list


# сделаем замеры на массивах разной длины
lst_1 = [uniform(0, 50) for _ in range(100)]

print('Время выполнения merge_list() при длине массива 100: ', timeit(
    'merge_list(lst_1[:])',
    globals=globals(),
    number=100
))

lst_2 = [uniform(0, 50) for _ in range(1000)]
print('Время выполнения merge_list() при длине массива 1000: ', timeit(
    'merge_list(lst_2[:])',
    globals=globals(),
    number=100
))

lst_3 = [uniform(0, 50) for _ in range(10000)]
print('Время выполнения merge_list() при длине массива 10000: ', timeit(
    'merge_list(lst_3[:])',
    globals=globals(),
    number=100
))




"""
Время выполнения merge_list() при длине массива 100:  0.002044899999999572
Время выполнения merge_list() при длине массива 1000:  0.020780799999998933
Время выполнения merge_list() при длине массива 10000:  0.23889239999999923