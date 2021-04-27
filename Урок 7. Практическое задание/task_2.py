"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран \nИсходный:
и Отсортированный: массивы.

Хотя в примерах к уроку уже есть вариант реализации слияния,
попробуйте предложить другой (придумать или найти)

И попытаться сделать замеры на массивах разной длины: 10, 100, 1000, ...

Пример:
Введите число элементов: 5
Исходный: - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""
import timeit
from random import uniform


def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result


def merge_sort_req(lst_obj):
    if len(lst_obj) < 2:
        return lst_obj[:]
    else:
        center = len(lst_obj) // 2
        left = merge_sort_req(lst_obj[:center])
        right = merge_sort_req(lst_obj[center:])
        return merge(left, right)


orig_list = [uniform(0, 50) for _ in range(10)]
print('\nИсходный:', orig_list)
print('Отсортированный:', merge_sort_req(orig_list))

print('Время выполнния merge_sort_req (10):',
      timeit.timeit(
          "merge_sort_req(orig_list[:])",
          globals=globals(),
          number=1000))

orig_list = [uniform(0, 50) for _ in range(100)]

print('\nИсходный:', orig_list)
print('Отсортированный:', merge_sort_req(orig_list))

print('Время выполнния merge_sort_req (100):',
      timeit.timeit(
          "merge_sort_req(orig_list[:])",
          globals=globals(),
          number=1000))

orig_list = [uniform(0, 50) for _ in range(1000)]

print('\nИсходный:', orig_list)
print('Отсортированный:', merge_sort_req(orig_list))

print('Время выполнния merge_sort_req (1000): ',
      timeit.timeit(
          "merge_sort_req(orig_list[:])",
          globals=globals(),
          number=1000))

"""
Результаты замеров: 

Время выполнния merge_sort_req (10): 0.012321991000000001
Время выполнния merge_sort_req (100): 0.187656772
Время выполнния merge_sort_req (1000):  2.6930563449999996

"""
