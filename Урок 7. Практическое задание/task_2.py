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
from random import random
import timeit

"""
Прямое слияние Боуза-Нельсона - можно рассматривать как разновидность алгоритма сортировки слиянием,
хотя по сути это сортировочная сеть. Суть ее заключается в том, что все подмассивы можно сортировать параллельно
на каждом этапе. 
"""


def bose_nelson(lst):
    """
    Прямое слияние Боуза-Нельсона - можно рассматривать как разновидность алгоритма сортировки слиянием,
    хотя по сути это сортировочная сеть. Суть ее заключается в том, что все подмассивы можно сортировать параллельно
    на каждом этапе.
    Массив делится на две равноые части, затем сравниваются 1ый элемент левой части и  1ый правой части (2ой и 2о2 итд).
    Каждая группа становится отсортрованным подмассивом, затем выполняется их слияние. Далее выбираются следующие
    группы, по 2 элемент, сравниваются и сливаются. Цикл продолжается до тех пор пока размеры групп меньше размеров
    исходного массива.
    """

    def bose_nelson_merge(j, r, m):
        if j + r < len(lst):
            if m == 1:
                if lst[j] > lst[j + r]:
                    lst[j], lst[j + r] = lst[j + r], lst[j]
            else:
                m = m // 2
                bose_nelson_merge(j, r, m)
                if j + r + m < len(lst):
                    bose_nelson_merge(j + m, r, m)
                bose_nelson_merge(j + m, r - m, m)
        return lst

    m = 1
    while m < len(lst):
        j = 0
        while j + m < len(lst):
            bose_nelson_merge(j, m, m)
            j = j + m + m
        m = m + m
    return lst


def merge_sort(lst_obj):
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


orig_list = [random() * 50 for _ in range(10)]

# замеры 10
print("Замеры merge_sort на 10 элементах: ")
print(
    timeit.timeit(
        "merge_sort(orig_list[:])",
        globals=globals(),
        number=1000))

print("Замеры bose_nelson на 10 элементах: ")
print(
    timeit.timeit(
        "bose_nelson(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [random() * 50 for _ in range(100)]

# замеры 100
print("Замеры merge_sort на 100 элементах: ")
print(
    timeit.timeit(
        "merge_sort(orig_list[:])",
        globals=globals(),
        number=1000))
print("Замеры bose_nelson на 100 элементах:")

print(
    timeit.timeit(
        "bose_nelson(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [random() * 50 for _ in range(1000)]

# замеры 1000
print("Замеры merge_sort на 1000 элементах: ")
print(
    timeit.timeit(
        "merge_sort(orig_list[:])",
        globals=globals(),
        number=1000))
print("Замеры bose_nelson на 1000 элементах: ")

print(
    timeit.timeit(
        "bose_nelson(orig_list[:])",
        globals=globals(),
        number=1000))

my_lst = [random() * 50 for i in range(5)]
print(my_lst)
print(bose_nelson(my_lst[:]))
print(merge_sort(my_lst[:]))

"""
Замеры merge_sort на 10 элементах: 
0.013713800000000005
Замеры bose_nelson на 10 элементах: 
0.0177063
Замеры merge_sort на 100 элементах: 
0.21716640000000004
Замеры bose_nelson на 100 элементах:
0.7851531
Замеры merge_sort на 1000 элементах: 
3.5325358000000002
Замеры bose_nelson на 1000 элементах: 
31.9154757

Судя по замерам, Прямое слияние Боуза-Нельсона, работает довольно медленно в сравнении с классическим.
Вероятно при использовании параллельных вычислений прямое слияние Боуза-Нельсона будет более эффективно.
"""
