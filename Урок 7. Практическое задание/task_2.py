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


def merge_sort(arr):
    # Последнее разделение массива
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    # Выполняем merge_sort рекурсивно с двух сторон
    left, right = merge_sort(arr[:mid]), merge_sort(arr[mid:])

    # Объединяем стороны вместе
    return merge(left, right, arr.copy())


def merge(left, right, merged):
    left_cursor, right_cursor = 0, 0
    while left_cursor < len(left) and right_cursor < len(right):

        # Сортируем каждый и помещаем в результат
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


# замеры 10
orig_list = [random.uniform(0, 50) for _ in range(int(input('Введите число элементов:')))]
print(f'Исходный - {orig_list}',
      timeit.timeit(
          "merge_sort(orig_list[:])",
          globals=globals(),
          number=1000), f'Отсортированный - {merge_sort(orig_list)}', sep='\n')

# замеры 100
orig_list = [random.uniform(0, 50) for _ in range(int(input('Введите число элементов:')))]
print(f'Исходный - {orig_list}',
      timeit.timeit(
          "merge_sort(orig_list[:])",
          globals=globals(),
          number=1000), f'Отсортированный - {merge_sort(orig_list)}', sep='\n')

# замеры 1000
orig_list = [random.uniform(0, 50) for _ in range(int(input('Введите число элементов:')))]
print(f'Исходный - {orig_list}',
      timeit.timeit(
          "merge_sort(orig_list[:])",
          globals=globals(),
          number=1000), f'Отсортированный - {merge_sort(orig_list)}', sep='\n')

'''
Введите число элементов:10
0.03339009000000015
Введите число элементов:100
0.5150200080000005
Введите число элементов:1000
6.895873255
'''
