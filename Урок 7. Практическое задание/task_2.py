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


import timeit
import random


def merge_sort(arr):

    def merge(fst, snd):
        res = []
        i, j = 0, 0

        while i < len(fst) and j < len(snd):

            if fst[i] < snd[j]:
                res.append(fst[i])
                i += 1

            else:
                res.append(snd[j])
                j += 1

        res.extend(fst[i:] if i < len(fst) else snd[j:])

        return res

    def div_half(lst):

        if len(lst) == 1:
            return lst

        elif len(lst) == 2:
            return lst if lst[0] <= lst[1] else lst[::-1]

        else:
            return merge(div_half(lst[:len(lst)//2]), div_half(lst[len(lst)//2:]))

    return div_half(arr)


SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 50
array = [random.uniform(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print('Массив:', array, sep='\n')
# print('После сортировки:', merge_sort(array), sep='\n')

print(
    timeit.timeit(
        "merge_sort(array[:])",
        globals=globals(),
        number=1000))


def merge_sort_lesson(lst_obj):
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


orig_list = array.copy()

# замеры 10
print(
    timeit.timeit(
        "merge_sort_lesson(orig_list[:])",
        globals=globals(),
        number=1000))

SIZE = 100
array = [random.uniform(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
orig_list = array.copy()
print('_' * 100)

print(
    timeit.timeit(
        "merge_sort(array[:])",
        globals=globals(),
        number=1000))

print(
    timeit.timeit(
        "merge_sort_lesson(orig_list[:])",
        globals=globals(),
        number=1000))

SIZE = 1000

array = [random.uniform(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
orig_list = array.copy()
print('_' * 100)

print(
    timeit.timeit(
        "merge_sort(array[:])",
        globals=globals(),
        number=1000))

print(
    timeit.timeit(
        "merge_sort_lesson(orig_list[:])",
        globals=globals(),
        number=1000))

# Нашёл немного другую вариацию реализации слияния с двумя массивами, но разницы особо не видно:
# Замеры:
# Массив 10:
# [21.543229880967836, 25.46680050549722, 15.611573329668804, 8.131684624002855,
# 44.15515148762157, 0.8772329577837301, 0.3236534609754482, 29.362914080042113, 47.17699107592417, 36.460499493067466]
# 0.006954099999999998
# 0.006057799999999999
# ____________________________________________________________________________________________________
# Массив 100:
# 0.1038343
# 0.10286379999999998
# ____________________________________________________________________________________________________
# # Массив 1000:
# 1.4287237
# 1.3877278000000002
