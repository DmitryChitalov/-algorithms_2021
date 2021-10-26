import operator
import timeit
import numpy as np


def merge_sort(lst, compare=operator.lt):
    if len(lst) < 2:
        return lst[:]
    else:
        middle = int(len(lst) / 2)
        left = merge_sort(lst[:middle], compare)
        right = merge_sort(lst[middle:], compare)
        return merge(left, right, compare)


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


n = int(input('Введите количество элементов: '))
arr = np.random.uniform(0, 50, n)
print(arr)
print(merge_sort(arr))
arr = np.random.uniform(0, 50, 10)       # 10 элементов 0.017962699999999998
print(f'10 элементов {timeit.timeit("merge_sort(arr[:])",globals=globals(),number=1000)}')
arr = np.random.uniform(0, 50, 100)     # 100 элементов 0.22295299999999996
print(f'100 элементов {timeit.timeit("merge_sort(arr[:])",globals=globals(),number=1000)}')
arr = np.random.uniform(0, 50, 1000)    # 1000 элементов 2.9044693
print(f'1000 элементов {timeit.timeit("merge_sort(arr[:])",globals=globals(),number=1000)}')

# Вывод:
# На большом количестве данных сортировка слиянием показывает достаточно высокие
# результаты, таким образом скорость уменьшается чуть больше чем на порядок,
# почти так же как и увеличивается кол-во данных.
