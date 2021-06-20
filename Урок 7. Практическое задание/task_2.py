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

from random import random
from timeit import timeit


def merge(left, right):
    sorted_list = []
    left_index = right_index = 0

    for _ in range(len(left) + len(right)):
        if left_index < len(left) and right_index < len(right):
            # Сравниваем первые элементы в начале каждого списка
            # Если первый элемент левого подсписка меньше, добавляем его
            # в отсортированный массив
            if left[left_index] <= right[right_index]:
                sorted_list.append(left[left_index])
                left_index += 1
            # Если первый элемент правого подсписка меньше, добавляем его
            # в отсортированный массив
            else:
                sorted_list.append(right[right_index])
                right_index += 1

        # Если достигнут конец левого списка, элементы правого списка
        # добавляем в конец результирующего списка
        elif left_index == len(left):
            sorted_list.append(right[right_index])
            right_index += 1
        # Если достигнут конец правого списка, элементы левого списка
        # добавляем в отсортированный массив
        elif right_index == len(right):
            sorted_list.append(left[left_index])
            left_index += 1
    return sorted_list


def merge_sort(my_list):
    # Возвращаем список, если он состоит из одного элемента
    if len(my_list) <= 1:
        return my_list

    # Для того чтобы найти середину списка, используем деление без остатка
    # Индексы должны быть integer
    mid = len(my_list) // 2

    # Сортируем и объединяем подсписки
    left = merge_sort(my_list[:mid])
    right = merge_sort(my_list[mid:])

    # Объединяем отсортированные списки в результирующий
    return merge(left, right)


n = int(input("Введите число элементов: "))
my_list = [round(random() * 100, 4) for _ in range(n)]
print("Исходный список: ", my_list)
print("Отсортированный список: ", merge_sort(my_list[:]))

# замеряем на массиве из 10 элементов
print("\nЗамеряем на массиве из 10 элементов")
my_list = [round(random() * 100, 4) for _ in range(10)]
print(timeit("merge_sort(my_list[:])", globals=globals(), number=1000))

# замеряем на массиве из 100 элементов
print("\nЗамеряем на массиве из 100 элементов")
my_list = [round(random() * 100, 4) for _ in range(100)]
print(timeit("merge_sort(my_list[:])", globals=globals(), number=1000))

# замеряем на массиве из 1000 элементов
print("\nЗамеряем на массиве из 1000 элементов")
my_list = [round(random() * 100, 4) for _ in range(1000)]
print(timeit("merge_sort(my_list[:])", globals=globals(), number=1000))

"""
Результаты замеров:

Замеряем на массиве из 10 элементов
0.025537372000000058

Замеряем на массиве из 100 элементов
0.3979113860000001

Замеряем на массиве из 1000 элементов
5.725240299

"""