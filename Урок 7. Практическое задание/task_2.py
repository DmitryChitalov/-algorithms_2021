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


def sorted_by_murge(lst_obj):
    if len(lst_obj) > 1:
        center = len(lst_obj) // 2
        left = lst_obj[:center]
        right = lst_obj[center:]

        sorted_by_murge(left)
        sorted_by_murge(right)

        # перестали делить
        # выполняем слияние
        m, j, k = 0, 0, 0

        while m < len(left) and j < len(right):
            if left[m] < right[j]:
                lst_obj[k] = left[m]
                m += 1
            else:
                lst_obj[k] = right[j]
                j += 1
            k += 1

        while m < len(left):
            lst_obj[k] = left[m]
            m += 1
            k += 1

        while j < len(right):
            lst_obj[k] = right[j]
            j += 1
            k += 1
        return lst_obj


values_of_list = int(input('Введите число элементов, если введете 0, то сделаются замеры на массивах разной длины: '
                           '10, 100, 1000, ... : '))


if values_of_list == 0:
    random_list = [random.uniform(-100, 100) for i in range(10)]

    # замеры 10
    print(
        timeit.timeit(
            "sorted_by_murge(random_list[:])",
            globals=globals(),
            number=1000),
        f'\nИсходный массив - {random_list};\nОтсортированный массив - {sorted_by_murge(random_list[:])}.')

    random_list = [random.uniform(-100, 100) for i in range(100)]

    # замеры 100
    print(
        timeit.timeit(
            "sorted_by_murge(random_list[:])",
            globals=globals(),
            number=1000),
        f'\nИсходный массив - {random_list};\nОтсортированный массив - {sorted_by_murge(random_list[:])}.')

    random_list = [random.uniform(-100, 100) for i in range(1000)]

    # замеры 1000
    print(
        timeit.timeit(
            "sorted_by_murge(random_list[:])",
            globals=globals(),
            number=1000),
        f'\nИсходный массив - {random_list};\nОтсортированный массив - {sorted_by_murge(random_list[:])}.')

    random_list = [random.uniform(-100, 100) for i in range(10000)]

    # замеры 10000
    print(
        timeit.timeit(
            "sorted_by_murge(random_list[:])",
            globals=globals(),
            number=1000),
        f'\nИсходный массив - {random_list};\nОтсортированный массив - {sorted_by_murge(random_list[:])}.')

else:
    random_list = [random.uniform(-100, 100) for i in range(values_of_list)]
    # замеры пользователя
    print(
        timeit.timeit(
            "sorted_by_murge(random_list[:])",
            globals=globals(),
            number=1000),
        f'\nИсходный массив - {random_list};\nОтсортированный массив - {sorted_by_murge(random_list[:])}.')