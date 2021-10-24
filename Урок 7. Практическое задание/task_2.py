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
from timeit import timeit


def merge_sort(obj):
    if len(obj) > 1:
        median_list = len(obj) // 2
        left_list = obj[:median_list]
        right_list = obj[median_list:]

        merge_sort(left_list)
        merge_sort(right_list)

        i, j, k = 0, 0, 0

        while i < len(left_list) and j < len(right_list):
            if left_list[i] < right_list[j]:
                obj[k] = left_list[i]
                i += 1
            else:
                obj[k] = right_list[j]
                j += 1
            k += 1

        while i < len(left_list):
            obj[k] = left_list[i]
            i += 1
            k += 1

        while j < len(right_list):
            obj[k] = right_list[j]
            j += 1
            k += 1
        return obj


list_len = int(input('Введите количество элементов: \n'))
test_list = [random.random() for i in range(list_len)]
print(f'Исходный - {test_list}')
print(f'Отсортированный - {merge_sort(test_list)}')
print(f'{list_len} элементов', timeit('merge_sort(test_list[:])', globals=globals(), number=1000))
"""
Для 10 элементов время выполнения - 0.014677999999999969
Для 100 элементов время выполнения - 0.22962229999999995
Для 1000 элементов время выполнения - 2.8496870000000003

На 1000 элементов результаты уже не очень, на 10000 совсем плохо - 37.345229
"""