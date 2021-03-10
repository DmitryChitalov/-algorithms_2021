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
from timeit import timeit


def merge_sort(nums):
    if len(nums) > 1:
        center = len(nums) // 2
        left = nums[:center]
        right = nums[center:]

        merge_sort(left)
        merge_sort(right)

        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1
        return nums


numbers = int(input('Введите число элементов: '))
test = [random.uniform(0, 50) for _ in range(numbers)]
print(f'Исходный  - {test}')
print(f'Отсортированный - {merge_sort(test)}')

n_10 = [random.uniform(0, 50) for _ in range(10)]
n_100 = [random.uniform(0, 50) for _ in range(100)]
n_1000 = [random.uniform(0, 50) for _ in range(1000)]
print('Массив из 10 чисел', timeit('merge_sort(n_10)', globals=globals(), number=1000))
print('Массив из 100 чисел', timeit('merge_sort(n_100)', globals=globals(), number=1000))
print('Массив из 1000 чисел', timeit('merge_sort(n_1000)', globals=globals(), number=1000))
