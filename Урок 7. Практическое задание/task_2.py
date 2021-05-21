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


def merge_list(one, too):
    lst = []
    i = j = 0
    while i < len(one) and j < len(too):
        if one[i] < too[j]:
            lst.append(one[i])
            i += 1
        else:
            lst.append(too[j])
            j += 1
    if i < len(one):
        lst += one[i:]
    if j < len(too):
        lst += too[j:]
    return lst


def merge_sort(lst):
    if len(lst) == 1:
        return lst
    middle = len(lst) // 2
    left = merge_sort(lst[:middle])
    rigth = merge_sort(lst[middle:])
    return merge_list(left, rigth)


def different_size():
    quantity_el = int(input('Введите число элементов: '))
    orig_list = [random.randint(0, 50) + random.random() for _ in range(quantity_el)]
    return f'Исходный - {orig_list}\nОтсортированный - {merge_sort(orig_list)}'


print(different_size())
orig_list = [random.randint(0, 50) + random.random() for _ in range(10)]

# замеры 10
print(
    timeit.timeit(
        "merge_sort(orig_list[:])",
        globals=globals(),
        number=1000))
print('_____10 элементов_____')
orig_list2 = [random.randint(0, 50) + random.random() for _ in range(100)]
# замеры 100
print(
    timeit.timeit(
        "merge_sort(orig_list2[:])",
        globals=globals(),
        number=1000))
print('_____100 элементов_____')
orig_list3 = [random.randint(0, 50) + random.random() for _ in range(1000)]
# замеры 1000
print(
    timeit.timeit(
        "merge_sort(orig_list3[:])",
        globals=globals(),
        number=1000))
print('_____1000 элементов_____')