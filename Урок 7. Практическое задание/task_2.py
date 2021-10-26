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
import timeit
import random


def merge_sort_1(lst_obj):
    if len(lst_obj) > 1:
        center = len(lst_obj) // 2
        left = lst_obj[:center]
        right = lst_obj[center:]

        merge_sort_1(left)
        merge_sort_1(right)

        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lst_obj[k] = left[i]
                i += 1
            else:
                lst_obj[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            lst_obj[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            lst_obj[k] = right[j]
            j += 1
            k += 1
        return lst_obj


# Еще один вариант самый понятный для меня который я нашел, для себя комментарии не удалил
def merge(left_list, right_list):
    sorted_list = []
    left_list_index = right_list_index = 0

    # Длина списков часто используется, поэтому создадим переменные для удобства
    left_list_length, right_list_length = len(left_list), len(right_list)

    for _ in range(left_list_length + right_list_length):
        if left_list_index < left_list_length and right_list_index < right_list_length:
            # Сравниваем первые элементы в начале каждого списка
            # Если первый элемент левого подсписка меньше, добавляем его
            # в отсортированный массив
            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
            # Если первый элемент правого подсписка меньше, добавляем его
            # в отсортированный массив
            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1

        # Если достигнут конец левого списка, элементы правого списка
        # добавляем в конец результирующего списка
        elif left_list_index == left_list_length:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1
        # Если достигнут конец правого списка, элементы левого списка
        # добавляем в отсортированный массив
        elif right_list_index == right_list_length:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1

    return sorted_list


def merge_sort(nums):
    # Возвращаем список, если он состоит из одного элемента
    if len(nums) <= 1:
        return nums

    # Для того чтобы найти середину списка, используем деление без остатка
    # Индексы должны быть integer
    mid = len(nums) // 2

    # Сортируем и объединяем подсписки
    left_list = merge_sort(nums[:mid])
    right_list = merge_sort(nums[mid:])

    # Объединяем отсортированные списки в результирующий
    return merge(left_list, right_list)


orig_list = [random.randint(-100, 100) for _ in range(10)]

# замеры 10
print("range 10:")
print("merge_sort_1: ",
      timeit.timeit(
          "merge_sort_1(orig_list[:])",
          globals=globals(),
          number=1000))
print("merge_sort: ",
      timeit.timeit(
          "merge_sort(orig_list[:])",
          globals=globals(),
          number=1000))

orig_list = [random.randint(-100, 100) for _ in range(100)]

# замеры 100
print("range 100:")
print("merge_sort_1: ",
      timeit.timeit(
          "merge_sort_1(orig_list[:])",
          globals=globals(),
          number=1000))
print("merge_sort: ",
      timeit.timeit(
          "merge_sort(orig_list[:])",
          globals=globals(),
          number=1000))

orig_list = [random.randint(-100, 100) for _ in range(1000)]

# замеры 1000
print("range 1000:")
print("merge_sort_1: ",
      timeit.timeit(
          "merge_sort_1(orig_list[:])",
          globals=globals(),
          number=1000))
print("merge_sort: ",
      timeit.timeit(
          "merge_sort(orig_list[:])",
          globals=globals(),
          number=1000))

print("The list is: " ,orig_list)
print("After function merge_sort_1: ",merge_sort_1(orig_list))
print("After function merge_sort: ",merge_sort(orig_list))

"""
range 10:
merge_sort_1:  0.04698660000000002
merge_sort:  0.03824560000000002
range 100:
merge_sort_1:  0.4204361
merge_sort:  0.4080661
range 1000:
merge_sort_1:  5.0071425
merge_sort:  4.127089600000001
"""
