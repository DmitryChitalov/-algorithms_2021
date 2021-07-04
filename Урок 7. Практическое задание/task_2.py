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


def merge(A, B):
    Res = []
    i = 0
    j = 0
    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            Res.append(A[i])
            i += 1
        else:
            Res.append(B[j])
            j += 1
    Res += A[i:] + B[j:]
    return Res


def MergeSort(A):
    if len(A) <= 1:
        return A
    else:
        L = A[:len(A) // 2]
        R = A[len(A) // 2:]
    return merge(MergeSort(L), MergeSort(R))


n = int(input('Введите число\n'))
spam = [random() * 50 for _ in range(n)]
print(spam)
print(MergeSort(spam[:]))

print(timeit("MergeSort([random() * 50 for _ in range(10)])", globals=globals(), number=10000))
# 0.1162139249999985
print(timeit("MergeSort([random() * 50 for _ in range(100)])", globals=globals(), number=10000))
# 1.7108501490000005
print(timeit("MergeSort([random() * 50 for _ in range(1000)])", globals=globals(), number=10000))
# 24.103024502
