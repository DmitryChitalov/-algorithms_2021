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

from random import uniform, random
from timeit import timeit
from operator import lt

def merge_sort_1(lst_obj):
    if len(lst_obj) > 1:
        center = len(lst_obj) // 2
        left = lst_obj[:center]
        right = lst_obj[center:]

        merge_sort(left)
        merge_sort(right)

        # перестали делить
        # выполняем слияние
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

print()

def merge_sort(array_obj, compare=lt):
    if len(array_obj) < 2:
        return array_obj[:]
    else:
        middle = int(len(array_obj) / 2)
        left = merge_sort(array_obj[:middle], compare)
        right = merge_sort(array_obj[middle:], compare)
        return merge(left, right, compare)


def merge(left, right, compare):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result


k = int(input('Введите количество элементов списка: '))
source_list = [uniform(0, 50) for _ in range(k)] # или [float(random() * 50 for _ in range(k)]
print(f'Исходный список: {source_list}')

sorted_list = merge_sort(source_list[:])

print(f'Отсортированный список: {sorted_list}')
print()
print('Время сортировки слиянием на массивах разной длины: 10, 100, 1000, 10000, 100000 (число запусков 100):')
# for k in (10, 100, 1000, 10000, 100000):
#     source_list = [uniform(0, 50) for _ in range(k)]
#     print(timeit('merge_sort(source_list[:])', globals=globals(), number=100))

# Сложность Сортировки слиянием - O(n log n)
# Результаты:

#Введите количество элементов списка: 10
# Исходный список: [15.56295342604011, 3.6299385213627575, 38.43675376437854, 25.50252876541002, 40.95559390692746, 31.428647101369577, 26.20760630981479, 49.02957461413364, 26.145034335401686, 18.935148591617555]
# Отсортированный список: [3.6299385213627575, 15.56295342604011, 18.935148591617555, 25.50252876541002, 26.145034335401686, 26.20760630981479, 31.428647101369577, 38.43675376437854, 40.95559390692746, 49.02957461413364]

# Время сортировки слиянием на массивах разной длины: 10, 100, 1000, 10000, 100000 (число запусков 100):
# 0.006850899999999882
# 0.11891220000000002
# 1.7449849
# 21.8952981
# 286.55512839999994
#
# При каждом увеличении числа элементов массива в 10 раз время увеличивается в :
# 17,35716475 - 1.736
# 14,67456577 - 1.467
# 12,54755735 - 1.255
# 13,08751893 - 1.309

# то есть коеф-т увеличения времени уменьшается с ростом числа элементов массива,
# то есть, можно резюмировать, что метод сортировки слиянием особенно эффективен на больших массивах данных.
