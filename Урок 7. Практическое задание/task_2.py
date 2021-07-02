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
from random import random
from task_1 import sort_base, sort_optimaze


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left, right = merge_sort(arr[:mid]), merge_sort(arr[mid:])

    return merge(left, right, arr.copy())


def merge(left, right, merged):
    left_cursor, right_cursor = 0, 0
    while left_cursor < len(left) and right_cursor < len(right):

        if left[left_cursor] <= right[right_cursor]:
            merged[left_cursor + right_cursor] = left[left_cursor]
            left_cursor += 1
        else:
            merged[left_cursor + right_cursor] = right[right_cursor]
            right_cursor += 1

    for left_cursor in range(left_cursor, len(left)):
        merged[left_cursor + right_cursor] = left[left_cursor]

    for right_cursor in range(right_cursor, len(right)):
        merged[left_cursor + right_cursor] = right[right_cursor]

    return merged


if __name__ == '__main__':

    n = int(input('Введите число элементов: '))
    test_list = [random() * 50 for _ in range(n)]

    # print('Исходный массив', test_list, sep='\n')
    # print('Отсортированный массив', merge_sort(test_list), sep='\n')

    print('Замер для сортировки слиянием', timeit("merge_sort(test_list[:])", globals=globals(), number=1000))

    print('Замер для сортировки "методом пузырька"', timeit("sort_base(test_list[:])", globals=globals(), number=1000))
    print('Замер для сортировки оптимизированным "методом пузырька"', timeit("sort_optimaze(test_list[:])", globals=globals(), number=1000))

"""
вывод
    Введите число элементов: 10
    Замер для сортировки слиянием 0.01708540000000003
    Замер для сортировки "методом пузырька" 0.009314899999999682
    Замер для сортировки оптимизированным "методом пузырька" 0.009726000000000123
    
    Введите число элементов: 100
    Замер для сортировки слиянием 0.25182569999999993
    Замер для сортировки "методом пузырька" 0.7695783
    Замер для сортировки оптимизированным "методом пузырька" 0.7606875
    
    Введите число элементов: 1000
    Замер для сортировки слиянием 4.3110462
    Замер для сортировки "методом пузырька" 87.1112053
    Замер для сортировки оптимизированным "методом пузырька" 91.3456357

Реализовал метод сортировки слиянием через функцию merge_sort, которая рекурсивно делит массив и при объединении
вызывает функцию сортировки merge. 
Как видно, из примеров вывода, метод сортировки слиянием выигрывает в скорости у метода сортировки "пузырьком" 
при увеличении размера массива 
"""




