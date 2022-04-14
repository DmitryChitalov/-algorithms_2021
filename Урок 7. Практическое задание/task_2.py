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


def merge_list(l_half1, l_half2):
    sorted_list = []
    i = 0
    j = 0
    while i < len(l_half1) and j < len(l_half2):
        if l_half1[i] < l_half2[j]:
            sorted_list.append(l_half1[i])
            i += 1
        else:
            sorted_list.append(l_half2[j])
            j += 1

    sorted_list += l_half1[i:] + l_half2[j:]
    return sorted_list


def merge_sort(lst):
    middle = len(lst) // 2
    l1 = lst[:middle]
    l2 = lst[middle:]

    if len(l1) > 1:
        l1 = merge_sort(l1)
    if len(l2) > 1:
        l2 = merge_sort(l2)

    result = merge_list(l1, l2)
    return result


if __name__ == '__main__':

    test_list1 = [random.uniform(0, 50) for _ in range(10)]
    test_list2 = [random.uniform(0, 50) for _ in range(100)]
    test_list3 = [random.uniform(0, 50) for _ in range(1000)]
    print(timeit.timeit("merge_sort(test_list1[:])", globals=globals(), number=10))
    print(timeit.timeit("merge_sort(test_list2[:])", globals=globals(), number=10))
    print(timeit.timeit("merge_sort(test_list3[:])", globals=globals(), number=10))


"""
Время выполнения сортировки методом слияния растет прямо пропорциональна размеру
массива. Замеры показывают 10 кратное увеличение времени при 10-кратном увеличении массива.

0.0001228999999999987
0.0021338000000000017
0.0252261
"""