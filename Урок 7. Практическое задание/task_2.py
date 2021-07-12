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
import timeit
import random
from urllib3.connectionpool import xrange

orig_list_10 = [random.randint(0, 50) for _ in range(10)]
orig_list_100 = [random.randint(0, 50) for _ in range(100)]
orig_list_1000 = [random.randint(0, 50) for _ in range(1000)]

# 1 Вариант
def merge_sort_1(a):
    def MergerGroup(a, left, m, right):
        if left >= right: return None
        if m < left or right < m: return None
        t = left
        for j in xrange(m + 1, right + 1):
            for i in xrange(t, j):
                if a[j] < a[i]:
                    r = a[j]
                    for k in xrange(j, i, -1):
                        a[k] = a[k - 1]
                    a[i] = r
                    t = i
                    break
    if len(a) < 2: return None
    k = 1
    while k < len(a):
        g = 0
        while g < len(a):
            z = g + k + k - 1
            r = z if z < len(a) else len(a) - 1
            MergerGroup(a, g, g + k - 1, r)
            g += 2 * k
        k *= 2
    return a


# 2 Вариант
def merge(left, right):
    lst = []
    while left and right:
        if left[0] < right[0]:
            lst.append(left.pop(0))
        else:
            lst.append(right.pop(0))
    if left:
        lst.extend(left)
    if right:
        lst.extend(right)
    return lst

def merge_sort_2(lst):
    length = len(lst)
    if length >= 2:
        mid = int(length / 2)
        lst = merge(merge_sort_2(lst[:mid]), merge_sort_2(lst[mid:]))
    return lst

print(f'Исходный при длине 10: {orig_list_10}')
print(f'Исходный при длине 100: {orig_list_100}')
print(f'Исходный при длине 1000: {orig_list_1000}')

print(f'1 Вариант. Отсортированный при длине 10: {merge_sort_1(orig_list_10)}')
print(f'1 Вариант. Отсортированный при длине 100: {merge_sort_1(orig_list_100)}')
print(f'1 Вариант. Отсортированный при длине 1000: {merge_sort_1(orig_list_1000)}')
print(f'2 Вариант. Отсортированный при длине 10: {merge_sort_2(orig_list_10)}')
print(f'2 Вариант. Отсортированный при длине 100: {merge_sort_2(orig_list_100)}')
print(f'2 Вариант. Отсортированный при длине 1000: {merge_sort_2(orig_list_1000)}')

print(f'Время на выполнение 1 варанта при длине 10: ',
    timeit.timeit(
        "merge_sort_1(orig_list_10[:])",
        globals=globals(),
        number=1000))
print(f'Время на выполнение 1 варанта при длине 100: ',
    timeit.timeit(
        "merge_sort_1(orig_list_100[:])",
        globals=globals(),
        number=1000))
print(f'Время на выполнение 1 варанта при длине 1000: ',
    timeit.timeit(
        "merge_sort_1(orig_list_1000[:])",
        globals=globals(),
        number=1000))

print(f'Время на выполнение 2 варанта при длине 10: ',
    timeit.timeit(
        "merge_sort_2(orig_list_10[:])",
        globals=globals(),
        number=1000))
print(f'Время на выполнение 2 варанта при длине 100: ',
    timeit.timeit(
        "merge_sort_2(orig_list_100[:])",
        globals=globals(),
        number=1000))
print(f'Время на выполнение 2 варанта при длине 1000: ',
    timeit.timeit(
        "merge_sort_2(orig_list_1000[:])",
        globals=globals(),
        number=1000))

# В этом листинге значительно дольше выполняется 1 вариант кода это связано с наличием в первом вложенных функций и циклов,
# а также использованием в 2 варианте встроенных функций