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
from random import randint


# Попробовал сделать свой вариант, не глядя в пример


def rec_merge_sort(array):
    if len(array) == 1:
        return array
    elif len(array) == 2:
        if array[1] < array[0]:
            array[0], array[1] = array[1], array[0]
        return array
    elif len(array) > 2:
        left = rec_merge_sort(array[:len(array) // 2])
        right = rec_merge_sort(array[len(array) // 2:])
        array = []
        while left or right:
            if not left:
                array.append(right.pop(0))
            elif not right:
                array.append(left.pop(0))
            elif left[0] <= right[0]:
                array.append(left.pop(0))
            elif right[0] <= left[0]:
                array.append(right.pop(0))
        return array


my_list = [randint(0, 50) for i in range(100)]
result = rec_merge_sort(my_list[:])
print(all(result[i] <= result[i] for i in range(len(result) - 1)))


# Попытка сделать нерекурсивную сортировку слиянием:


def merge_sort(array):
    temp_list = []

    for i in range(0, len(array), 2):
        if i + 1 > len(array) - 1:
            temp_list.append([array[i]])
        else:
            a = array[i]
            b = array[i + 1]
            if b < a:
                a, b = b, a
            temp_list.append([a, b])

    temp_temp_list = []
    while len(temp_list[0]) != len(array):
        for i in range(0, len(temp_list), 2):
            if i + 1 > len(temp_list) - 1:
                sublist = temp_list[i]
            elif len(temp_list) >= i + 1:
                left = temp_list[i]
                right = temp_list[i + 1]
                sublist = []
                while left or right:
                    if not left:
                        sublist.append(right.pop(0))
                    elif not right:
                        sublist.append(left.pop(0))
                    elif left[0] <= right[0]:
                        sublist.append(left.pop(0))
                    elif right[0] < left[0]:
                        sublist.append(right.pop(0))
            temp_temp_list.append(sublist)
        else:
            temp_list = temp_temp_list
            temp_temp_list = []
    return temp_list[0]


result = merge_sort(my_list[:])
print(all(result[i] <= result[i] for i in range(len(result) - 1)))

my_list = [randint(0, 50) for i in range(10)]

print(f'Рекурсивная сортировка, 10 элементов: '
      f'{timeit("rec_merge_sort(my_list[:])", "from __main__ import rec_merge_sort, my_list", number=100)}')
print(f'Нерекурсивная сортировка, 10 элементов: '
      f'{timeit("merge_sort(my_list[:])", "from __main__ import merge_sort, my_list", number=100)}')

my_list = [randint(0, 50) for i in range(100)]

print(f'Рекурсивная сортировка, 100 элементов: '
      f'{timeit("rec_merge_sort(my_list[:])", "from __main__ import rec_merge_sort, my_list", number=100)}')
print(f'Нерекурсивная сортировка, 100 элементов: '
      f'{timeit("merge_sort(my_list[:])", "from __main__ import merge_sort, my_list", number=100)}')

my_list = [randint(0, 50) for i in range(1000)]

print(f'Рекурсивная сортировка, 1000 элементов: '
      f'{timeit("rec_merge_sort(my_list[:])", "from __main__ import rec_merge_sort, my_list", number=100)}')
print(f'Нерекурсивная сортировка, 1000 элементов: '
      f'{timeit("merge_sort(my_list[:])", "from __main__ import merge_sort, my_list", number=100)}')

my_list = [randint(0, 50) for i in range(10000)]

print(f'Рекурсивная сортировка, 10000 элементов: '
      f'{timeit("rec_merge_sort(my_list[:])", "from __main__ import rec_merge_sort, my_list", number=100)}')
print(f'Нерекурсивная сортировка, 10000 элементов: '
      f'{timeit("merge_sort(my_list[:])", "from __main__ import merge_sort, my_list", number=100)}')

"""
Рекурсивная сортировка слиянием в замерах показала себя немного быстрее
Замеры: 
Рекурсивная сортировка, 10 элементов: 0.0007779000000000015
Нерекурсивная сортировка, 10 элементов: 0.000834399999999999
Рекурсивная сортировка, 100 элементов: 0.013976999999999996
Нерекурсивная сортировка, 100 элементов: 0.013364500000000001
Рекурсивная сортировка, 1000 элементов: 0.19125769999999997
Нерекурсивная сортировка, 1000 элементов: 0.20052820000000002
Рекурсивная сортировка, 10000 элементов: 3.1741618
Нерекурсивная сортировка, 10000 элементов: 3.6357981

"""
