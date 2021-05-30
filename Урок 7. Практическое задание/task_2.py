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


from random import uniform
from timeit import timeit

n = int(input("Введите число элементов: "))


def merge_sort(lst_obj):
    if len(lst_obj) > 1:
        center = len(lst_obj) // 2
        right = lst_obj[center:]
        left = lst_obj[:center]

        merge_sort(right)
        merge_sort(left)

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


real_list = [uniform(1, 50) for _ in range(n)]
print(f"Исходный -        {real_list}")
print(f"Отсортированный - {merge_sort(real_list)}")

# замеры 10
print(
    timeit(
        "merge_sort(real_list[:])",
        globals=globals(),
        number=10000))

real_list = [uniform(1, 50) for _ in range(100)]

# замеры 100
print(
    timeit(
        "merge_sort(real_list[:])",
        globals=globals(),
        number=10000))

real_list = [uniform(1, 50) for _ in range(1000)]

# замеры 1000
print(
    timeit(
        "merge_sort(real_list[:])",
        globals=globals(),
        number=10000))

"""
Введите число элементов: 5
Исходный -        [22.961794134932795, 34.7616096184703, 7.451986615232771, 24.837726510670095, 26.20300550432546]
Отсортированный - [7.451986615232771, 22.961794134932795, 24.837726510670095, 26.20300550432546, 34.7616096184703]
0.036169700000000304
1.8569133000000004
24.4900363
"""
