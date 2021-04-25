"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Хотя в примерах к уроку уже есть вариант реализации слияния, попробуйте предложить другой
(придумать или найти)

И попытаться сделать замеры на массивах разной длины: 10, 100, 1000, ...

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""
import timeit
import random

d = [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]


def merge(right: list, left: list, result: list):
    result.append((left if left[0] < right[0] else right).pop(0))
    return merge(right, left, result) if left and right else result + left + right


def merge_sort(collection: list):
    if len(collection) == 1:
        return collection
    return merge(merge_sort(collection[len(collection) // 2:]),
                 merge_sort(collection[:len(collection) // 2]), [])


orig_list = [random.randint(-100, 100) for _ in range(10)]

print(
    timeit.timeit(
        "merge_sort(orig_list[:])",
        globals=globals(),
        number=1000),
        orig_list[:], '\n',
        merge_sort(orig_list[:])
        )

orig_list = [random.randint(-100, 100) for _ in range(100)]

# замеры 100
print(
    timeit.timeit(
        "merge_sort(orig_list[:])",
        globals=globals(),
        number=1000),
        orig_list[:], '\n',
        merge_sort(orig_list[:])
        )

orig_list = [random.randint(-100, 100) for _ in range(996)]

# замеры 1000
print(
    timeit.timeit(
        "merge_sort(orig_list[:])",
        globals=globals(),
        number=1000),
        orig_list[:], '\n',
        merge_sort(orig_list[:])
        )



"""
0.013023199999999999 - 10 элементов
0.208309 - 100 элементов
3.1471199999999997 - 996 элементов
Нашёл на просторах интернета, реализация написана более лаконично, кратко.
сложность получается O(n log n)
"""
