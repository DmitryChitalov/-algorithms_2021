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
from operator import lt
from random import uniform
from timeit import timeit


def merge_sort(s_list, compare=lt):
    if len(s_list) < 2:
        return s_list[:]
    else:
        middle = int(len(s_list)/2)
        left = merge_sort(s_list[:middle], compare)
        right = merge_sort(s_list[middle:], compare)
        return merge(left, right, compare)


def merge(left, right, compare):
    res_list = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            res_list.append(left[i])
            i += 1
        else:
            res_list.append(right[j])
            j += 1
    while i < len(left):
        res_list.append(left[i])
        i += 1
    while j < len(right):
        res_list.append(right[j])
        j += 1
    return res_list


main_list = [uniform(0.0, 50.0) for _ in range(10)]
main_list_2 = [uniform(0.0, 50.0) for _ in range(100)]
main_list_3 = [uniform(0.0, 50.0) for _ in range(1000)]


print(f'Main list: {main_list[:]}\n'
      f'Sorted List: {merge_sort(main_list)[:]}\n'
      f'{"~"*70}\n'
      f'Time for merge sort. 10 elements: '
      f'{timeit("merge_sort(main_list)[:]", globals=globals(), number=100)}\n'
      f'Time for merge sort. 100 elements: '
      f'{timeit("merge_sort(main_list_2)[:]", globals=globals(), number=100)}\n'
      f'Time for merge sort. 1000 elements: '
      f'{timeit("merge_sort(main_list_3)[:]", globals=globals(), number=100)}\n')

"""
Неплохо показывает себя при сортировке объемных списков из-за сложности О(n log n). 
Для примера, один из запусков, когда на 1000 элементов отработало быстрее, чем для 100

Main list: [46.12604358177222, 37.75219749022535, 40.45600934659902, 11.61221611052589, 45.904240224438844, 
            28.300200209560717, 19.955551332964795, 41.830353828786095, 12.667995019174539, 33.21743538327618]
Sorted List: [11.61221611052589, 12.667995019174539, 19.955551332964795, 28.300200209560717, 33.21743538327618, 
              37.75219749022535, 40.45600934659902, 41.830353828786095, 45.904240224438844, 46.12604358177222]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Time for merge sort. 10 elements: 0.0014445979995798552
Time for merge sort. 100 elements: 0.020859456000835053
Time for merge sort. 1000 elements: 0.26079688199934026

Time for merge sort. 10 elements: 0.0014785540006414521
Time for merge sort. 100 elements: 0.025499850999040063
Time for merge sort. 1000 elements: 0.2457494640002551

"""
