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


def merge(left, right):
    if len(left) == 0:
        return right
    if len(right) == 0:
        return left
    result = []
    index_left = index_right = 0
    while len(result) < len(left) + len(right):
        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1
        if index_right == len(right):
            result += left[index_left:]
            break
        if index_left == len(left):
            result += right[index_right:]
            break
    return result


def merge_sort(array):
    if len(array) < 2:
        return array
    midpoint = len(array) // 2
    return merge(
        left=merge_sort(array[:midpoint]),
        right=merge_sort(array[midpoint:]))


def gen_array(n):
    return [round(uniform(0.0, 49.99), 2) for _ in range(n)]


length = int(input('Введите число элементов: '))
my_array = gen_array(length)
print(f'Исходный - {my_array}')
print(f'Отсортированый - {merge_sort(my_array[:])}')

# Введите число элементов: 5
# Исходный - [25.95, 19.11, 25.07, 1.34, 14.94]
# Отсортированый - [1.34, 14.94, 19.11, 25.07, 25.95]

arr_10 = gen_array(10)
arr_100 = gen_array(100)
arr_1000 = gen_array(1000)

print('#' * 100)
print('Массив 10 элементов:',
      timeit('merge_sort(arr_10[:])', globals=globals(), number=1000))  # 0.01811738000014884
print('Массив 100 элементов:',
      timeit('merge_sort(arr_100[:])', globals=globals(), number=1000))  # 0.27594505100023525
print('Массив 1000 элементов:',
      timeit('merge_sort(arr_1000[:])', globals=globals(), number=1000))  # 4.102288875999875
# Массив 10 элементов: 0.01811738000014884
# Массив 100 элементов: 0.27594505100023525
# Массив 1000 элементов: 4.102288875999875
