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

import random
import timeit


def merge_sort(data):
    count = len(data)
    if count > 2:
        part_1 = merge_sort(data[:count // 2])
        part_2 = merge_sort(data[count // 2:])
        data = part_1 + part_2
        last_index = len(data) - 1

        for i in range(last_index):
            min_value = data[i]
            min_index = i

            for j in range(i + 1, last_index + 1):
                if min_value > data[j]:
                    min_value = data[j]
                    min_index = j

            if min_index != i:
                data[i], data[min_index] = data[min_index], data[i]

    elif len(data) > 1 and data[0] > data[1]:
        data[0], data[1] = data[1], data[0]

    return data


num_array1 = [random.randint(0, 49) for i in range(10)]
num_array2 = [random.randint(0, 49) for i in range(100)]
num_array3 = [random.randint(0, 49) for i in range(1000)]

print(num_array1)
print(num_array2)
print(num_array3)

print(merge_sort(num_array1))
print(merge_sort(num_array2))
print(merge_sort(num_array3))


print(
    timeit.timeit(
        "merge_sort(num_array1[:])",
        globals=globals(),
        number=1000))

print(
    timeit.timeit(
        "merge_sort(num_array2[:])",
        globals=globals(),
        number=1000))

print(
    timeit.timeit(
        "merge_sort(num_array3[:])",
        globals=globals(),
        number=1000))


"""
Время выполнения для 10, 100, 1000 элементов:
0.013599651007098146
0.5603459779958939
40.77737134399649
Сложность nlog2n, что приблизтельно подтверждается замерами
"""