"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50]. Выведите на экран исходный
и отсортированный массивы.
Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""

import timeit
import random


def merge_sort(lst_obj):
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


def bubble_sort_3(lst_obj):
    n = 0
    while n < len(lst_obj):
        is_sorted = True
        for i in range(len(lst_obj) - 1, n, -1):
            if lst_obj[i - 1] > lst_obj[i]:
                lst_obj[i - 1], lst_obj[i] = lst_obj[i], lst_obj[i - 1]
                is_sorted = False
        if is_sorted:
            break
        n += 1
    return lst_obj


def my_print(*args):
    print('=-' * 50)
    print(f'Кол-во элементов: {len(args[0])}\nИсходный список:\n{args[0]}')
    print(f'Отсортированный список:\n{args[1]}')
    print('*' * 50)


orig_list_10 = [random.uniform(0.0, 50.0) for _ in range(10)]
orig_list_100 = [random.uniform(0.0, 50.0) for _ in range(100)]
orig_list_1000 = [random.uniform(0.0, 50.0) for _ in range(1000)]

# замеры 10
sorted_list_10 = merge_sort(orig_list_10[:])
my_print(orig_list_10, sorted_list_10)

print(f'Сортировка методом слияния:'
      f'{timeit.timeit("merge_sort(orig_list_10[:])",globals=globals(),number=1000)}')
print(f'Сортировка методом "пузырька":'
      f'{timeit.timeit("bubble_sort_3(orig_list_10[:])",globals=globals(),number=1000)}')

# замеры 100
sorted_list_100 = merge_sort(orig_list_100[:])
my_print(orig_list_100, sorted_list_100)

print(f'Сортировка методом слияния:'
      f'{timeit.timeit("merge_sort(orig_list_100[:])",globals=globals(),number=1000)}')
print(f'Сортировка методом "пузырька":'
      f'{timeit.timeit("bubble_sort_3(orig_list_100[:])",globals=globals(),number=1000)}')

# замеры 1000
sorted_list_1000 = merge_sort(orig_list_1000[:])
my_print(orig_list_1000, sorted_list_1000)
print(f'Сортировка методом слияния:'
      f'{timeit.timeit("merge_sort(orig_list_1000[:])",globals=globals(),number=1000)}')
print(f'Сортировка методом "пузырька":'
      f'{timeit.timeit("bubble_sort_3(orig_list_1000[:])",globals=globals(),number=1000)}')


"""
10 элементов
Сортировка методом слияния: 0.018748700000000007
Сортировка методом "пузырька": 0.012320999999999999

100 элементов
Сортировка методом слияния: 0.1804775
Сортировка методом "пузырька": 0.6891435000000001

1000 элементов
Сортировка методом слияния: 2.5484662
Сортировка методом "пузырька": 72.4991071

Вывод.
Если на десяти элементах пузырьковая сортировка опережает сортировку методом слияния, то при увеличении кол-ва
элементов слияние не оставляет "пузырькам" ни одного шанса.
Цифры говорят сами за себя.
"""
