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
from timeit import timeit
import random


def merge_list(left, right):
    left_course = 0
    right_course = 0
    result = []

    while len(left) > left_course and len(right) > right_course:
        if left[left_course] < right[right_course]:
            result.append(left[left_course])
            left_course += 1
        else:
            result.append(right[right_course])
            right_course += 1

    if len(left) > left_course:
        result += left[left_course:]
    if len(right) > right_course:
        result += right[right_course:]
    return result


def merge_sort(array):
    if len(array) == 1:
        return array
    middle = len(array) // 2
    left = merge_sort(array[:middle])
    right = merge_sort(array[middle:])
    return merge_list(left, right)


user_array = [random.random() * 50 for num in range(int(input('Введите число элементов: ')))]
array = user_array[:]

print(array)
print(merge_sort(user_array[:]))

user_array_10 = [random.random() * 50 for num in range(10)]
user_array_100 = [random.random() * 50 for num in range(100)]
user_array_1000 = [random.random() * 50 for num in range(1000)]

print(timeit('merge_sort(user_array_10[:])', globals=globals(), number=1000))
print(timeit('merge_sort(user_array_100[:])', globals=globals(), number=1000))
print(timeit('merge_sort(user_array_1000[:])', globals=globals(), number=1000))

"""
При реализации варианта решения не опирался на вариант с лекции и пробовал реализовать сам. 
Столкнулся с проблемой склейки 2х отсортированных массивов, но когда разобрался пришел к такому решению.

Из замеров видно, что при увеличении кол-ва элементов массива увеличивается и время сортировки: 
0.016649099999999972
0.2361114999999998
3.4370882999999997 
"""