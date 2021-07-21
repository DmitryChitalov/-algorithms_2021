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
from random import uniform
from timeit import timeit


def merge_sort(arr):

    # Базовый случай
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    # Делим на две части, пока не дойдем до базового случая
    left, right = merge_sort(arr[:mid]), merge_sort(arr[mid:])

    # Вызываем функцию слияния
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


n = int(input("Введите число элементов: "))
lst = [uniform(0, 50) for i in range(n)]
print(f'Неотсортированный массив: {lst}')
print(f'Отсортированный массив: {merge_sort(lst)}')

print(f'###### Тесты ###### Тесты ######')
print('Сортировка слиянием 100 элементов: ',
      timeit(
          "merge_sort([uniform(0, 50) for i in range (100)])",
          globals=globals(),
          number=1))

print('Сортировка слиянием 1000 элементов: ',
      timeit(
          "merge_sort([uniform(0, 50) for i in range (1000)])",
          globals=globals(),
          number=1))

print('Сортировка слиянием 10000 элементов: ',
      timeit(
          "merge_sort([uniform(0, 50) for i in range (10000)])",
          globals=globals(),
          number=1))

print('Сортировка слиянием 100000 элементов: ',
      timeit(
          "merge_sort([uniform(0, 50) for i in range (100000)])",
          globals=globals(),
          number=1))

# Результаты
# Сортировка слиянием 100 элементов:  0.00020280000000000298
# Сортировка слиянием 1000 элементов:  0.002466000000000003
# Сортировка слиянием 10000 элементов:  0.0295589
# Сортировка слиянием 100000 элементов:  0.3715464
# Как видно из результатов, сортировка слиянием работает в разы лучше сортировки пузырьком
# за счет улучшения сложности самого алгоритма (Пузырьком - O(n^2); Слиянием - O(nlogn)).
# Разница особенна заметна на массиве большой длины.


