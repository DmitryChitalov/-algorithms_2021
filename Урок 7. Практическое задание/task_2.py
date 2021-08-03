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

import random
from timeit import timeit


def merge_sort(list_obj):
    if len(list_obj) < 2:
        return list_obj

    middle = len(list_obj) // 2
    left = merge_sort(list_obj[:middle])
    right = merge_sort(list_obj[middle:])

    i, j = 0, 0
    result = []
    while i < len(left) or j < len(right):
        if not i < len(left):
            result.append(right[j])
            j += 1
        elif not j < len(right):
            result.append(left[i])
            i += 1
        elif left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    return result


nums = int(input("Введите число элементо в массиве: "))
nums_list = [random.random() + random.randint(0, 50) for _ in range(nums)]
print(f"Исходный: {nums_list}\nОтсортированный: {merge_sort(nums_list)}")

nums_list_1 = [random.random() + random.randint(0, 50) for _ in range(10)]
nums_list_2 = [random.random() + random.randint(0, 50) for _ in range(100)]
nums_list_3 = [random.random() + random.randint(0, 50) for _ in range(1000)]

print(f'Время сортировки массива с 10 элементами: '
      f'{timeit("merge_sort(nums_list_1[:])", globals=globals(), number=1000)}')
# Время сортировки массива с 10 элементами: 0.012572000000000472
print(f'Время сортировки массива с 100 элементами: '
      f'{timeit("merge_sort(nums_list_2[:])", globals=globals(), number=1000)}')
# Время сортировки массива с 100 элементами: 0.19458269999999978 
print(f'Время сортировки массива с 1000 элементами: '
      f'{timeit("merge_sort(nums_list_3[:])", globals=globals(), number=1000)}')
# Время сортировки массива с 1000 элементами: 2.6863645