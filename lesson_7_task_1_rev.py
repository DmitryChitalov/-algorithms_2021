"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы.
Сортировка должна быть реализована в виде функции.
Обязательно доработайте алгоритм (сделайте его умнее).
Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение. Обязательно сделайте замеры времени обеих реализаций
и обосновать дала ли оптимизация эффективность
Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию.
Сделайте выводы!!!
Опишите в чем была ваша доработка и помогла ли вам доработка??
"""
import timeit
from random import randint


def bubble_sort_vise_versa(rand_list):
    n = 1
    while n < len(rand_list):
        for i in range(len(rand_list) - n):
            if rand_list[i] < rand_list[i + 1]:
                rand_list[i], rand_list[i + 1] = rand_list[i + 1], rand_list[i]
        n += 1
    return rand_list


#  вариант с флагом на замены

def bubble_sort_vv_flag(rand_list):
    n = 1
    replacement = True
    while n < len(rand_list) and replacement:
        replacement = False
        for i in range(len(rand_list) - n):
            if rand_list[i] < rand_list[i + 1]:
                rand_list[i], rand_list[i + 1] = rand_list[i + 1], rand_list[i]
                replacement = True
        n += 1
    return rand_list


#  вариант с уменьшением длин строки
def bubble_sort_vv_len(rand_list):
    n = 1
    len_list = len(rand_list)
    while n < len_list:
        for i in range(len_list - n):
            if rand_list[i] < rand_list[i + 1]:
                rand_list[i], rand_list[i + 1] = rand_list[i + 1], rand_list[i]
        n += 1
        len_list -= 1
    return rand_list


# Замеры на 10
origin_list = [randint(-100, 100) for i in range(10)]
print('Замеры на 10:')
print(f'Исходный массив: {origin_list}.')
print(f'Отсортированный по убыванию массив: {bubble_sort_vise_versa(origin_list[:])}.')
print(f'Массив, отсортированный функцией с флагом на замены: {bubble_sort_vv_flag(origin_list[:])}.')
print(f'Массив, отсортированный функцией с уменьшением длины строки: {bubble_sort_vv_len(origin_list[:])}.')
print('Время выполнения сортировки без улучшений составляет: ',
      timeit.timeit('bubble_sort_vise_versa(origin_list[:])', number=1000, globals=globals()), '.', sep='')
print('Время выполнения сортировки с флагом на замены составляет: ',
      timeit.timeit('bubble_sort_vv_flag(origin_list[:])', number=1000, globals=globals()), '.', sep='')
print('Время выполнения сортировки с с уменьшением длины строки составляет: ',
      timeit.timeit('bubble_sort_vv_len(origin_list[:])', number=1000, globals=globals()), '.', sep='')
print('-' * 100)

# Замеры на 100
origin_list = [randint(-100, 100) for a in range(100)]
print('Замеры на 100:')
print(f'Исходный массив: {origin_list}.')
print(f'Отсортированный по убыванию массив: {bubble_sort_vise_versa(origin_list[:])}.')
print(f'Массив, отсортированный функцией с флагом на замены: {bubble_sort_vv_flag(origin_list[:])}.')
print(f'Массив, отсортированный функцией с уменьшением длины строки: {bubble_sort_vv_len(origin_list[:])}.')
print('Время выполнения сортировки без улучшений составляет: ',
      timeit.timeit('bubble_sort_vise_versa(origin_list[:])', number=1000, globals=globals()), '.', sep='')
print('Время выполнения сортировки с флагом на замены составляет: ',
      timeit.timeit('bubble_sort_vv_flag(origin_list[:])', number=1000, globals=globals()), '.', sep='')
print('Время выполнения сортировки с с уменьшением длины строки составляет: ',
      timeit.timeit('bubble_sort_vv_len(origin_list[:])', number=1000, globals=globals()), '.', sep='')
print('-' * 100)

# Замеры на 1000
origin_list = [randint(-100, 100) for n in range(1000)]
print('Замеры на 1000:')
print(f'Исходный массив: {origin_list}.')
print(f'Отсортированный по убыванию массив: {bubble_sort_vise_versa(origin_list[:])}.')
print(f'Массив, отсортированный функцией с флагом на замены: {bubble_sort_vv_flag(origin_list[:])}.')
print(f'Массив, отсортированный функцией с уменьшением длины строки: {bubble_sort_vv_len(origin_list[:])}.')
print('Время выполнения сортировки без улучшений составляет: ',
      timeit.timeit('bubble_sort_vise_versa(origin_list[:])', number=1000, globals=globals()), '.', sep='')
print('Время выполнения сортировки с флагом на замены составляет: ',
      timeit.timeit('bubble_sort_vv_flag(origin_list[:])', number=1000, globals=globals()), '.', sep='')
print('Время выполнения сортировки с с уменьшением длины строки составляет: ',
      timeit.timeit('bubble_sort_vv_len(origin_list[:])', number=1000, globals=globals()), '.', sep='')
print('-' * 100)

"""
Змеры показали, что флаг на замены нееффективен, а уменьшение длины массива приводит к сокращению времени выполнения ф-и

Результаты замеров:
Замеры на 10:
Время выполнения сортировки без улучшений составляет: 0.04982399999999999.
Время выполнения сортировки с флагом на замены составляет: 0.06756030000000002.
Время выполнения сортировки с с уменьшением длины строки составляет: 0.03717029999999999.
----------------------------------------------------------------------------------------------------
Замеры на 100:
Время выполнения сортировки без улучшений составляет: 2.8139556000000003.
Время выполнения сортировки с флагом на замены составляет: 2.6828318.
Время выполнения сортировки с с уменьшением длины строки составляет: 1.5093569999999996.
----------------------------------------------------------------------------------------------------
Замеры на 1000:
Время выполнения сортировки без улучшений составляет: 286.52102149999996.
Время выполнения сортировки с флагом на замены составляет: 307.1394685.
Время выполнения сортировки с с уменьшением длины строки составляет: 173.72171379999997.
"""