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
import operator


def merge_sort(lst, compare=operator.lt):
    if len(lst) < 2:
        return lst[:]
    else:
        middle = int(len(lst) / 2)
        left = merge_sort(lst[:middle], compare)
        right = merge_sort(lst[middle:], compare)
        return merge(left, right, compare)


def merge(left, right, compare):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result


def random_list(n):
    lst = [random() * 50 for el in range(n)]
    return lst


try:
    number = int(input('Введите кол-во элементов массива: '))
    lst = random_list(number)
    print(f'Исходный массив: \n {lst}')
    print(f"Отсортированный массив слиянием: \n{merge_sort(lst[:])}")
    print(
        timeit(
            "merge_sort(lst[:])",
            globals=globals(),
            number=1000))
except ValueError:
    print('Вы ввели не число!!!')

'''
Замеры для 10, 100 и 1000 элементов 
0.03392981000000006
0.466909405
5.914864221
'''

