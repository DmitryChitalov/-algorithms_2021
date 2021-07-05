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
from timeit import default_timer, timeit


def time_mem_decor(func):
    def wrapper(lst):
        time_start = default_timer()
        res = func(lst)
        time_diff = default_timer() - time_start
        print(f'Время  "{func.__name__}": {time_diff}')
        return res

    return wrapper


def merge(left_lst, right_lst):
    sorted_lst = []
    left_idx = right_idx = 0

    left_len, right_len = len(left_lst), len(right_lst)

    for _ in range(left_len + right_len):
        if left_idx < left_len and right_idx < right_len:
            if left_lst[left_idx] <= right_lst[right_idx]:
                sorted_lst.append(left_lst[left_idx])
                left_idx += 1
            else:
                sorted_lst.append(right_lst[right_idx])
                right_idx += 1

        elif left_idx == left_len:
            sorted_lst.append(right_lst[right_idx])
            right_idx += 1
        elif right_idx == right_len:
            sorted_lst.append(left_lst[left_idx])
            left_idx += 1

    return sorted_lst


def merge_sort(nums):
    if len(nums) < 2:
        return nums

    mid = len(nums) // 2

    left_list = merge_sort(nums[:mid])
    right_list = merge_sort(nums[mid:])

    return merge(left_list, right_list)


# [0; 50) = {0 <= x < 50} - опустим это, чтобы не перегружать код.
my_lst = [random.uniform(0, 50) for _ in range(10)]

print(f"Исходный:\n{my_lst}")
print(f"Отсортированный:\n{merge_sort(my_lst[:])}\n")
print("1000:",
      timeit('merge_sort(my_lst[:])', globals=globals(), number=1000))
print("10000:",
      timeit('merge_sort(my_lst[:])', globals=globals(), number=10000))
print("100000:",
      timeit('merge_sort(my_lst[:])', globals=globals(), number=100000))
