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
from timeit import timeit


my_list = [random() * 50 for i in range(int(input("Введите число элементов: ")))]
my_list_1 = [randint(-100, 100) for i in range(1000)]

def merge_sort(lst_obj):
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


def merge_sort_2(a):
    n = len(a)
    if n < 2:
        return a
    l = merge_sort_2(a[:n//2])
    r = merge_sort_2(a[n//2:n])
    i = j = 0
    result = []
    while i < len(l) or j < len(r):
        if not i < len(l):
            result.append(r[j])
            j += 1
        elif not j < len(r):
            result.append(l[i])
            i += 1
        elif l[i] < r[j]:
            result.append(l[i])
            i += 1
        else:
            result.append(r[j])
            j += 1
    return result

print(timeit('merge_sort(my_list[:])', globals=globals(), number=1))
print(timeit('merge_sort_2(my_list[:])', globals=globals(), number=1))

print(my_list)
print(merge_sort(my_list[:]))
print(merge_sort(my_list[:]))

# Массив равен 10: merge_sort - 6.616499999978487e-05
#                 merge_sort_2 - 7.798100000044883e-05
# Массив равен 100: merge_sort - 0.000787843999999982
#                 merge_sort_2 - 0.0009542030000000423
# Массив равен 1000: merge_sort - 0.010807211999999566
#                 merge_sort_2 - 0.012290740000000078
