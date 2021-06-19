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
from timeit import timeit
from random import uniform


# Реализация с https://tproger.ru/translations/sorting-algorithms-in-python/
def merge(left_list, right_list):
    sorted_list = []
    left_list_index = right_list_index = 0

    left_list_length, right_list_length = len(left_list), len(right_list)

    for _ in range(left_list_length + right_list_length):
        if left_list_index < left_list_length and right_list_index < right_list_length:
            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1

        elif left_list_index == left_list_length:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1
        elif right_list_index == right_list_length:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1

    return sorted_list


def merge_sort(nums):
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2
    left_list = merge_sort(nums[:mid])
    right_list = merge_sort(nums[mid:])

    # Объединяем отсортированные списки в результирующий
    return merge(left_list, right_list)


random_list_of_nums = [uniform(0, 50) for _ in range(10)]
print(f'{random_list_of_nums}\n{merge_sort(random_list_of_nums[:])}')

print(f'Время: {timeit("merge_sort(random_list_of_nums)", globals=globals(), number=1000)}')

random_list_of_nums = [uniform(0, 50) for _ in range(100)]
print(f'{random_list_of_nums}\n{merge_sort(random_list_of_nums[:])}')

print(f'Время: {timeit("merge_sort(random_list_of_nums)", globals=globals(), number=1000)}')

random_list_of_nums = [uniform(0, 50) for _ in range(1000)]
print(f'{random_list_of_nums}\n{merge_sort(random_list_of_nums[:])}')

print(f'Время: {timeit("merge_sort(random_list_of_nums)", globals=globals(), number=1000)}')

'''
На больших массивах эффективность алгоритма заметна лучше.
'''
