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
import timeit

from random import random




def merge_sort(list):

    list_length = len(list)
    if list_length == 1:
        return list
    mid_point = list_length // 2

    left_partition = merge_sort(list[:mid_point])
    right_partition = merge_sort(list[mid_point:])

    return merge(left_partition, right_partition)


def merge(left, right):

    output = []
    i = j = 0

    while i < len(left) and j < len(right):

        if left[i] < right[j]:
            output.append(left[i])
            i += 1
        else:
            output.append(right[j])
            j += 1

    output.extend(left[i:])
    output.extend(right[j:])

    return output

small_list = [random() * 100 for i in range(10)]
mid_list = [random() * 100 for j in range(1000)]



def run_merge_sort():
    print(timeit.timeit("merge_sort(small_list[:])",globals=globals(), number=1000))
    print(timeit.timeit("merge_sort(mid_list[:])",globals=globals(), number=1000))


run_merge_sort()

0.014645099999999994
2.9665036

#функция выполняется достаточно таки быстро, при небольшом количестве элементтов