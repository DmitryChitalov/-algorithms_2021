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
import random
import timeit


def merge(list_1, list_2):
    i = 0
    j = 0
    result_list = []
    while i < len(list_1) and j < len(list_2):
        if list_1[i] < list_2[j]:
            result_list.append(list_1[i])
            i += 1
        else:
            result_list.append(list_2[j])
            j += 1
    result_list.extend(list_1[i:])
    result_list.extend(list_2[j:])
    return result_list


def sort_merge(list_arg):
    if len(list_arg) > 1:
        return merge(sort_merge(list_arg[len(list_arg) // 2:]), sort_merge(list_arg[: len(list_arg) // 2]))
    else:
        return list_arg


list_test = [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
print(sort_merge(list_test))
# [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]


list_10 = [random.randint(0, 10) for i in range(10)]
list_100 = [random.randint(0, 10) for i in range(100)]
list_1000 = [random.randint(0, 10) for i in range(1000)]

print(timeit.timeit('sort_merge(list_10)', globals=globals(), number=1000))
print(timeit.timeit('sort_merge(list_100)', globals=globals(), number=1000))
print(timeit.timeit('sort_merge(list_1000)', globals=globals(), number=1000))

'''
0.023157799999999996
0.2071731
2.8754404
'''