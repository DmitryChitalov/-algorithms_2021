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
from random import uniform
from timeit import timeit


def merge_sort(lst_obj):
    len_lst = len(lst_obj)
    if len_lst < 2:
        return lst_obj
    left = merge_sort(lst_obj[:len_lst // 2])
    right = merge_sort(lst_obj[len_lst // 2:len_lst])

    i, j = 0, 0
    result = []

    while i < len(left) or j < len(right):
        if not i < len(left):
            result.append(right[j])
            j += 1
        elif not j < len(right):
            result.append(left[i])
            i += 1
        elif left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    return result


user_n = int(input('Введите число элементов: '))
user_lst = [uniform(0, 50) for _ in range(user_n)]
print(f'Ваш исходный список - {user_lst}')
print(f'Ваш отсортированный список - {merge_sort(user_lst)}')

test_lst_10 = [uniform(0, 50) for _ in range(10)]
test_lst_100 = [uniform(0, 50) for _ in range(100)]
test_lst_1000 = [uniform(0, 50) for _ in range(1000)]
print(f'Слияние сортировкой 10 элементов: {timeit("merge_sort(test_lst_10[:])", globals=globals(), number=1000)}')
print(f'Слияние сортировкой 100 элементов: {timeit("merge_sort(test_lst_100[:])", globals=globals(), number=1000)}')
print(f'Слияние сортировкой 1000 элементов: {timeit("merge_sort(test_lst_1000[:])", globals=globals(), number=1000)}')

"""
Слияние сортировкой 10 элементов: 0.014106599999999858
Слияние сортировкой 100 элементов: 0.21671970000000007
Слияние сортировкой 1000 элементов: 3.0555687

Вывод: можно сказать, что сортировка с помощью слияния достаточно быстрый и эффективный способ сортировки,
однако стоит учесть, что данный способ не столь эффективный в плане затрат памяти.
"""
