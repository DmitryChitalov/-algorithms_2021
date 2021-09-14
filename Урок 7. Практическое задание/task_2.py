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
import operator


def generate_list():
    return [random.uniform(0, 50) for _ in range(100)]


def merge_sort(L, compare=operator.lt):
    if len(L) < 2:
        return L[:]
    else:
        middle = int(len(L) / 2)
        left = merge_sort(L[:middle], compare)
        right = merge_sort(L[middle:], compare)
        return merge(left, right, compare)


def merge(left, right, compare):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
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

l = generate_list()
print(l)
new = merge_sort(l)
print(new)
print(
    f"Сортировка списка функцией merge_sort составила {timeit.timeit('merge_sort(l[:])', globals=globals(), number=1000)} секунд")
print(
    f"Сортировка списка функцией merge_sort составила {timeit.timeit('merge_sort(l[:])', globals=globals(), number=10000)} секунд")
print(
    f"Сортировка списка функцией merge_sort составила {timeit.timeit('merge_sort(l[:])', globals=globals(), number=100000)} секунд")

# Сортировка списка функцией merge_sort составила 0.5412807000000001 секунд
# Сортировка списка функцией merge_sort составила 4.6127882 секунд
# Сортировка списка функцией merge_sort составила 46.2698552 секунд
