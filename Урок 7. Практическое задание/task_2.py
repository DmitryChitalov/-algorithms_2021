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


def my_merge_sort(lst_obj):
    if len(lst_obj) > 1:
        center = len(lst_obj) // 2
        left = lst_obj[:center]
        right = lst_obj[center:]

        merge_sort(left)
        merge_sort(right)

        lst_obj.clear()
        while len(left) > 0 and len(right) > 0:
            l_min = min(left)
            r_min = min(right)
            if min(left) <= min(right):
                lst_obj.append(left.pop(left.index(l_min)))
            else:
                lst_obj.append(right.pop(right.index(r_min)))

        if len(left):
            lst_obj.extend(left)
        else:
            lst_obj.extend(right)

        return lst_obj


def merge_sort(lst_obj):
    if len(lst_obj) > 1:
        center = len(lst_obj) // 2
        left = lst_obj[:center]
        right = lst_obj[center:]

        merge_sort(left)
        merge_sort(right)

        # перестали делить
        # выполняем слияние
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


if __name__ == '__main__':
    while True:
        try:
            n = int(input('Введите число элементов'))
            if n < 1:
                raise ValueError
        except ValueError:
            print(f'Введите натуральное число!')
        else:
            break

    a = [random.uniform(0, 50) for _ in range(n)]
    print(my_merge_sort(a[:]))

    stmt = [
        'my_merge_sort(a[:])',
        'merge_sort(a[:])'
    ]

    for st in stmt:
        print(f'на выполение функции {st} затрачено времени: '
              f'{timeit.timeit(st, setup="a =[random.uniform(0, 50) for _ in range(10)]", number=1000, globals=globals())}')

    for st in stmt:
        print(f'на выполение функции {st} затрачено времени: '
              f'{timeit.timeit(st, setup="a =[random.uniform(0, 50) for _ in range(100)]", number=1000, globals=globals())}')

    for st in stmt:
        print(f'на выполение функции {st} затрачено времени: '
              f'{timeit.timeit(st, setup="a =[random.uniform(0, 50) for _ in range(1000)]", number=1000, globals=globals())}')


"""
на выполение функции my_merge_sort(a[:]) затрачено времени: 0.013652900000000301
на выполение функции merge_sort(a[:]) затрачено времени: 0.008867500000000028
на выполение функции my_merge_sort(a[:]) затрачено времени: 0.2549701000000004
на выполение функции merge_sort(a[:]) затрачено времени: 0.1331857000000003
на выполение функции my_merge_sort(a[:]) затрачено времени: 10.1727028
на выполение функции merge_sort(a[:]) затрачено времени: 1.8164380999999992

Изначально предложенный вариант сортировки намного эффективнее за счет наличия в нем операция только лишь с константной
сложностью.
"""
