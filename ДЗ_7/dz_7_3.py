import random
from statistics import median
from timeit import timeit


def gnomeSort(arr):
    """
    Сортировка Гномия
    """
    index = 0
    # всего элементов
    n = len(arr)
    while index < n:
        if index == 0:
            index = index + 1
        if arr[index] >= arr[index - 1]:
            index = index + 1
        else:
            arr[index], arr[index - 1] = arr[index - 1], arr[index]
            index = index - 1
    return arr


def get_median_with_sort(array):
    n = len(array)
    arr_sorted = gnomeSort(array[:])
    if n % 2:
        return arr_sorted[n // 2]
    else:
        median1 = arr_sorted[n // 2]
        median2 = arr_sorted[n // 2 - 1]
        return (median1 + median2) / 2


def get_stat_median(array):
    return median(array)


def get_median_wo_sort(array):
    if len(array) == 1:
        return array[0]
    else:
        array.pop(array.index(max(array)))
        array.pop(array.index(min(array)))
        return get_median_wo_sort(array)


if __name__ == '__main__':
    m = int(input('Введите m для исходного массива: '))
    default_array = [random.randint(0, 100) for _ in range(2 * m + 1)]
    print(f'Исходный массив: {default_array}')
    print(f'Медиана с сортировкой: {get_median_with_sort(default_array[:])}')
    print("Время поиска медианы: ", timeit("get_median_with_sort(default_array)",
                                           globals=globals(), number=1000), " сек.")

    print()
    print(f'Медиана без сортировки: {get_median_wo_sort(default_array[:])}')
    print("Время поиска медианы: ", timeit("get_median_wo_sort(default_array)",
                                           globals=globals(), number=1000), " сек.")

    print()
    print(f'Медиана из модуля statistics: {get_stat_median(default_array[:])}')
    print("Время поиска медианы: ", timeit("get_stat_median(default_array)",
                                           globals=globals(), number=1000), " сек.")
