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

from timeit import timeit
from random import uniform


def merge(left_part, right_part):
    sort_list = []
    left_index = right_index = 0

    left_len, right_len = len(left_part), len(right_part)

    for _ in range(left_len + right_len):
        if left_index < left_len and right_index < right_len:
            if left_part[left_index] >= right_part[right_index]:
                sort_list.append(left_part[left_index])
                left_index += 1
            else:
                sort_list.append(right_part[right_index])
                right_index += 1
        elif left_index == left_len:
            sort_list.append(right_part[right_index])
            right_index += 1
        elif right_index == right_len:
            sort_list.append(left_part[left_index])
            left_index += 1
    return sort_list


def merge_sort(nums):
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2
    left_part = merge_sort(nums[:mid])
    right_part = merge_sort(nums[mid:])
    return merge(left_part, right_part)


try:
    amt = int(input('Введите число элементов: '))
    random_list = [uniform(0, 50) for _ in range(amt)]
    print('Исходный список -', random_list)
    print('Отсортированный список -', merge_sort(random_list))
except ValueError:
    print('Нужно ввести число, а не букву или другой символ!')

'''
Пример работы:
Введите число элементов: 5
Исходный список - [24.19262044256072, 22.436884752693025, 14.376628882212556, 
44.267367500027405, 46.59413358264855]
Отсортированный список - [46.59413358264855, 44.267367500027405, 24.19262044256072, 
22.436884752693025, 14.376628882212556]
'''

# замеры времени:
print(timeit("merge_sort(random_list[:])", globals=globals(), number=1000))

'''
Вывод на небольших размерах массива работает быстро.
На размерах массива 1000 цифры уже намного крупнее. Скорость алгоритма вполне
приемлема для метода слияния. У него должна быть сложность O(n log n).
0.056281096000020625 - длина массива 10
0.21759875600037049 - длина массива 100
1.9373899359998177 - длина массива 1000
'''
