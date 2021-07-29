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
import timeit


def merge_sort(arr):
    """
    Сложность: O(N Log N).
    :param arr:
    :return:
    """
    if len(arr) > 1:

        # Finding the mid of the array
        mid = len(arr) // 2

        # Dividing the array elements
        L = arr[:mid]

        # into 2 halves
        R = arr[mid:]

        # Sorting the first half
        merge_sort(L)

        # Sorting the second half
        merge_sort(R)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


def get_data_from_user() -> list:
    while True:
        el_count = input("Введите число элементов: ")
        print(el_count)
        if el_count.isdigit():
            el_count = int(el_count)
            break
        else:
            print("Вы ввели что-то не то. Заходим на новый круг!")

    return [random.uniform(0, 50) for _ in range(el_count)]


or_list = get_data_from_user()
print("Исходный:")
print(*or_list)
merge_sort(or_list)
print("Отсортированный:")
print(*or_list)
print()

orig_list = [random.uniform(0, 50) for _ in range(10)]

# замеры 10
print("Замеры 10 элементов: ",
      timeit.timeit(
          "merge_sort(orig_list[:])",
          globals=globals(),
          number=1000))

orig_list = [random.uniform(0, 50) for _ in range(100)]

# замеры 100
print("Замеры 100 элементов: ",
      timeit.timeit(
          "merge_sort(orig_list[:])",
          globals=globals(),
          number=1000))

orig_list = [random.uniform(0, 50) for _ in range(1000)]

# замеры 1000
print("Замеры 1000 элементов: ",
      timeit.timeit(
          "merge_sort(orig_list[:])",
          globals=globals(),
          number=1000))

"""
Замеры 10 элементов:  0.04276480000000049
Замеры 100 элементов:  0.6210529999999999
Замеры 1000 элементов:  7.9098654999999995
"""
