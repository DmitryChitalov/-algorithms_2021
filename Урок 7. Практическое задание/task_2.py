from random import randint
from timeit import timeit

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


def merge_sort(lst, start, end):
    if end - start > 1:
        mid = (start + end) // 2
        merge_sort(lst, start, mid)
        merge_sort(lst, mid, end)
        merge_list(lst, start, mid, end)
    return my_lst


def merge_list(lst, start, mid, end):
    left = lst[start:mid]
    right = lst[mid:end]
    k = start
    i = 0
    j = 0
    while start + i < mid and mid + j < end:
        if left[i] <= right[j]:
            lst[k] = left[i]
            i = i + 1
        else:
            lst[k] = right[j]
            j = j + 1
        k = k + 1
    if start + i < mid:
        while k < end:
            lst[k] = left[i]
            i = i + 1
            k = k + 1
    else:
        while k < end:
            lst[k] = right[j]
            j = j + 1
            k = k + 1


number = int(input('Введите число элементов: '))
my_lst = [randint(0, 50) for x in range(number)]
print(f' Исходный массив - {my_lst}')
print(f' Отсортированный массив - {merge_sort(my_lst,0,len(my_lst))}')
print('Время выполнения - ', timeit(
        "merge_sort(my_lst[:], 0, len(my_lst))",
        globals=globals(),
        number=10000
    )
)

"""
10 элементов - время выполнения -  0.13536709999999985
100 элементов - время выполнения -  1.9419784999999994
1000 элементов - время выполнения -  27.127406800000003
"""