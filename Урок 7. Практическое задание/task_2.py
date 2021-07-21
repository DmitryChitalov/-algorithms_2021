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
from random import randint, random
from timeit import timeit


# Вариант алгоритма через  рекурсию. Сложность N*log(N).

def mergeSort(A):
    if len(A) <= 1:
        return A
    else:
        L = A[:len(A) // 2]
        R = A[len(A) // 2:]
    return merge(mergeSort(L), mergeSort(R))


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


unsorted_lst_10 = [random() * randint(0, 50) for i in range(10)]
print(f'Массив на 10 эл-ов {unsorted_lst_10}')
print(f'Отсортированный массив на 10 эл-ов{mergeSort(unsorted_lst_10)}')
unsorted_lst_100 = [random() * randint(0, 50) for i in range(100)]
print(f'Массив на 100 эл-ов {unsorted_lst_100}')
print(f'Отсортированный массив на 100 эл-ов{mergeSort(unsorted_lst_100)}')
unsorted_lst_1000 = [random() * randint(0, 50) for i in range(1000)]
print(f'Массив на 1000 эл-ов {unsorted_lst_1000}')
print(f'Отсортированный массив на 1000 эл-ов{mergeSort(unsorted_lst_1000)}')

# Замеры

print(
    timeit(
        "mergeSort(unsorted_lst_10[:])",
        globals=globals(),
        number=1000))

print(
    timeit(
        "mergeSort(unsorted_lst_100[:])",
        globals=globals(),
        number=1000))

print(
    timeit(
        "mergeSort(unsorted_lst_1000[:])",
        globals=globals(),
        number=1000))
