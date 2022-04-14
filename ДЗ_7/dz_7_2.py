from random import uniform
from timeit import timeit


def merge(arr, l, m, r):
    """
    Сортировка слиянием

    Слияние 2-х подмассивов массива arr[]
    Первый подмассив - arr[l..m]
    Второй подмассив - arr[m+1..r]

    """
    n1 = m - l + 1
    n2 = r - m

    # Создаем вресенный массив
    L = [0] * (n1)
    R = [0] * (n2)

    # Копируем данные во временные массивы L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    # Склеиваем временные массивы в arr[l..r]
    i = 0  # Начальный индекс первого подмассива
    j = 0  # Начальный индекс второго подмассива
    k = l  # Начальный индекс склеинного подмассива

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Копируем оставшиеся элементы L[] если есть
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Копируем оставшиеся элементы R[] если есть
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


def mergeSort(arr, l, r):
    if l < r:
        m = l + (r - l) // 2

        # Сортируем первую и 2-ю половины
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)


def sort_n_print(size: int, to_print: bool = False):
    arr = [uniform(0, 50) for _ in range(size)]
    n = len(arr)

    if to_print:
        print(f"Исходный массив, размер = {n}: ")
        print(arr)

    # Сортируем исходный массив
    mergeSort(arr, 0, n - 1)

    if to_print:
        print(f"Отсортированный массив из {n}:")
        print(arr)


# размеры массивов
sz1 = 10
sz2 = 100
sz3 = 1000

sort_n_print(sz1, 1)
sort_n_print(sz2, 1)
sort_n_print(sz3, 1)

print("Результаты измерений:")
print(f"длина массива {sz1}: ", timeit(f"sort_n_print({sz1})", globals=globals(), number=1000), " сек.")
print(f"длина массива {sz2}: ", timeit(f"sort_n_print({sz2})", globals=globals(), number=1000), " сек.")
print(f"длина массива {sz3}: ", timeit(f"sort_n_print({sz3})", globals=globals(), number=1000), " сек.")

""" Результат
длина массива 10:  0.0170395  сек.
длина массива 100:  0.22420070000000003  сек.
длина массива 1000:  3.0450890999999998  сек.
"""
