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
from random import randint
from timeit import timeit
from collections import deque
from itertools import islice


def merge_sort(left):  # способ с использованием класса deque из модуля collections.

    center = len(left) // 2
    left, right = deque(islice(left, 0, center)), deque(islice(left, center, len(left)))

    if len(left) > 1 or len(right) > 1:
        left, right = merge_sort(left), merge_sort(right)

    result = deque()

    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left.popleft())
        else:
            result.append(right.popleft())
    while len(left):
        result.append(left.popleft())
    while len(right):
        result.append(right.popleft())
    return result


def merge_sort_nominal(lst_obj):  # способ разобранный в качестве примера на уроке.
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


def merge_sort_inverse(left):  # способ аналогичный первому, но без использования деки, сортирующий в обратном порядке.

    center = len(left) // 2
    left, right = left[:center], left[center:]

    if len(left) > 1 or len(right) > 1:
        left, right = merge_sort_inverse(left), merge_sort_inverse(right)

    result = []

    while len(left) > 0 and len(right) > 0:
        if left[-1] <= right[-1]:
            result.insert(0, left.pop())
        else:
            result.insert(0, right.pop())
    while len(left):
        result.insert(0, left.pop())
    while len(right):
        result.insert(0, right.pop())
    return result


orig_list_10 = [randint(0, 49) for i in range(10)]
orig_list_100 = [randint(0, 49) for j in range(100)]
orig_list_1000 = [randint(0, 49) for k in range(1000)]

print(orig_list_100)
print()
print(merge_sort((orig_list_100[:])))
print()
print(merge_sort_inverse((orig_list_100[:])))
print(
    timeit(
        "merge_sort(orig_list_10[:])",
        globals=globals(),
        number=10000))
# time = 0.23533555900000003 sec
print(
    timeit(
        "merge_sort(orig_list_100[:])",
        globals=globals(),
        number=10000))
# time = 3.560612226 sec
print(
    timeit(
        "merge_sort(orig_list_1000[:])",
        globals=globals(),
        number=10000))
# time = 43.221397642 sec — согласно замерам прослеживается сложность N*log(N), если смотреть в сравнении на графике,
# то рост даже более плавный, чем у «каноничной» зависимости.
print(
    timeit(
        "merge_sort_nominal(orig_list_100[:])",
        globals=globals(),
        number=10000))
# time = 3.5171160519999987 sec
print(
    timeit(
        "merge_sort_inverse(orig_list_100[:])",
        globals=globals(),
        number=10000))
# time = 3.369044879999997 sec
