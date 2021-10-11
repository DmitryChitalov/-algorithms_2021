#!/usr/bin/env python3

from array import array
from random import uniform
from timeit import timeit


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

def sort(numbers):
    if len(numbers) > 1:
        center = len(numbers) // 2

        left = numbers[:center]
        right = numbers[center:]

        sort(left)
        sort(right)

        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                numbers[k] = left[i]
                i += 1
            else:
                numbers[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            numbers[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            numbers[k] = right[j]
            j += 1
            k += 1
        return numbers


def main():
    array = [uniform(0, 50) for _ in range(int(input('Введите число элементов: ')))]

    print(f'Исходный:   {array}')
    print(f'Отсортированный:   {sort(array)}')

    print('10 элементов - ', timeit('sort([uniform(0, 50) for _ in range(10)])', globals=globals(), number=1000))
    print('100 элементов - ', timeit('sort([uniform(0, 50) for _ in range(100)])', globals=globals(), number=1000))
    print('1000 элементов - ', timeit('sort([uniform(0, 50) for _ in range(1000)])', globals=globals(), number=1000))

if __name__ == '__main__':
    main()

'''
10 элементов -  0.022506313000121736
100 элементов -  0.26154428200061375
1000 элементов -  4.226396938000107
'''
