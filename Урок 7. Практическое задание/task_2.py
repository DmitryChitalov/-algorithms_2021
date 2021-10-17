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

from random import random
from timeit import timeit


def merge_sort_from_lesson(lst_obj):
    if len(lst_obj) > 1:
        center = len(lst_obj) // 2
        left = lst_obj[:center]
        right = lst_obj[center:]

        merge_sort(left)
        merge_sort(right)

        # перестали делить
        # выполняем слияние
        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lst_obj[k] = left[i]
                i += 1
            else:
                lst_obj[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            lst_obj[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            lst_obj[k] = right[j]
            j += 1
            k += 1
        return lst_obj


def merge_sort(array):
    array_length = len(array)
    if array_length <= 1:
        return

    fst_part = array[:array_length // 2]
    snd_part = array[array_length // 2:]
    fst_part_len = len(fst_part)
    snd_part_len = len(snd_part)

    # print(fst_part)
    # print(snd_part)

    merge_sort(fst_part)
    merge_sort(snd_part)

    sorted_array = [0] * array_length
    one_index, two_index, sorted_index = 0, 0, 0

    for sorted_index in range(array_length):
        if one_index == fst_part_len or two_index == snd_part_len:
            break
        else:
            if fst_part[one_index] <= snd_part[two_index]:
                sorted_array[sorted_index] = fst_part[one_index]
                one_index += 1
            else:
                sorted_array[sorted_index] = snd_part[two_index]
                two_index += 1

    while one_index < fst_part_len and sorted_index < array_length:
        sorted_array[sorted_index] = fst_part[one_index]
        sorted_index += 1
        one_index += 1

    while two_index < snd_part_len and sorted_index < array_length:
        sorted_array[sorted_index] = snd_part[two_index]
        sorted_index += 1
        two_index += 1

    for i in range(array_length):
        array[i] = sorted_array[i]

    return array


if __name__ == '__main__':
    # SIZE = 10   # Execution time for 10 elements array for merge_sort function is 0.006067699999999999
    # SIZE = 100    # Execution time for 100 elements array for merge_sort function is 0.09316529999999999
    SIZE = 1000     # Execution time for 1000 elements array for merge_sort function is 1.1693152
    a = [random() * 49 for _ in range(SIZE)]

    print(a)
    print(merge_sort(a[:]))
    print(f"Execution time for {SIZE} elements array for merge_sort function is "
          f"{timeit('merge_sort(a[:])', number=500, globals=globals())}")
    print(f"Execution time for {SIZE} elements array for merge_sort_from_lesson function is "
          f"{timeit('merge_sort_from_lesson(a[:])', number=500, globals=globals())}")
