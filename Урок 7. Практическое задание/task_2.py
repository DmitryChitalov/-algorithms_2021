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


def merge_sort(A):
    if len(A) == 1 or len(A) == 0:
        return
    L, R = A[:len(A) // 2], A[len(A) // 2:]
    merge_sort(L)
    merge_sort(R)
    n = m = k = 0
    C = [0] * (len(L) + len(R))
    while n < len(L) and m < len(R):
        if L[n] <= R[m]:
            C[k] = L[n]
            n += 1
        else:
            C[k] = R[m]
            m += 1
        k += 1
    while n < len(L):
        C[k] = L[n]; n += 1; k += 1
    while m < len(R):
        C[k] = R[m]; m += 1; k += 1
    for i in range(len(A)):
        A[i] = C[i]
    return A


orig_list = [random.uniform(0, 50) for _ in range(5)]
print(orig_list)
print(merge_sort(orig_list))

orig_list = [random.uniform(0, 50) for _ in range(10)]

print(
    timeit.timeit(
        "merge_sort(orig_list.copy())",
        globals=globals(),
        number=1000))

orig_list = [random.uniform(0, 50) for _ in range(100)]

print(
    timeit.timeit(
        "merge_sort(orig_list.copy())",
        globals=globals(),
        number=1000))

orig_list = [random.uniform(0, 50) for _ in range(1000)]

print(
    timeit.timeit(
        "merge_sort(orig_list.copy())",
        globals=globals(),
        number=1000))


"""
0.043170552991796285
0.3460975990165025
4.110839213011786
"""