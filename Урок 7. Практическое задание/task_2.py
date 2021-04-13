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
from timeit import timeit


def merge_sort(arr):

    if len(arr) > 1:
        middle = len(arr) // 2
        lefthalf = arr[:middle]
        righthalf = arr[middle:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                arr[k] = lefthalf[i]
                i += 1
            else:
                arr[k] = righthalf[j]
                j += 1
            k += 1

        while i < len(lefthalf):
            arr[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            arr[k] = righthalf[j]
            j += 1
            k += 1


n = int(input("Введите число элементов: "))
lst = [random()*50 for i in range(n)]

print(f"Исходный - {lst}")
merge_sort(lst)
print(f"Отсортированный - {lst}")
print(timeit('merge_sort(lst[:])',
             number=1000,
             globals=globals()))

"""
Введите число элементов: 10
Исходный - [44.69325460064689, 4.298240030024747, 28.057050265715123, 13.903067002612696, 49.39551503322306, ... ]
Отсортированный - [2.9580803409690604, 4.298240030024747, 13.903067002612696, 17.34142720001265, 19.75690267151234, ...]
0.01776809999999962

Введите число элементов: 100
Исходный - [0.7862477440415572, 37.93315343243173, 38.13442414502006, 37.24247124637726, 18.830357913317116, ....]
Отсортированный - [0.4860615726487716, 0.5927811585670406, 0.7862477440415572, 0.8438984830480889, 0.9526869937299,...]
0.3042473000000001

Введите число элементов: 1000
Исходный - [6.035077051583693, 16.58192445973644, 35.23343779090707, 43.58334520274202, 10.841252050000211, ...]
Отсортированный - [0.06192983029366661, 0.14612493380231628, 0.15247242259944782, 0.1647507768013201, ...]
4.199794000000001
"""
