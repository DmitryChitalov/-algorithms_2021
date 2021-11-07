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


# с просторов интернета

def merge(list_left, list_right):
    sorted_list = []
    index_left, index_right = 0, 0
    left_list_length, right_list_length = len(list_left), len(list_right)
    for _ in range(left_list_length + right_list_length):
        if index_left < left_list_length and index_right < right_list_length:
            if list_left[index_left] <= list_right[index_right]:
                sorted_list.append(list_left[index_left])
                index_left += 1
            else:
                sorted_list.append(list_right[index_right])
                index_right += 1
        elif index_left == left_list_length:
            sorted_list.append(list_right[index_right])
            index_right += 1
        elif index_right == right_list_length:
            sorted_list.append(list_left[index_left])
            index_left += 1
    return sorted_list


def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    separation = len(nums) // 2
    left_list = merge_sort(nums[:separation])
    right_list = merge_sort(nums[separation:])
    return merge(left_list, right_list)


# замер на 10
list_megre = [random.randint(0, 50) for _ in range(10)]
print(f'Неотсортированный массив: {list_megre}')
print(f'Время выполнения: '
      f'{timeit.timeit("merge_sort(list_megre[:])", globals=globals(), number=1)} \n'
      f'Отсортированный массив: {merge_sort(list_megre[:])}')
# время выполнения 4.410000110510737e-05

# замер на 100
list_megre = [random.randint(0, 50) for _ in range(100)]
print(f'Неотсортированный массив: {list_megre}')
print(f'Время выполнения: '
      f'{timeit.timeit("merge_sort(list_megre[:])", globals=globals(), number=1)} \n'
      f'Отсортированный массив: {merge_sort(list_megre[:])}')
# время выполнения 0.00044609999167732894

# замер на 1000
list_megre = [random.randint(0, 50) for _ in range(1000)]
print(f'Неотсортированный массив: {list_megre}')
print(f'Время выполнения: '
      f'{timeit.timeit("merge_sort(list_megre[:])", globals=globals(), number=1)} \n'
      f'Отсортированный массив: {merge_sort(list_megre[:])}')
# время выполнения 0.00045000000682193786
