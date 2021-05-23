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
# Вариант сортировки слиянием с сайта
# https://tproger.ru/translations/sorting-algorithms-in-python/
from timeit import timeit
from memory_profiler import profile
from random import uniform


def merge(left_list, right_list):
    sorted_list = []
    left_list_index = right_list_index = 0

    # Длина списков часто используется, поэтому создадим переменные для удобства
    left_list_length, right_list_length = len(left_list), len(right_list)

    for _ in range(left_list_length + right_list_length):
        if left_list_index < left_list_length and right_list_index < right_list_length:
            # Сравниваем первые элементы в начале каждого списка
            # Если первый элемент левого подсписка меньше, добавляем его
            # в отсортированный массив
            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
            # Если первый элемент правого подсписка меньше, добавляем его
            # в отсортированный массив
            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1

        # Если достигнут конец левого списка, элементы правого списка
        # добавляем в конец результирующего списка
        elif left_list_index == left_list_length:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1
        # Если достигнут конец правого списка, элементы левого списка
        # добавляем в отсортированный массив
        elif right_list_index == right_list_length:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1

    return sorted_list


def merge_sort(nums):
    # Возвращаем список, если он состоит из одного элемента
    if len(nums) <= 1:
        return nums

    # Для того чтобы найти середину списка, используем деление без остатка
    # Индексы должны быть integer
    mid = len(nums) // 2

    # Сортируем и объединяем подсписки
    left_list = merge_sort(nums[:mid])
    right_list = merge_sort(nums[mid:])

    # Объединяем отсортированные списки в результирующий
    return merge(left_list, right_list)


# код с урока
def merge_sort_from_lesson(lst_obj):
    if len(lst_obj) > 1:
        center = len(lst_obj) // 2
        left = lst_obj[:center]
        right = lst_obj[center:]

        merge_sort(left)
        merge_sort(right)

        # перестали делить
        # выполняем слияние
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

"""
Результаты замеров приведенных ниже подтвердили, что сложность найденного алгоритма O(NlogN)
т.к. алгоритм рекурсивный видно, что требуемое количество памяти также
растет при увеличении длины входного массива.
"""

# Проведем замеры времени и памяти с различными длинами массива.
numbers_list = [uniform(0, 49) for _ in range(10)]
print(f'исходный массив:\n {numbers_list}')
print(f'отсортированный массив:\n {merge_sort(numbers_list[:])}')

# время - 0.016978099999999996 с, память - 19,4 MiB
print('новая реализация:')
print(f"время выполения: {timeit('merge_sort(numbers_list[:])', number=1000, globals=globals())}")
print('занимаемая память:\n')
mrg_sort_mem_profile(numbers_list[:])

# время - 0.01160040000000001 с, память - 19,5 MiB
print('реализация с урока:')
print(f"время выполения: {timeit('merge_sort_from_lesson(numbers_list[:])', number=1000, globals=globals())}")
print('занимаемая память:\n')
mrg_sort_from_lesson_mem_profile(numbers_list[:])

numbers_list = [uniform(0, 49) for _ in range(100)]

# время - 0.21257529999999997 с, память - 19,5 MiB
print('новая реализация:')
print(f"время выполения: {timeit('merge_sort(numbers_list[:])', number=1000, globals=globals())}")
print('занимаемая память:\n')
mrg_sort_mem_profile(numbers_list[:])

# время - 0.23939429999999995 с, память - 19,5 MiB
print('реализация с урока:')
print(f"время выполения: {timeit('merge_sort_from_lesson(numbers_list[:])', number=1000, globals=globals())}")
print('занимаемая память:\n')
mrg_sort_from_lesson_mem_profile(numbers_list[:])

numbers_list = [uniform(0, 49) for _ in range(1000)]

# время - 3.1609960999999998 с, память - 19,6 MiB
print('новая реализация:')
print(f"время выполения: {timeit('merge_sort(numbers_list[:])', number=1000, globals=globals())}")
print('занимаемая память:\n')
mrg_sort_mem_profile(numbers_list[:])

# время - 3.0686491 с, память - 19,6 MiB
print('реализация с урока:')
print(f"время выполения: {timeit('merge_sort_from_lesson(numbers_list[:])', number=1000, globals=globals())}")
print('занимаемая память:\n')
mrg_sort_from_lesson_mem_profile(numbers_list[:])

numbers_list = [uniform(0, 49) for _ in range(10000)]

# время - 38.1928949 с, память - 21.4 MiB
print('новая реализация:')
print(f"время выполения: {timeit('merge_sort(numbers_list[:])', number=1000, globals=globals())}")
print('занимаемая память:\n')
mrg_sort_mem_profile(numbers_list[:])

# время - 39.2008879 с, память - 21.4 MiB
print('реализация с урока:')
print(f"время выполения: {timeit('merge_sort_from_lesson(numbers_list[:])', number=1000, globals=globals())}")
print('занимаемая память:\n')
mrg_sort_from_lesson_mem_profile(numbers_list[:])
