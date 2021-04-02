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
from timeit import timeit
from memory_profiler import profile

"""
Источник: https://tproger.ru/translations/sorting-algorithms-in-python/
"""


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


@profile
def test_100():
    merge_sort(orig_list_100)


@profile
def test_1000():
    merge_sort(orig_list_1000)


@profile
def test_10000():
    merge_sort(orig_list_10000)


@profile
def test_100000():
    merge_sort(orig_list_100000)


orig_list_100 = [random.uniform(0, 49) for _ in range(100)]
test_100()
print(f'100 элементов, {timeit("merge_sort(orig_list_100[:])", globals=globals(), number=1000)}')
print('=' * 50)

orig_list_1000 = [random.uniform(0, 49) for _ in range(1000)]
test_1000()
print(f'1000 элементов, {timeit("merge_sort(orig_list_1000[:])", globals=globals(), number=1000)}')
print('=' * 50)

orig_list_10000 = [random.uniform(0, 49) for _ in range(10000)]
test_10000()
print(f'10000 элементов, {timeit("merge_sort(orig_list_10000[:])", globals=globals(), number=1000)}')
print('=' * 50)

orig_list_100000 = [random.uniform(0, 49) for _ in range(100000)]
test_100000()
print(f'100000 элементов, {timeit("merge_sort(orig_list_100000[:])", globals=globals(), number=1000)}')
print('=' * 50)
"""
Результаты
1) 100 элементов, 0.148743  // 19.5 MiB  
2) 1000 элементов, 2.2632746 // 19.5 MiB
3) 10000 элементов, 26.981804399999998 // 20.7 MiB 
4) 100000 элементов, 339.86500290000004 // 25.8 MiB 

Результаты показали, что скорость выполнения алгоритма достаточно высокая, однако при работе 
с большим количеством входных данных, требуется все больше памяти для вычислений.
(с учетом большого числа элементов, время относительно быстрое)
"""
