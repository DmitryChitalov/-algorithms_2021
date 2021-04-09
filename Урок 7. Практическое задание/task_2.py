"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Хотя в примерах к уроку уже есть вариант реализации слияния, попробуйте предложить другой
(придумать или найти)

И попытаться сделать замеры на массивах разной длины: 10, 100, 1000, ...

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""

import random
from timeit import timeit
import time
import memory_profiler
from memory_profiler import profile
# from cProfile import run


def decor(func):
    def wrapper(*args, **kwargs):
        m1 = memory_profiler.memory_usage()
        t1 = time.time()
        res = func(*args, **kwargs)
        t2 = time.time()
        m2 = memory_profiler.memory_usage()
        mem_diff = m2[0] - m1[0]
        return res, mem_diff, t2-t1
    return wrapper


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

@profile
def merge_sort_mem(a):
    merge_sort(a)
    merge_sort_down_up(a)

def merge_sort_down_up(a):
    def MergerGroup(a, left, m, right):
        if left >= right: return None
        if m < left or right < m: return None
        t = left
        for j in range(m + 1, right + 1):  # подгруппа 2
            for i in range(t, j):  # цикл подгруппы 1
                if a[j] < a[i]:
                    r = a[j]
                    # итерационно переставляем элементы, чтобы упорядочить
                    for k in range(j, i, -1):
                        a[k] = a[k - 1]
                    a[i] = r
                    t = i  # проджолжение вставки в группе 1
                    break  # к следующему узлу из подгруппы 2

    if len(a) < 2: return None
    k = 1
    while k < len(a):
        g = 0
        while g < len(a):  # группы
            z = g + k + k - 1  # последний эл-т группы
            r = z if z < len(a) else len(a) - 1  # последняя группа
            MergerGroup(a, g, g + k - 1, r)  # слияние
            g += 2 * k
        k *= 2
    return a


@decor
def merge_sort_cover(a):
    return merge_sort(a)

@decor
def merge_sort_down_up_cover(a):
    return merge_sort_down_up(a)




orig_list = [random.uniform(0, 50) for _ in range(10)]
print(orig_list)
print(merge_sort(orig_list[:]))
print(merge_sort_down_up(orig_list[:]))
# exit()

list_param = [10, 100, 1000]
func_list = ['merge_sort', 'merge_sort_down_up']
max_len = len(max(func_list, key=len))

for param in list_param:
    orig_list = [random.uniform(0, 50) for _ in range(param)]
    print(f'Сравним варианты сортировки слиянием для массива из ({param}) элементов:')
    for el in func_list:
        print(f'Функция {el}:'.ljust(max_len + 10, '_'),
              timeit(el + '(orig_list[:])', setup='orig_list = [random.uniform(0, 50) for _ in range(param)]',
                     number=1000, globals=globals()))

param = 10000
orig_list = [random.uniform(0, 50) for _ in range(param)]
print(f'Сравним варианты сортировки слиянием для массива из ({param}) элементов на требования к памяти:')
res, mem_diff, time_diff = merge_sort_cover(orig_list[:])
print(f"Выполнение первого варианта (с рекурсией) заняло {mem_diff} Mib, {time_diff} времени.")
res, mem_diff, time_diff = merge_sort_down_up_cover(orig_list[:])
print(f"Выполнение второго варианта (снизу вверх - без рекурсии) заняло {mem_diff} Mib, {time_diff} времени.")

'''
Существует два основных способа реализации алгоритма сортировки слиянием:
Один из которых использует подход "сверху вниз" (merge_sort). 
Он чаще используется по причине внешней простоты и скорости выполнения.
Второй способ "восходящий" (merge_sort_down_up), работает в противоположном направлении и не содержит рекурсии.
Какждый из подходов имеет свои плюсы:
1) Рекурсионный - скорость и простота реализации.
2) "Снизу вверх" - минимальные требования к памяти.

Аналитика:
Сравним варианты сортировки слиянием для массива из (10) элементов:
Функция merge_sort:_________ 0.03241219499999992
Функция merge_sort_down_up:_ 0.03639089200000001
Сравним варианты сортировки слиянием для массива из (100) элементов:
Функция merge_sort:_________ 0.39629636999999995
Функция merge_sort_down_up:_ 0.7278625339999998
Сравним варианты сортировки слиянием для массива из (1000) элементов:
Функция merge_sort:_________ 5.4450779769999995
Функция merge_sort_down_up:_ 44.341838931
Сравним варианты сортировки слиянием для массива из (10000) элементов на требования к памяти:
Выполнение первого варианта (с рекурсией) заняло 0.06640625 Mib, 0.07105731964111328 времени.
Выполнение второго варианта (снизу вверх - без рекурсии) заняло 0.0 Mib, 3.9668374061584473 времени.

Примечание:
Замеры памяти делал отдельно от timeit ввиду серьезных тормозов из-за количества тестов.
'''