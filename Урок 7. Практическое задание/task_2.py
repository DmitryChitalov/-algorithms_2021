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
import operator
import timeit
import random


def merge(left, right, compare):
    result = []
    j = 0
    i = 0
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


def merge_sort(some_list, compare=operator.lt):
    if len(some_list) < 2:
        return some_list[:]
    else:
        middle = len(some_list) // 2
        left = merge_sort(some_list[:middle], compare)
        right = merge_sort(some_list[middle:], compare)
        return merge(left, right, compare)


quantity = int(input('Введите количетство элементов: '))
my_list = [random.uniform(0, 50) for a in range(quantity)]

print('Исходный массив:', my_list)
print('Отсортированный массив:', merge_sort(my_list))

orig_list_10 = [random.uniform(0, 50) for b in range(10)]
print('Массив длинной 10 элементов ')
print(timeit.timeit("merge_sort(orig_list_10[:])", globals=globals(), number=1000))

orig_list_100 = [random.uniform(0, 50) for c in range(100)]
print('Массив длинной 100 элементов ')
print(timeit.timeit("merge_sort(orig_list_100[:])", globals=globals(), number=1000))

orig_list_1000 = [random.uniform(0, 50) for d in range(1000)]
print('Массив длинной 1000 элементов ')
print(timeit.timeit("merge_sort(orig_list_1000[:])", globals=globals(), number=1000))

orig_list_10000 = [random.uniform(0, 50) for e in range(10000)]
print('Массив длинной 10000 элементов ')
print(timeit.timeit("merge_sort(orig_list_10000[:])", globals=globals(), number=1000))

'''
Массив длинной 10 
0.014262700000000184
Массив длинной 100 
0.21983799999999976
Массив длинной 1000 
3.0123334
Массив длинной 10000 
40.15342950
Время сильно возрастает при увеичении массива
'''
