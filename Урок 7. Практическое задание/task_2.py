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


def merge_from_lesson(arr):
    if len(arr) > 1:
        center = len(arr) // 2
        left = arr[:center]
        right = arr[center:]

        merge_from_lesson(left)
        merge_from_lesson(right)

        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
        return arr


def merge_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    else:
        middle = int(len(arr) / 2)
        left = merge_sort(arr[:middle])
        right = merge_sort(arr[middle:])
        return merge(left, right)


def merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left[0])
            left = left[1:]
        else:
            result.append(right[0])
            right = right[1:]
    if len(left) > 0:
        result += left
    if len(right) > 0:
        result += right
    return result


lst_test_100 = [uniform(0, 50) for i in range(100)]
lst_test_1000 = [uniform(0, 50) for i in range(1000)]
lst_test_10000 = [uniform(0, 50) for i in range(10000)]

print('-' * 50, 'Сортировка слиянием из урока', '-' * 50)
print(
    f'Затраченное время на сортировку массива из 100 элементов:\n{timeit("merge_from_lesson(lst_test_100[:])", globals=globals(), number=1000)}\n'
    f'Затраченное время на сортировку массива из 1000 элементов:\n{timeit("merge_from_lesson(lst_test_1000[:])", globals=globals(), number=1000)}\n'
    f'Затраченное время на сортировку массива из 10000 элементов:\n{timeit("merge_from_lesson(lst_test_10000[:])", globals=globals(), number=1000)}')

print('-' * 50, 'Альтернативная сортировка слиянием', '-' * 50)
print(
    f'Затраченное время на сортировку массива из 100 элементов:\n{timeit("merge_sort(lst_test_100[:])", globals=globals(), number=1000)}\n'
    f'Затраченное время на сортировку массива из 1000 элементов:\n{timeit("merge_sort(lst_test_1000[:])", globals=globals(), number=1000)}\n'
    f'Затраченное время на сортировку массива из 10000 элементов:\n{timeit("merge_sort(lst_test_10000[:])", globals=globals(), number=1000)}')

print('-' * 50, 'Сортировка пользовательского массива', '-' * 50)
user_number = int(input('Введите число: '))
some_lst = [uniform(0, 50) for i in range(user_number)]

print(
    f'Массив из {user_number} элементов:\nИсходный массив - {some_lst}\nОтсортированный массив - {merge_sort(some_lst)}')
print('Затраченное время - ', timeit('merge_sort(some_lst)', globals=globals(), number=10000))

"""
Вывод:
Пример рассмотренный на уроке оказался быстрее. И если на массивах до 100 элементов это почти незаметно, то на массиве
в 10000 элементов скорость выше в 5 раз. 
Полагаю, мой пример меленнее из-за постоянной работы со срезами (создаются много новых объектов), в то время как 
пример из урока работает с индексами существующего объекта.
"""
