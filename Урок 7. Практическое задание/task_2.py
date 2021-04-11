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


def merge_sort_from_lesson(lst_obj):

    if len(lst_obj) > 1:

        center = len(lst_obj) // 2

        left = lst_obj[:center]

        right = lst_obj[center:]

        merge_sort(left)

        merge_sort(right)

        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):

            if left[i] < right[j]:

                lst_obj[k] = left[i]

                i += 1

            else:
                lst_obj[k] = right[j]

                j += 1

            k += 1

        while i < len(left):

            lst_obj[k] = left[i]

            i += 1

            k += 1

        while j < len(right):

            lst_obj[k] = right[j]

            j += 1

            k += 1

        return lst_obj


@profile
def mrg_sort_mem_profile(list_to_sort):

    merge_sort(list_to_sort)


@profile
def mrg_sort_from_lesson_mem_profile(list_to_sort):

    merge_sort_from_lesson(list_to_sort)


numbers_list = [uniform(0, 49) for _ in range(10)]

print(f'Исходный массив: {numbers_list}')

print(f'Отсортированный массив: {merge_sort(numbers_list[:])}')


print('Интернет:')

print(f"Время: {timeit('merge_sort(numbers_list[:])', number=1000, globals=globals())}")

print('Память:\n')

mrg_sort_mem_profile(numbers_list[:])

print('Урок:')

print(f"Время: {timeit('merge_sort_from_lesson(numbers_list[:])', number=1000, globals=globals())}")

print('Память:\n')

mrg_sort_from_lesson_mem_profile(numbers_list[:])

numbers_list = [uniform(0, 49) for _ in range(100)]

print('Интернет:')

print(f"Время: {timeit('merge_sort(numbers_list[:])', number=1000, globals=globals())}")

print('Память:\n')

mrg_sort_mem_profile(numbers_list[:])

print('Урок:')

print(f"Время: {timeit('merge_sort_from_lesson(numbers_list[:])', number=1000, globals=globals())}")

print('Память:\n')

mrg_sort_from_lesson_mem_profile(numbers_list[:])

numbers_list = [uniform(0, 49) for _ in range(1000)]

print('Интернет:')

print(f"Время: {timeit('merge_sort(numbers_list[:])', number=1000, globals=globals())}")

print('Память:\n')

mrg_sort_mem_profile(numbers_list[:])

print('Урок:')

print(f"Время выполения: {timeit('merge_sort_from_lesson(numbers_list[:])', number=1000, globals=globals())}")

print('Память:\n')

mrg_sort_from_lesson_mem_profile(numbers_list[:])

numbers_list = [uniform(0, 49) for _ in range(10000)]

print('Интернет:')

print(f"Время: {timeit('merge_sort(numbers_list[:])', number=1000, globals=globals())}")

print('Память:\n')

mrg_sort_mem_profile(numbers_list[:])

print('Урок:')

print(f"Время: {timeit('merge_sort_from_lesson(numbers_list[:])', number=1000, globals=globals())}")

print('Память:\n')

mrg_sort_from_lesson_mem_profile(numbers_list[:])

numbers_list = [uniform(0, 49) for _ in range(100000)]

print('Интернет:')

print(f"Время: {timeit('merge_sort(numbers_list[:])', number=1000, globals=globals())}")

print('Память:\n')

mrg_sort_mem_profile(numbers_list[:])

print('Урок:')

print(f"Время: {timeit('merge_sort_from_lesson(numbers_list[:])', number=1000, globals=globals())}")

print('Память:\n')

mrg_sort_from_lesson_mem_profile(numbers_list[:])

'''
-----------------------------------------------------------------------------------------------------------------------
Я использовала замеры времени, тем самым мы можем увидеть что сложность алгоритма O(NlogN), так как
с ростом длины массива, время выполнения алгоритма растет, но не сильно значительно. Замеры же, показали что
с ростом данных, объем памяти будет увеличиваться очень существенно. Так же результаты замеров времени выполнения
и самой памяти, показывают то, что реализация алгоритма не сильно устпуает реализации с урока.
-----------------------------------------------------------------------------------------------------------------------
(Вариант реализации найден в интернете, своим не является, если понадобится могу сикнуть ссылку).
-----------------------------------------------------------------------------------------------------------------------
Результаты:
-----------------------------------------------------------------------------------------------------------------------
Можете посмотреть сами, так как их тут много и код получится слишком массивным.
-----------------------------------------------------------------------------------------------------------------------
'''