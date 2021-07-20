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
from timeit import default_timer


def create_lst(nums):
    """Create array"""
    return [random.random() * 50 for i in range(nums)]

def merge(left, right):
    """Merge part"""
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
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

def merge_sort(in_array):
    """Recursive part"""
    if len(in_array) < 2:
        return in_array[:]
    else:
        middle = int(len(in_array) // 2)
        left = merge_sort(in_array[:middle])
        right = merge_sort(in_array[middle:])
        result = merge(left, right)
    return result



lst = create_lst(1000000)
print('Input array')
print(lst)
start = default_timer()
print('\nSorted array')
print(merge_sort(lst))
print(f'Working time merge sort:{default_timer() - start}')
"""
100         Working time merge sort:0.0004294999999999993
1000        Working time merge sort:0.007729399999999997
10000       Working time merge sort:0.0550085
1000000     Working time merge sort:8.132188300000001
Из результатов видно, что сложность сортировки слиянием - логарифмическая.
"""
