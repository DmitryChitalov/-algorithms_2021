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
from random import triangular
from timeit import default_timer, repeat


def get_usr_lst():
    usr_num = int(input('Введите число элементов: '))  # I believe in the user
    return [triangular(0, 50) for _ in range(int(usr_num))]


def merge(left_lst, right_lst):
    """ Слияние двух списков """
    sorted_lst = [0]*(len(left_lst) + len(right_lst))
    i = k = n = 0

    while i < len(left_lst) and k < len(right_lst):
        if left_lst[i] <= right_lst[k]:
            sorted_lst[n] = left_lst[i]
            i += 1
        else:  # left_lst[i] > right_lst[k]
            sorted_lst[n] = right_lst[k]
            k += 1
        n += 1

    while i < len(left_lst):  # One of them will be empty, so only one cycle will be used
        sorted_lst[n] = left_lst[i]
        i += 1
        n += 1

    while k < len(right_lst):
        sorted_lst[n] = right_lst[k]
        k += 1
        n += 1

    return sorted_lst


def merge_sort(lst_obj):
    if len(lst_obj) <= 1:
        return lst_obj

    mid = len(lst_obj) // 2
    left_part = merge_sort(lst_obj[:mid])
    right_part = merge_sort(lst_obj[mid:])

    return merge(left_part, right_part)


def hoar_sort(lst_obj):
    if len(lst_obj) <= 1:
        return
    barrier = lst_obj[0]
    left_part = []
    right_part = []
    medium_part = []

    for el in lst_obj:
        if el < barrier:
            left_part.append(el)
        elif el > barrier:
            right_part.append(el)
        else:
            medium_part.append(el)

    hoar_sort(left_part)
    hoar_sort(right_part)
    k = 0
    for x in left_part + medium_part + right_part:
        lst_obj[k] = x
        k += 1
    return lst_obj


orig_list = get_usr_lst()
print(orig_list)
print(merge_sort(orig_list[:]))
print(hoar_sort(orig_list[:]))


def new_lists():
    orig_list1 = [triangular(0, 50) for _ in range(10)]
    orig_list2 = [triangular(0, 50) for _ in range(100)]
    orig_list3 = [triangular(0, 50) for _ in range(1000)]
    orig_list4 = [triangular(0, 50) for _ in range(10000)]
    orig_list5 = [triangular(0, 50) for _ in range(100000)]

    return orig_list1, orig_list2, orig_list3, orig_list4, orig_list5


explore_functions = ['merge_sort', 'hoar_sort']

for test_number in range(1, 3):
    print(f'\nТест {test_number}', end='\n\n')
    explore_lists = new_lists()

    for function in explore_functions:
        print(f'Функция {function}')

        for explore_list in explore_lists:
            time_sec = min(repeat(
                f'{function}({explore_list[:]})', globals=globals(), timer=default_timer, repeat=3, number=1))

            print(f'Список длинной: {len(explore_list)}, best time for sorting: {round(time_sec, 4)} sec')
        print('')


# Тест 1

# Функция merge_sort                                          Функция hoar_sort
# Список длинной: 10, best time for sorting: 0.0 sec          Список длинной: 10, best time for sorting: 0.0 sec
# Список длинной: 100, best time for sorting: 0.0008 sec      Список длинной: 100, best time for sorting: 0.0005 sec
# Список длинной: 1000, best time for sorting: 0.01 sec       Список длинной: 1000, best time for sorting: 0.0068 sec
# Список длинной: 10000, best time for sorting: 0.1278 sec    Список длинной: 10000, best time for sorting: 0.094 sec
# Список длинной: 100000, best time for sorting: 1.5362 sec   Список длинной: 100000, best time for sorting: 1.2497 sec

# Тест 2

# Функция merge_sort                                         Функция hoar_sort
# Список длинной: 10, best time for sorting: 0.0 sec         Список длинной: 10, best time for sorting: 0.0 sec
# Список длинной: 100, best time for sorting: 0.0007 sec     Список длинной: 100, best time for sorting: 0.0006 sec
# Список длинной: 1000, best time for sorting: 0.0101 sec    Список длинной: 1000, best time for sorting: 0.0092 sec
# Список длинной: 10000, best time for sorting: 0.1248 sec   Список длинной: 10000, best time for sorting: 0.0928 sec
# Список длинной: 100000, best time for sorting: 1.5824 sec  Список длинной: 100000, best time for sorting: 1.1782 sec


# В данной задаче реализовано две реккурентные сортировки: сортировка слиянием и быстрая сортировка Тони Хоара.
# Барьерный элемент для быстрой сортировки был выбран первым по счёту, т.к. известно, что список неотсортирован.
# Если есть вероятность, что список может быть отсортирован полностью или отчасти, то лучше выбирать рандомный элемент,
# т.к. сложность алгоритма будет стремиться к квадратичной.
# При одинаковой сложности этих двух алгоритмов N*logN сортировка Тони Хоара оказалась быстрее.
