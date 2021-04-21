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
import random


def merge(left_list, right_list):
    sorted_list = []
    left_index = right_index = 0
    left_length, right_length = len(left_list), len(right_list)
    for _ in range(left_length + right_length):
        if left_index < left_length and right_index < right_length:
            if left_list[left_index] <= right_list[right_index]:
                sorted_list.append(left_list[left_index])
                left_index += 1
            else:
                sorted_list.append(right_list[right_index])
                right_index += 1
        elif left_index == left_length:
            sorted_list.append(right_list[right_index])
            right_index += 1
        elif right_index == right_length:
            sorted_list.append(left_list[left_index])
            left_index += 1
    return sorted_list


def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left_list = merge_sort(nums[:mid])
    right_list = merge_sort(nums[mid:])
    return merge(left_list, right_list)


orig_list = [random.uniform(0, 50) for _ in range(10)]
print(f'Исходный массив {orig_list}')
print(f'Отсортированный по возрастанию {merge_sort(orig_list[:])}')

# замеры 10
print('10')
print(
    timeit.timeit(
        "merge_sort(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [random.uniform(0, 50) for _ in range(100)]

# замеры 100
print('100')
print(
    timeit.timeit(
        "merge_sort(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [random.uniform(0, 50) for _ in range(1000)]

# замеры 1000
print('1000')
print(
    timeit.timeit(
        "merge_sort(orig_list[:])",
        globals=globals(),
        number=1000))

"""
10
0.043735699999999995
100
0.6153637
1000
6.225134300000001

Сложность данного вида сортировки О(n log n)
При росте объема входных данных скорость выполения растет значительно медленнее, чем
при применении например пузырьковой сортировки из task_1

"""
