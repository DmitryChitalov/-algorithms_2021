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
import random
import timeit


def merge(left_list, right_list):
    sorted_list = []
    left_list_index = right_list_index = 0

    left_list_length, right_list_length = len(left_list), len(right_list)

    for _ in range(left_list_length + right_list_length):
        if left_list_index < left_list_length and right_list_index < right_list_length:

            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1

            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1

        elif left_list_index == left_list_length:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1

        elif right_list_index == right_list_length:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1

    return sorted_list


def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left_list = merge_sort(nums[:mid])
    right_list = merge_sort(nums[mid:])
    return merge(left_list, right_list)


user_answer = int(input("Введите число элементов: "))
orig_list = [random.triangular(0, 50) for _ in range(user_answer)]
print(timeit.timeit("merge_sort(orig_list[:])", globals=globals(), number=100))
print("Исходный массив!")
print(orig_list)
orig_list = merge_sort(orig_list)
print("Отсортированный массив!")
print(orig_list)

"""
Время работы функции на 10 эллементах составила - 0.003090200000000043 сек.
Время работы функции на 100 эллементах составила - 0.07372519999999971 сек.
Время работы функции на 1000 эллементах составила - 0.9668078000000002 сек.
Время работы функции на 5000 эллементах составила - 5.7856838999999995 сек.
Вывод: с увелечением массива увеличиваеться и время работы, но на больших массивах,
т.к. на 5000 элементов время, не такое же большое как при сортировке пузырьком.
Поэтому по сранению с пызырьковой сортировкой, то слияние выигрывает на больших массивах,
а вот на меленьких проигрывает.
"""
