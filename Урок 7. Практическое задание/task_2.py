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
from timeit import timeit
import random


def merge_sort_recurs(lst_obj):  # исходный алгоритм - рекурсивный
    if len(lst_obj) > 1:
        center = len(lst_obj) // 2
        left = lst_obj[:center]
        right = lst_obj[center:]

        merge_sort_recurs(left)
        merge_sort_recurs(right)

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


def merge_sort_iter(lst_obj):  # альтернативный алгоритм - итеративный
    support = lst_obj[:]
    n = len(support)
    size = 1
    while size < n:
        j = 0
        while j < n - size:
            merge(lst_obj, support, j, j + size - 1, j + size, min(j + 2 * size - 1, n - 1))
            j += size * 2
        size = size * 2
    return lst_obj


def merge(lst_obj, support, ls, le, rs, re):
    for i in range(ls, re + 1):
        support[i] = lst_obj[i]
    l = ls
    r = rs
    for i in range(ls, re + 1):
        if l > le:
            lst_obj[i] = support[r]
            r += 1
        elif r > re:
            lst_obj[i] = support[l]
            l += 1
        elif support[l] < support[r]:
            lst_obj[i] = support[l]
            l += 1
        else:
            lst_obj[i] = support[r]
            r += 1
    return None


orig_list = [random.uniform(0, 50) for n in range(10)]
print(orig_list)
print(merge_sort_recurs(orig_list[:]))
print(merge_sort_iter(orig_list[:]))

orig_list = [random.uniform(0, 50) for n in range(10)]
print('Рекурсивный алгоритм, 10 эл-тов:', timeit('merge_sort_recurs(orig_list[:])', globals=globals(), number=1000))
print('Итеративный алгоритм, 10 эл-тов:', timeit('merge_sort_iter(orig_list[:])', globals=globals(), number=1000))
orig_list = [random.uniform(0, 50) for n in range(100)]
print('Рекурсивный алгоритм, 100 эл-тов:', timeit('merge_sort_recurs(orig_list[:])', globals=globals(), number=1000))
print('Итеративный алгоритм, 100 эл-тов:', timeit('merge_sort_iter(orig_list[:])', globals=globals(), number=1000))
orig_list = [random.uniform(0, 50) for n in range(1000)]
print('Рекурсивный алгоритм, 1000 эл-тов:', timeit('merge_sort_recurs(orig_list[:])', globals=globals(), number=1000))
print('Итеративный алгоритм, 1000 эл-тов:', timeit('merge_sort_iter(orig_list[:])', globals=globals(), number=1000))

'''
Алгоритмы имеют одинаковую сложность O(N logN), рекурсивный выполняется немного быстрее

Рекурсивный алгоритм, 10 эл-тов: 0.028356761
Итеративный алгоритм, 10 эл-тов: 0.037938022
Рекурсивный алгоритм, 100 эл-тов: 0.46147415700000005
Итеративный алгоритм, 100 эл-тов: 0.5196910820000001
Рекурсивный алгоритм, 1000 эл-тов: 6.378412496999999
Итеративный алгоритм, 1000 эл-тов: 7.882305422999999
'''