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

from timeit import default_timer
from memory_profiler import memory_usage
from random import random


# Сделаем замеры при помощи декоратора:
def my_decor(func):
    def check_optimize(*args):
        t1 = default_timer()
        m1 = memory_usage()
        result = func(*args)
        m2 = memory_usage()
        t2 = default_timer()
        mem_res = m2[0] - m1[0]
        time_res = t2 - t1
        return f'Память: {mem_res},\nВремя: {time_res}', result
    return check_optimize


'''
Не до конца сообразил, как работает слияние, поэтому поискал код, отличающийся от
того, что был на занятии, чтобы получше разобраться
'''


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


@my_decor
def recur_decor(check_list):
    def merge_sort(sort_list):
        if len(sort_list) < 2:
            return sort_list
        mid = len(sort_list) // 2
        return merge(merge_sort(sort_list[:mid]), merge_sort(sort_list[mid:]))
    return merge_sort(check_list)


# Списки:
small_list = [random() * 100 for i in range(10)]
mid_list = [random() * 100 for j in range(1000)]
big_list = [random() * 100 for k in range(10000)]
huge_list = [random() * 100 for l in range(100000)]


# Проверки
info_1, result_1 = recur_decor(small_list[:])
info_2, result_2 = recur_decor(mid_list[:])
info_3, result_3 = recur_decor(big_list[:])
info_4, result_4 = recur_decor(huge_list[:])

print(f'Исходный: {small_list}\nОтсортированный: {result_1}')

print(info_1)
print(info_2)
print(info_3)
print(info_4)

'''
Результат: 

Исходный: [33.05765258338636, 54.81335120174943, 92.90669193395063, 69.22831115383794, 65.64333504873159, 57.52339189957403, 51.04593362767411, 97.85902830843285, 43.71754826678609, 66.26248790218632]
Отсортированный: [33.05765258338636, 43.71754826678609, 51.04593362767411, 54.81335120174943, 57.52339189957403, 65.64333504873159, 66.26248790218632, 69.22831115383794, 92.90669193395063, 97.85902830843285]

Память: 0.0,
Время: 0.21296890000000002

Память: 0.0,
Время: 0.22092160000000005

Память: 0.09375,
Время: 0.2821077000000001

Память: 0.8359375,
Время: 1.111424

По итогу видим, что функция выполняется достаточно таки быстро, при этом
в первых трех случаях затраты времени и памяти несущественны. В четвертом
случае уже можно видеть, что функции действительно требуется память, а
скорость ее выполнения для такого количества элементов относительно высокая.
'''
