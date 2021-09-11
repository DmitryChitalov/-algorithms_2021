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

lst = [random.uniform(0, 50) for _ in range(100)]


def merge_sort(lst_obj):
    if len(lst_obj) > 1:
        center = len(lst_obj)//2
        left = iter(merge_sort(lst_obj[:center]))
        x1 = next(left)
        right = iter(merge_sort(lst_obj[center:]))
        x2 = next(right)
        lst_obj = []
        try:
            while True:
                if x1 <= x2:
                    lst_obj.append(x1)
                    x1 = next(left)
                else:
                    lst_obj.append(x2)
                    x2 = next(right)
        except:
            if x1 <= x2:
                lst_obj.append(x2)
                lst_obj.extend(right)
            else:
                lst_obj.append(x1)
                lst_obj.extend(left)
    return lst_obj


print(
    timeit.timeit(
        "merge_sort(lst[:])",
        globals=globals(),
        number=1000))
n = int(input('Enter the number of items\n'))
print(f'Original - {lst[:n]}')
print(f'Sorted - {merge_sort(lst)[:n]}')

"""
Work time of the def merge_sort:

range(10) - 0.010916999999999996
range(100) - 0.15149439999999997
range(1000) - 1.9128663000000001
"""
"""
Example of how the function works:

0.1567922
Enter the number of items
5
Original - [29.799093276085557, 41.33500328085662, 20.474986483408745, 44.16397993411609, 33.277957687104006]
Sorted - [0.11675317648334183, 0.44460108422031963, 1.6850934070044399, 1.766622793153605, 2.8098818156293612]
"""
