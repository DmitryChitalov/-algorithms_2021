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


def merge_sort(arr):
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


unsorted_lst_10 = [random() * randint(0, 50) for i in range(10)]
unsorted_lst_100 = [random() * randint(0, 50) for i in range(100)]
unsorted_lst_1000 = [random() * randint(0, 50) for i in range(1000)]
merge_10 = timeit("merge_sort(unsorted_lst_10)", globals=globals(), number=100)
merge_100 = timeit("merge_sort(unsorted_lst_100)", globals=globals(), number=100)
merge_1000 = timeit("merge_sort(unsorted_lst_1000)", globals=globals(), number=100)
print("Массив на 10 элементов:")
print(unsorted_lst_10)
print(merge_sort(unsorted_lst_10))
print(f"Сортировка слиянием на 10 элементах заняла {merge_10} сек.\n")
print("Массив на 100 элементов:")
print(unsorted_lst_100)
print(merge_sort(unsorted_lst_100))
print(f"Сортировка слиянием на 100 элементах заняла {merge_100} сек.\n")
print("Массив на 1000 элементов:")
print(unsorted_lst_1000)
print(merge_sort(unsorted_lst_1000))
print(f"Сортировка слиянием на 1000 элементах заняла {merge_1000} сек.\n")

"""
Сортировка слиянием на 10 элементах заняла 0.001805600000000001 сек.
Сортировка слиянием на 100 элементах заняла 0.026009699999999997 сек.
Сортировка слиянием на 1000 элементах заняла 0.3481736 сек.

Пример из урока не очень понятный, этот гораздо понятнее и проще для понимания
На этих замерах очевидна сложность N*log(N)
Слияние очень эффективно и шустро работает.
"""