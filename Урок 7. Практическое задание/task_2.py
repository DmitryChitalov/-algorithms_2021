"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Хотя в примерах к уроку уже есть вариант реализации слияния,
попробуйте предложить другой (придумать или найти)

И попытаться сделать замеры на массивах разной длины: 10, 100, 1000, ...

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""
from random import random
import timeit

"""
Прямое слияние Боуза-Нельсона - можно рассматривать как разновидность алгоритма сортировки слиянием,
хотя по сути это сортировочная сеть. Суть ее заключается в том, что все подмассивы можно сортировать параллельно
на каждом этапе. 
"""


def bose_nelson(data):
    """
    Прямое слияние Боуза-Нельсона - можно рассматривать как разновидность алгоритма сортировки слиянием,
    хотя по сути это сортировочная сеть. Суть ее заключается в том, что все подмассивы можно сортировать параллельно
    на каждом этапе.
    """

    def bose_nelson_merge(j, r, m):
        if j + r < len(data):
            if m == 1:
                if data[j] > data[j + r]:
                    data[j], data[j + r] = data[j + r], data[j]
            else:
                m = m // 2
                bose_nelson_merge(j, r, m)
                if j + r + m < len(data):
                    bose_nelson_merge(j + m, r, m)
                bose_nelson_merge(j + m, r - m, m)
        return data

    m = 1
    while m < len(data):
        j = 0
        while j + m < len(data):
            bose_nelson_merge(j, m, m)
            j = j + m + m
        m = m + m
    return data


def merge_sort(lst_obj):
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


orig_list = [random() * 50 for _ in range(10)]

# замеры 10
print(
    timeit.timeit(
        "merge_sort(orig_list[:])",
        globals=globals(),
        number=1000))

print(
    timeit.timeit(
        "bose_nelson(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [random() * 50 for _ in range(100)]

# замеры 100
print(
    timeit.timeit(
        "merge_sort(orig_list[:])",
        globals=globals(),
        number=1000))

print(
    timeit.timeit(
        "bose_nelson(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [random() * 50 for _ in range(1000)]

# замеры 1000
print(
    timeit.timeit(
        "merge_sort(orig_list[:])",
        globals=globals(),
        number=1000))

print(
    timeit.timeit(
        "bose_nelson(orig_list[:])",
        globals=globals(),
        number=1000))

my_lst = [random() * 50 for i in range(10)]
print(my_lst)
print(bose_nelson(my_lst[:]))
print(merge_sort(my_lst))
