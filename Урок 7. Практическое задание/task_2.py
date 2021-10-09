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


def merge_sort(my_mas):
    if len(my_mas) > 1:
        center = len(my_mas) // 2
        left = my_mas[:center]
        right = my_mas[center:]

        merge_sort(left)
        merge_sort(right)

        # перестали делить
        # выполняем слияние
        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                my_mas[k] = left[i]
                i += 1
            else:
                my_mas[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            my_mas[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            my_mas[k] = right[j]
            j += 1
            k += 1
        return my_mas


my_mas = [random.randint(0, 50) for _ in range(10)]

# замеры 10
print(
    timeit.timeit(
        "merge_sort(my_mas[:])",
        globals=globals(),
        number=1000))

orig_list = [random.randint(-100, 100) for _ in range(100)]

# замеры 100
print(
    timeit.timeit(
        "merge_sort(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [random.randint(-100, 100) for _ in range(1000)]

# замеры 1000
print(
    timeit.timeit(
        "merge_sort(orig_list[:])",
        globals=globals(),
        number=1000))


'''
0.022275099999999992
0.2340753
3.2659873
'''
