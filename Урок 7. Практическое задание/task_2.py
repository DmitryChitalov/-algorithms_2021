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

from random import random, randint
from timeit import default_timer


def time_it(func):
    def wrapper(numb):
        start_time = default_timer()
        res = func(numb)
        print(default_timer() - start_time)
        return res
    return wrapper


def standard_mergesort(lst):
    if len(lst) == 1 or len(lst) == 1:
        return
    middle = len(lst) // 2
    l_lst, r_lst = lst[:middle], lst[middle:]
    standard_mergesort(l_lst)
    standard_mergesort(r_lst)

    # слияние массивов
    l_ind = r_ind = i = 0
    while l_ind < len(l_lst) and r_ind < len(r_lst):
        if l_lst[l_ind] <= r_lst[r_ind]:
            lst[i] = l_lst[l_ind]
            l_ind += 1
        else:
            lst[i] = r_lst[r_ind]
            r_ind += 1
        i += 1
    while l_ind < len(l_lst):
        lst[i] = l_lst[l_ind]
        l_ind += 1
        i += 1
    while r_ind < len(r_lst):
        lst[i] = r_lst[r_ind]
        r_ind += 1
        i += 1


def merge(left, right):
    result = list()
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left[0])
            del left[0]
        else:
            result.append(right[0])
            del right[0]
    while len(left) > 0:
        result.append(left[0])
        del left[0]
    while len(right) > 0:
        result.append(right[0])
        del right[0]
    return result


def mergesort(lst):
    if len(lst) <= 1:
        return lst
    else:
        middle = len(lst) // 2
        left = lst[:middle]
        right = lst[middle:]

        left = mergesort(left)
        right = mergesort(right)
        result = merge(left, right)
        return result


@time_it
def standard_mergesort_measure(lst):
    standard_mergesort(lst)


@time_it
def mergesort_measure(lst):
    return mergesort(lst)



print("Массив из 10 элементов:")
source_list = [round(random() * 50, 3) for _ in range(10)]
sorted_list = source_list[:]
print("Исходный массив: ", source_list)
print("\nСтандартная сортировка слиянием: ")
standard_mergesort_measure(sorted_list)
print(sorted_list)
print("Другая реализация: ")
sorted_list = mergesort_measure(source_list)
print(sorted_list)

print("\nМассив из 100 элементов:")
source_list = [round(random() * 50, 3) for _ in range(100)]
sorted_list = source_list[:]
print("Стандартная сортировка слиянием: ")
standard_mergesort_measure(sorted_list)
print("Другая реализация: ")
sorted_list = mergesort_measure(source_list)

print("\nМассив из 1000 элементов:")
source_list = [round(random() * 50, 3) for _ in range(1000)]
sorted_list = source_list[:]
print("Стандартная сортировка слиянием: ")
standard_mergesort_measure(sorted_list)
print("Другая реализация: ")
sorted_list = mergesort_measure(source_list)

print("\nМассив из 10000 элементов:")
source_list = [round(random() * 50, 3) for _ in range(10000)]
sorted_list = source_list[:]
print("Стандартная сортировка слиянием: ")
standard_mergesort_measure(sorted_list)
print("Другая реализация: ")
sorted_list = mergesort_measure(source_list)


'''
Результаты замеров
Массив из 10 элементов:
Стандартная сортировка слиянием: 
9.670000000000512e-05
Другая реализация: 
0.00010540000000000549

Массив из 100 элементов:
Стандартная сортировка слиянием: 
0.0007101999999999942
Другая реализация: 
0.0005486999999999853

Массив из 1000 элементов:
Стандартная сортировка слиянием: 
0.009278199999999986
Другая реализация: 
0.007194200000000012

Массив из 10000 элементов:
Стандартная сортировка слиянием: 
0.07938820000000002
Другая реализация: 
0.11841120000000005

Первый вариант сортировки слиянием (standard_mergesort) аналогичен варианту, предложенномуу на лекции.
Второй вариант использует дополнительную память для создания вспомогательных списков. 

Оба варианта выполняют сортировку за примерно одинаковое время.
В приведенном замере на списках длины 100 и 1000, второй вариант работает быстрее. Со списком из 10000 - первый.
Однако при многократном запуске можно увидеть, что то один, то другой вариант работает быстрее.
Оба варианта имеют сложность n*log(n).
'''

