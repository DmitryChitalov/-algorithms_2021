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
import timeit


def merge(left_list, right_list):
    sorted_list = []
    left_list_index = 0
    right_list_index = 0
    left_list_length = len(left_list)
    right_list_length = len(right_list)
    for i in range(left_list_length + right_list_length):
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


def merge_sort(input_array):
    if len(input_array) <= 1:
        return input_array
    middle = len(input_array) // 2
    left_list = merge_sort(input_array[:middle])
    right_list = merge_sort(input_array[middle:])
    return merge(left_list, right_list)


number_of_elems = int(input("Введите число элементов: "))

test_array = [random.uniform(0, 50) for _ in range(number_of_elems)]
print("Array to sort: ", test_array)

merge_sorted_array = merge_sort(test_array[:])
print("Sorted array: ", merge_sorted_array)

if merge_sorted_array == sorted(test_array):
    print("Algo is OK")

"""
Array to sort:  [48.24372134331545, 30.39838214549003, 31.678545414019805, 22.390062776716707, 43.09251936398804, 47.0417990376896, 17.72528317993033, 36.79679891212271, 7.993678604418452, 47.925479428787135]
Sorted array:  [7.993678604418452, 17.72528317993033, 22.390062776716707, 30.39838214549003, 31.678545414019805, 36.79679891212271, 43.09251936398804, 47.0417990376896, 47.925479428787135, 48.24372134331545]
Algo is OK

Функция сортировки слиянием дает такие же результаты, что и встроенная sorted(test_array), значит алгоритм работает
верно
"""


test_array = [random.uniform(0, 50) for _ in range(10)]
print(timeit.timeit("merge_sort(test_array[:])", globals=globals(), number=1000))
test_array = [random.uniform(0, 50) for _ in range(100)]
print(timeit.timeit("merge_sort(test_array[:])", globals=globals(), number=1000))
test_array = [random.uniform(0, 50) for _ in range(1000)]
print(timeit.timeit("merge_sort(test_array[:])", globals=globals(), number=1000))
test_array = [random.uniform(0, 50) for _ in range(10000)]
print(timeit.timeit("merge_sort(test_array[:])", globals=globals(), number=1000))

"""
10 elements:     0.024976400000000003
100 elements:    0.40298599999999996
1000 elements:   5.335869300000001
10000 elements:   64.5913922
Данный алгоритм работает значительно быстрее "пузырька"
"""
