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

# Взял тот же, решил упростить и украсить через доп.функции. День убил. Вышел Франкенштейн. Спасибо, что хоть
# работатет, время такое же почти. Хуже в пределах погрешности.

from random import randint, random
from timeit import timeit

def merge(my_array):
    if len(my_array) > 1:
        center = len(my_array) // 2
        left = my_array[:center]
        right = my_array[center:]
        merge(left)
        merge(right)
        i, j, k = 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                my_array[k] = left[i]
                i += 1
            else:
                my_array[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            my_array[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            my_array[k] = right[j]
            j += 1
            k += 1
        return my_array


my_array = [random()*50 for el in range(50)]  # произвольный массив
print(my_array)
print(merge(my_array[:]))

print(timeit("merge(my_array[:])", globals=globals(), number=10))
print(timeit("merge(my_array[:])", globals=globals(), number=100))
print(timeit("merge(my_array[:])", globals=globals(), number=1000))


def split_in_half(my_array):
    if len(my_array) > 2:
        center = len(my_array) // 2
        left = my_array[:center]
        right = my_array[center:]
        return [split_in_half(left), split_in_half(right)]
    return easy_sort(my_array)


def merge_sorted_parts(super_list):
    if isinstance(super_list[0], list) and isinstance(super_list[0][0], list):
        return merge_sorted_parts([merge_sorted_parts(super_list[0]), merge_sorted_parts(super_list[1])])
    elif isinstance(super_list[1][0], list):
        return merge_sorted_parts([super_list[0], merge_sorted_parts(super_list[1])])
    else:
        i, j, k = 0, 0, 0
        left = super_list[0]
        right = super_list[1]
        my_array = []
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                my_array.append(left[i])
                i += 1
            else:
                my_array.append(right[j])
                j += 1
            k += 1
        while i < len(left):
            my_array.append(left[i])
            i += 1
            k += 1
        while j < len(right):
            my_array.append(right[j])
            j += 1
            k += 1
        return my_array


def easy_sort(my_array):
    if len(my_array) == 2:
        if my_array[0] > my_array[1]:
            my_array[0], my_array[1] = my_array[1], my_array[0]
    return my_array


def merge_sort(my_array):
    if len(my_array) <= 2:
        return easy_sort(my_array)
    return merge_sorted_parts(split_in_half(my_array))

print(my_array)
print(merge_sort(my_array[:]))

print(timeit("merge_sort(my_array[:])", globals=globals(), number=10))
print(timeit("merge_sort(my_array[:])", globals=globals(), number=100))
print(timeit("merge_sort(my_array[:])", globals=globals(), number=1000))








