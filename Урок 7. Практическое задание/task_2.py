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

from random import uniform
from timeit import timeit


def vector_gen_range(count):
    return [uniform(0, 50) for i in range(count)]


def merge_sort(vector):
    n = len(vector)
    if n < 2:
        return vector

    left = merge_sort(vector[:n//2])
    right = merge_sort(vector[n//2:n])

    i = j = 0
    res = []
    while i < len(left) or j < len(right):
        if not i < len(left):
            res.append(right[j])
            j += 1
        elif not j < len(right):
            res.append(left[i])
            i += 1
        elif left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1

    return res


low_vector = vector_gen_range(10)
mid_vector = vector_gen_range(100)
top_vector = vector_gen_range(1000)


vector_len = int(input('Введите число элементов: '))
user_vector = vector_gen_range(vector_len)
print(f'Исходный - {user_vector}\n'
      f'Отсортированный - {merge_sort(user_vector)}')


print(
    timeit("merge_sort(low_vector)",
           globals=globals(),
           number=1000))

print(
    timeit("merge_sort(mid_vector)",
           globals=globals(),
           number=1000))

print(
    timeit("merge_sort(top_vector)",
           globals=globals(),
           number=1000))

"""
Результыта замеров:
0.020174899999999774
0.33899290000000004
4.845047800000001

Вывод: Решение быстрое, но не самое =) та же сортировка пузырьком из 
предыдущего задания, содержит в 4 раза больше элементов
 и работает в 4 раза быстрее.
"""
