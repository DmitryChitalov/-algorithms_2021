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


from random import randint
from timeit import timeit


def create_random_list(num):
    unsorted_list = [randint(0, 49) for _ in range(num)]
    print('Неотсортированный список:', unsorted_list)
    return unsorted_list


def merge_sort(list):
    list_length = len(list)
    if list_length == 1:
        return list
    mid_point = list_length // 2
    left_partition = merge_sort(list[:mid_point])
    right_partition = merge_sort(list[mid_point:])
    return merge(left_partition, right_partition)


def merge(left, right):
    output = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            output.append(left[i])
            i += 1
        else:
            output.append(right[j])
            j += 1
    output.extend(left[i:])
    output.extend(right[j:])
    return output


def test_time():
    print(
        timeit("print('Отсортированный список:', merge_sort(create_random_list(10)))", globals=globals(), number=100),
        timeit("print('Отсортированный список:', merge_sort(create_random_list(100)))", globals=globals(), number=100),
        timeit("print('Отсортированный список:', merge_sort(create_random_list(1000)))", globals=globals(), number=100))


# Сортировка слиянием работает лучше, поэтому разница в скорости между 10, 100, 1000 не такая значительная.


if __name__ == '__main__':
    test_time()
