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

def new_lst(user_numbers):
    cnt = 0
    orig_list = []
    while cnt < user_numbers:
        new_num = random.random() * 50
        orig_list.append(new_num)
        cnt += 1
    return orig_list

user_numbers = int(input('Введите число элементов: '))
orig_list = new_lst(user_numbers)
print(f'Новый массив:{orig_list}')
print(f'Отсортированный по возрастанию: {merge_sort(orig_list)}')


# Замеры
print(
    timeit.timeit(
        "merge_sort(new_lst(10))",
        globals=globals(),
        number=1000))
print(
    timeit.timeit(
        "merge_sort(new_lst(100))",
        globals=globals(),
        number=1000))
print(
    timeit.timeit(
        "merge_sort(new_lst(1000))",
        globals=globals(),
        number=1000))

"""
0.02551139999999963
0.39926459999999997
6.544694
"""

