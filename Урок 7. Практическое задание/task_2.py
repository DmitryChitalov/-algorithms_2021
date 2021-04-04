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
from timeit import timeit
from memory_profiler import profile
from random import uniform


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
    return merge(left_list, right_list)


@profile
def merge_sort_profile(list_obj):
    merge_sort(list_obj)


random_list_of_nums = [uniform(0, 49) for _ in range(int(input('Задайте длину списка: ')))]
print(f'Исходный - {random_list_of_nums}')
merge_sort(random_list_of_nums[:])
print(f'Отсортированный - {random_list_of_nums}')

print('\nЗамеры при длине 10:')
random_list_of_nums = [uniform(0, 49) for _ in range(10)]
print('память:')
merge_sort_profile(random_list_of_nums[:])
print(f"время: {timeit('merge_sort(random_list_of_nums[:])', number=1000, globals=globals())}")

print('\nЗамеры при длине 100:')
random_list_of_nums = [uniform(0, 49) for _ in range(100)]
print('память:')
merge_sort_profile(random_list_of_nums[:])
print(f"время: {timeit('merge_sort(random_list_of_nums[:])', number=1000, globals=globals())}")

print('\nЗамеры при длине 1000:')
random_list_of_nums = [uniform(0, 49) for _ in range(1000)]
print('память:')
merge_sort_profile(random_list_of_nums[:])
print(f"время: {timeit('merge_sort(random_list_of_nums[:])', number=1000, globals=globals())}")

print('\nЗамеры при длине 10000:')
random_list_of_nums = [uniform(0, 49) for _ in range(10000)]
print('память:')
merge_sort_profile(random_list_of_nums[:])
print(f"время: {timeit('merge_sort(random_list_of_nums[:])', number=1000, globals=globals())}")

'''
Замеры при длине 10:
память: 38.8
время: 0.01792186600000001

Замеры при длине 100:
память: 38.8
время: 0.27145839200000044

Замеры при длине 1000:
память: 38.9
время: 3.5642975970000004

Замеры при длине 10000:
память: 40.1
время: 45.246313885

результаты замеров подтвердили, что сложность найденного алгоритма O(NlogN)
т.к. алгоритм рекурсивный видно, что требуемое количество памяти также 
растет с увеличением передаваемого на вход массива
'''
