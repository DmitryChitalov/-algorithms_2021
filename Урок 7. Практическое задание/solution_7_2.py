from random import uniform
from timeit import timeit

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


def merge(a, b):
    """
    Сделал такой вариант, он является нисходящим, нашел в сети еще восходящий вариант без рекурсии,
    он написан на C#, пока не совсем с ним разобрался.
    :param a:
    :param b:
    :return:
    """
    res = []
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            res.append(a[i])
            i += 1
        else:
            res.append(b[j])
            j += 1
    res += a[i:] + b[j:]
    return res


def merge_sort(a):
    if len(a) <= 1:
        return a
    else:
        l = a[:len(a) // 2]
        r = a[len(a) // 2:]
    return merge(merge_sort(l), merge_sort(r))


try:
    orig_list = [uniform(0, 50) for _ in range(int(input('Введите число элементов: ')))]
    print('Исходный -', orig_list)
    print('Отсортированный -', merge_sort(orig_list[:]))

    print(timeit("merge_sort(orig_list[:])", globals=globals(), number=10))
    print(timeit("merge_sort(orig_list[:])", globals=globals(), number=100))
    print(timeit("merge_sort(orig_list[:])", globals=globals(), number=1000))

except ValueError:
    print('Необходимо ввести число')


