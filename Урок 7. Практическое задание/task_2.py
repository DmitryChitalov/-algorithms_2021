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

import random
import timeit

# Вариант, найденный в интернете, использует две функции. Суть та же, что на уроке.
# merge_sort - делит список пополам, пока длина списка не будет меньше двух
# merge - берет два входящих списка и строит из них res - отсортированный список.

def merge(list1, list2):
    left = 0
    right = 0
    res = []
    while left < len(list1) and right < len(list2):
        if list1[left] <= list2[right]:
            res.append(list1[left])
            left += 1
        else:
            res.append(list2[right])
            right += 1
    while left < len(list1):
        res.append(list1[left])
        left += 1
    while right < len(list2):
        res.append(list2[right])
        right += 1
    return res

def merge_sort(arr):
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    left = arr[0:mid]
    right = arr[mid:len(arr)]
    return merge(merge_sort(left), merge_sort(right))

list_length = int(input('Введите длину списка:\n'))
unsorted = [random.random() * random.randint(0, 50) for _ in range(list_length)]
print('Неотсортированный список:\n', unsorted)
print('Отсортированный список: \n', merge_sort(unsorted))


# Замеры на массивах разной длины:
list_10 = [random.random() * random.randint(0, 50) for _ in range(10)]
list_100 = [random.random() * random.randint(0, 50) for _ in range(100)]
list_1000 = [random.random() * random.randint(0, 50) for _ in range(1000)]

print('Массив 10 элементов: ', timeit.timeit("merge_sort(list_10[:])", globals=globals(), number=1000))
print('Массив 100 элементов: ', timeit.timeit("merge_sort(list_100[:])", globals=globals(), number=1000))
print('Массив 1000 элементов: ', timeit.timeit("merge_sort(list_1000[:])", globals=globals(), number=1000))

# Результаты:
# Массив 10 элементов:  0.008856200000000009
# Массив 100 элементов:  0.15525219999999998
# Массив 1000 элементов:  2.1729737
