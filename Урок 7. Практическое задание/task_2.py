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

lst = [random.uniform(0, 50) for _ in range(100)]


def merge_sort(obj):
    if len(obj) > 1:
        cent = len(obj) // 2
        left = iter(merge_sort(obj[:cent]))
        x1 = next(left)
        right = iter(merge_sort(obj[cent:]))
        x2 = next(right)
        obj = []
        try:
            while True:
                if x1 <= x2:
                    obj.append(x1)
                    x1 = next(left)
                else:
                    obj.append(x2)
                    x2 = next(right)
        except:
            if x1 <= x2:
                obj.append(x2)
                obj.extend(right)
            else:
                obj.append(x1)
                obj.extend(left)
    return obj


print(timeit.timeit("merge_sort(lst[:])", globals=globals(), number=1000))
num = int(input('Enter the number: \n'))
print(f'Original - {lst[:num]}')
print(f'Sorted - {merge_sort(lst)[:num]}')
