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
from timeit import default_timer
from memory_profiler import memory_usage
import random as rnd


def decor(func):
    def wrapper(*args, **kwargs):
        start_time = default_timer()
        m1 = memory_usage()
        res = func(*args, **kwargs)
        m2 = memory_usage()
        fin_time = default_timer()
        print(f"\nФункция: {func.__name__}")
        print(f"Memory: {m2[0] - m1[0]:0.5f} ")
        print(f"Time: {fin_time - start_time:0.5f} ")
        return res

    return wrapper


# Другой вариант
def merge_two_list(left_l, right_l):
    sorted_list = []
    n = len(left_l)
    m = len(right_l)
    i = 0
    j = 0
    while i < n and j < m:
        if left_l[i] < right_l[j]:
            sorted_list.append(left_l[i])
            i += 1
        else:
            sorted_list.append(right_l[j])
            j += 1
    sorted_list += left_l[i:] + right_l[j:]
    return sorted_list


def merge_sort(for_sort):
    n1 = len(for_sort) // 2
    a1 = for_sort[:n1]
    a2 = for_sort[n1:]

    if len(a1) > 1:
        a1 = merge_sort(a1)
    if len(a2) > 1:
        a2 = merge_sort(a2)

    return merge_two_list(a1, a2)


# # @decor
# def decor_merge_sort(for_sort):
#     return merge_sort(for_sort)


# Вариант с урока
# @decor
def merge_sort_lesson(lst_obj):
    if len(lst_obj) > 1:
        center = len(lst_obj) // 2
        left = lst_obj[:center]
        right = lst_obj[center:]

        merge_sort_lesson(left)
        merge_sort_lesson(right)

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


if __name__ == '__main__':
    """
    Среднее время алгоритма O(n log n), он работает гораздо быстрее алгоритмов O(n^2) (Выбором, Вставками, Пузырьком)
    что хорошо видно при увеличении массива, но он более объемный по памяти, так создает новый массив.
    Разница в работе алгоритма с уроки и другой его вариант, почти не видна, все в рамках погрешности...

    ************************* Число элементов: 5 *************************
    Вариант с урока Time: 0.003723665000000001
    Другой вариант Time: 0.0035449750000000058
    Исходный - [46.020100459094316, 11.19446540507061, 47.111120251472286, 13.55701726875736, 24.055156991603077]
    Отсортированный_1 - [11.19446540507061, 13.55701726875736, 24.055156991603077, 46.020100459094316, 47.111120251472286]
    Отсортированный_2 - [11.19446540507061, 13.55701726875736, 24.055156991603077, 46.020100459094316, 47.111120251472286]

    ************************* Число элементов: 100 *************************
    Вариант с урока Time: 0.14470181000000001
    Другой вариант Time: 0.12610135500000003

    ************************* Число элементов: 1000 *************************
    Вариант с урока Time: 1.9786017819999997
    Другой вариант Time: 1.665565966
    """

    print(f'{"*" * 25} Число элементов: 5 {"*" * 25}')
    arr_10 = [rnd.uniform(0, 49) for _ in range(5)]  # uniform дает число с плавающей точкой
    print(f'Вариант с урока Time: {timeit("merge_sort_lesson(arr_10[:])", globals=globals(), number=1000)}')
    print(f'Другой вариант Time: {timeit("merge_sort(arr_10[:])", globals=globals(), number=1000)}')
    print(f'Исходный - {arr_10}')
    print(f'Отсортированный_1 - {merge_sort_lesson(arr_10[:])}')  # Memory: 0.01172
    print(f'Отсортированный_2 - {merge_sort(arr_10[:])}')  # Memory: 0.01172

    print(f'{"*" * 25} Число элементов: 100 {"*" * 25}')
    arr_100 = [rnd.uniform(0, 49) for _ in range(100)]  # uniform дает число с плавающей точкой
    print(f'Вариант с урока Time: {timeit("merge_sort_lesson(arr_100[:])", globals=globals(), number=1000)}')
    print(f'Другой вариант Time: {timeit("merge_sort(arr_100[:])", globals=globals(), number=1000)}')

    print(f'{"*" * 25} Число элементов: 1000 {"*" * 25}')
    arr_1000 = [rnd.uniform(0, 49) for _ in range(1000)]  # uniform дает число с плавающей точкой
    print(f'Вариант с урока Time: {timeit("merge_sort_lesson(arr_1000[:])", globals=globals(), number=1000)}')
    print(f'Другой вариант Time: {timeit("merge_sort(arr_1000[:])", globals=globals(), number=1000)}')
