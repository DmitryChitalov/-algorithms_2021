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

from timeit import timeit
import random


def chek_time(f):
    return timeit(f"{f}", globals=globals(), number=10000)


def create_lst(length):
    return [random.random() * 50 for _ in range(length)]


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


user_input = int(input("Введите длину списка: "))
orig_list = create_lst(user_input)
print(f"Список:\n{orig_list}")
print(f"Отсортированный список:\n{merge_sort(orig_list)}")

orig_list_10 = create_lst(10)
orig_list_100 = create_lst(100)
orig_list_1000 = create_lst(1000)
print(f"Затрачено времени на сортировку 10 элементов:"
      f"\n{chek_time('merge_sort(orig_list_10[:])')}")
print(f"Затрачено времени на сортировку 100 элементов:"
      f"\n{chek_time('merge_sort(orig_list_100[:])')}")
print(f"Затрачено времени на сортировку 1000 элементов:"
      f"\n{chek_time('merge_sort(orig_list_1000[:])')}")

"""
Аналитика:
Использовал алгоритм из интернета.
По моим подсчетам сортировка вещественных чисел занимает в 10 раз больше времени чем сортировка целых чисел.


Замеры:
Затрачено времени на сортировку 10 элементов:
0.07131409999999994
Затрачено времени на сортировку 100 элементов:
1.1486797000000002
Затрачено времени на сортировку 1000 элементов:
16.2008579
"""
