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


def merge_sort(lst_obj):
    if len(lst_obj) > 1:
        center = len(lst_obj) // 2
        left = lst_obj[:center]
        right = lst_obj[center:]

        merge_sort(left)
        merge_sort(right)

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


origin_list_5 = [random.triangular(0, 49) for _ in range(5)]
print(f'Исходный - {origin_list_5}')
print(f'Отсортированный - {merge_sort(origin_list_5)}')
origin_list_10 = [random.triangular(0, 49) for _ in range(10)]
print(f'10 элементов', timeit('merge_sort(origin_list_10[:])', globals=globals(), number=1000))
origin_list_100 = [random.triangular(0, 49) for _ in range(100)]
print(f'100 элементов', timeit('merge_sort(origin_list_100[:])', globals=globals(), number=1000))
origin_list_1000 = [random.triangular(0, 49) for _ in range(1000)]
print(f'1000 элементов', timeit('merge_sort(origin_list_1000[:])', globals=globals(), number=1000))

# Исходный - [7.496832441874139, 23.162435813220988, 25.039743091542796, 26.06336023517397, 37.15331253569335]
# Отсортированный - [7.496832441874139, 23.162435813220988, 25.039743091542796, 26.06336023517397, 37.15331253569335]
# 10 элементов 0.0101745
# 100 элементов 0.3047044
# 100 элементов 3.3504515
# Ни очень быстрое выполнение  уже от 1000 элементов.
