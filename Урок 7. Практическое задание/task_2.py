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
import operator
import timeit


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


def merge_sort(lst, compare=operator.lt):
    if len(lst) < 2:
        return lst[:]
    else:
        middle = int(len(lst) / 2)
        left = merge_sort(lst[:middle], compare)
        right = merge_sort(lst[middle:], compare)
        return merge(left, right, compare)


n = int(input('Введите число элементов: '))
orig_list = [random.uniform(0, 50) for _ in range(n)]
print(orig_list)
print(merge_sort(orig_list[:]))

orig_list_2 = [random.uniform(0, 50) for _ in range(10)]

print(
    f'Время выполнения merge_sort при 10 элементах массива: '
    f'{timeit.timeit("merge_sort(orig_list_2[:])", globals=globals(), number=1000)}')

orig_list_3 = [random.uniform(0, 50) for _ in range(100)]

print(
    f'Время выполнения merge_sort при 100 элементах массива: '
    f'{timeit.timeit("merge_sort(orig_list_3[:])", globals=globals(), number=1000)}')

orig_list_4 = [random.uniform(0, 50) for _ in range(1000)]

print(
    f'Время выполнения merge_sort при 1000 элементах массива: '
    f'{timeit.timeit("merge_sort(orig_list_4[:])", globals=globals(), number=1000)}')

'''
Время выполнения merge_sort при 10 элементах массива: 0.01792425600000014
Время выполнения merge_sort при 100 элементах массива: 0.2374673460000003
Время выполнения merge_sort при 1000 элементах массива: 3.221889795
Вывод: чем больше элементов в массиве, тем большее время тратиться на выполнение функций. 
'''
