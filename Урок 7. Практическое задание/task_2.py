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

from random import randint
from timeit import timeit
from operator import lt


def merge_sort(list_obj, compare=lt):
    if len(list_obj) < 2:
        return list_obj[:]
    else:
        middle = int(len(list_obj) / 2)
        left = merge_sort(list_obj[:middle], compare)
        right = merge_sort(list_obj[middle:], compare)
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

if __name__ == '__main__':
    number = input('Введите размер массива: ')
    try:
        number = int(number)
    except ValueError:
        print('Вы ввели не число! Исправьтесь')

    some_list = [randint(0, 50) for i in range(number)]

    print(f'Исходный массив - {some_list}')
    print(f'Отсортированный массив - {merge_sort(some_list)}')


"""
Результаты измерений:
1. Время выполнения сортировки массива длинной 10: 0.00046526400000002077
2. Время выполнения сортировки массива длинной 100: 0.0038952329999999424
3. Время выполнения сортировки массива длинной 1000: 0.041783429000000094
"""

