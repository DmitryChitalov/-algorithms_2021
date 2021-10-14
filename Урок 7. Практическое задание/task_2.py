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
from random import random


def merge_sort(lst_obj):
    if len(lst_obj) > 1:
        center = len(lst_obj) // 2
        left = lst_obj[:center]
        right = lst_obj[center:]

        merge_sort(left)
        merge_sort(right)

        # перестали делить
        # выполняем слияние
        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lst_obj[k] = left[i]
                i += 1
            else:
                lst_obj[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            lst_obj[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            lst_obj[k] = right[j]
            j += 1
            k += 1
        return lst_obj


num = 1000

orig_list_10 = [random() * 50 for _ in range(10)]
# print(f'Исходный массив : {orig_list_10}\nОтсортированный массив: {merge_sort(orig_list_10[:])}')
# замеры 10
print(f'Звмер сортировки массива из 10: {timeit.timeit("merge_sort(orig_list_10[:])", globals=globals(), number=num)}')

orig_list_100 = [random() * 50 for _ in range(100)]
# print(f'Исходный массив : {orig_list_100}\nОтсортированный массив: {merge_sort(orig_list_100[:])}')
# замеры 100
print(f'Звмер сортировки массива из 100: {timeit.timeit("merge_sort(orig_list_100[:])", globals=globals(), number=num)}')

orig_list_1000 = [random() * 50 for _ in range(1000)]
# print(f'Исходный массив : {orig_list_1000}\nОтсортированный массив: {merge_sort(orig_list_1000[:])}')
# замеры 1000
print(f'Звмер сортировки массива из 1000: {timeit.timeit("merge_sort(orig_list_1000[:])", globals=globals(), number=num)}')

''''
Ваш вопрос из ПР: какие выводы можно сделать об оптимальности решения?
Ответ: Как и говорилось на уроке сложность алгоритма O(nlogn), что при большом количестве повторений дает преимошество 
в скорости перед другими алгоритмами имеющеми сложность O(n^2)
'''

