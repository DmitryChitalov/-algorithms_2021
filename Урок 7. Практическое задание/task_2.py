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
import random
unsorted_list_10 = [random.randint(-100, 100) for _ in range(10)]
unsorted_list_100 = [random.randint(-100, 100) for _ in range(100)]
unsorted_list_1000 = [random.randint(-100, 100) for _ in range(1000)]


def merge_join(a, b):
    fin_list = []
    c = d = 0
    while c < len(a) and d < len(b):
        if a[c] < b[d]:
            fin_list.append(a[c])
            c += 1
        else:
            fin_list.append(b[d])
            d += 1
    if c < len(a):
        fin_list += a[c:]
    if d < len(b):
        fin_list += b[d:]
    return fin_list


def merge_sort(lst_obj):
    if len(lst_obj) == 1:
        return lst_obj
    middle = len(lst_obj) // 2
    left = merge_sort(lst_obj[:middle])
    right = merge_sort(lst_obj[middle:])
    return merge_join(left, right)


print(timeit('merge_sort(unsorted_list_10[:])', globals=globals(), number=100))
'''0.0017966999999999983'''
print(timeit('merge_sort(unsorted_list_100[:])', globals=globals(), number=100))
'''0.024287500000000004'''
print(timeit('merge_sort(unsorted_list_1000[:])', globals=globals(), number=100))
'''31184829999999997'''
