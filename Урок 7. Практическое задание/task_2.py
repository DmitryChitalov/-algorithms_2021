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


def merge_sort(arr):
    def merge(first, second):
        result = []
        i, j = 0, 0
        while i < len(first) and j < len(second):
            if first[i] < second[j]:
                result.append(first[i])
                i += 1
            else:
                result.append(second[j])
                j += 1

        result.extend(first[i:] if i < len(first) else second[j:])

        return result

    def div_half(lst):
        if len(lst) == 1:
            return lst
        elif len(lst) == 2:
            return lst if lst[0] <= lst[1] else lst[::-1]
        else:
            return merge(div_half(lst[:len(lst)//2]), div_half(lst[len(lst)//2:]))
    return div_half(arr)


def array_size():
    return int(input('Введите число элементов массива: '))


array = [round(uniform(-50, 50), 2) for _ in range(array_size())]

print(f'Исходный массив: {array}')
print(f'Отсортированный массив: {merge_sort(array[:])}')
print(timeit("merge_sort(array[:])", globals=globals(), number=1000))

'''
Замеры производились на 1000 запусков:
Массив на 
    10 элементов: сортировка происходит за 0.009118999999999877,
    100 элементов: сортировка происходит за 0.15257450000000006,
    1000 элементов: сортировка происходит за 2.0540494000000002
'''