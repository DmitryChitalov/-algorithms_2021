"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы.

Сортировка должна быть реализована в
виде функции.

Обязательно доработайте алгоритм (сделайте его умнее)!

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение.
Обязательно сделайте замеры времени обеих реализаций
и обосновать дала ли оптимизация эффективность

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию.

Сделайте выводы!!!
Опишите в чем была ваша доработка и помогла ли вам доработка??
"""

import timeit
import random


def bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] > lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        n += 1
    return lst_obj


def bubble_sort_reverse(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        n += 1
    return lst_obj


def bubble_sort_rev_upgrade(lst_obj):
    """
    Данная функция является функцией пузырьковой сортировки по убыванию с проверкой факта выполения смены элементов
    местами на текущей итерации цикла. Если смена элементов местами не производилась, то массив отсортирован и
    функиця завершает работу.
    """
    n = 1
    was_sorting = True
    while was_sorting:
        was_sorting = False
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
                was_sorting = True
    return lst_obj


orig_list = [random.randint(-100, 100) for _ in range(10)]

# Проверка корректности работы функций:
print(f'Исходный список:\n{orig_list}')
print(f'Список, отсортированный по возрастанию:\n{bubble_sort(orig_list[:])}')
print(f'Список, отсортированный по убыванию:\n{bubble_sort_reverse(orig_list[:])}')
print(f'Список, отсортированный по убыванию (апгрейд):\n{bubble_sort_rev_upgrade(orig_list[:])}')

print('Замеры 10:')
print(
    timeit.timeit(
        "bubble_sort(orig_list[:])",
        globals=globals(),
        number=1000))

print(
    timeit.timeit(
        "bubble_sort_reverse(orig_list[:])",
        globals=globals(),
        number=1000))

print(
    timeit.timeit(
        "bubble_sort_rev_upgrade(orig_list[:])",
        globals=globals(),
        number=1000))

print('Замеры 200:')
orig_list = [random.randint(-100, 100) for _ in range(200)]

print(
    timeit.timeit(
        "bubble_sort(orig_list[:])",
        globals=globals(),
        number=1000))

print(
    timeit.timeit(
        "bubble_sort_reverse(orig_list[:])",
        globals=globals(),
        number=1000))

print(
    timeit.timeit(
        "bubble_sort_rev_upgrade(orig_list[:])",
        globals=globals(),
        number=1000))

print('Замеры 400:')
orig_list = [random.randint(-100, 100) for _ in range(400)]

print(
    timeit.timeit(
        "bubble_sort(orig_list[:])",
        globals=globals(),
        number=1000))

print(
    timeit.timeit(
        "bubble_sort_reverse(orig_list[:])",
        globals=globals(),
        number=1000))

print(
    timeit.timeit(
        "bubble_sort(orig_list[:])",
        globals=globals(),
        number=1000))

print(
    timeit.timeit(
        "bubble_sort_rev_upgrade(orig_list[:])",
        globals=globals(),
        number=1000))

print('Замеры 30 на отсортированном по убыванию списке:')
orig_list = [95, 77, 74, 67, 63, 43, 41, 36, 28, 19, 8, 2, 0, -4, -4, -15, -16, -19, -22, -35, -36, -50, -50, -61, -62,
             -62, -71, -72, -72, -90]

print(
    timeit.timeit(
        "bubble_sort(orig_list[:])",
        globals=globals(),
        number=1000))

print(
    timeit.timeit(
        "bubble_sort_reverse(orig_list[:])",
        globals=globals(),
        number=1000))

print(
    timeit.timeit(
        "bubble_sort_rev_upgrade(orig_list[:])",
        globals=globals(),
        number=1000))

"""
Замеры по 10 элементов (по возрастанию, по убыванию, по убыванию + апгрейд):
0.0093607
0.008138599999999996
0.009697999999999998

Замеры по 200 элементов (по возрастанию, по убыванию, по убыванию + апгрейд):
2.6228909000000002
2.4485235000000003
3.624482500000001

Замеры по 400 элементов (по возрастанию, по убыванию, по убыванию + апгрейд):
11.0292765
10.324614200000003
11.363427300000001 - повторный запуск функции сортировки по возрастанию для вывода №2.
16.109982600000002

Замеры по 30 элементов отсортированного списка (по возрастанию, по убыванию, по убыванию + апгрейд):
0.07477899999999948
0.0339659999999995
0.0021509999999977936

    Вывод №1 - Смысла в "улучшении" функции пузырьковой сортировки за счёт проверки факта выполнения смены элементов
местами на текущей итерации цикла я не вижу, так как чем больше элементов в исходном списке, тем меньше шанс, что этот 
список будет изначально отсортирован. В итоге такое "улучшение" функции даёт прирост времени выполнения функции
в немыслимые 1,5 раза! Но, стоит отдать должное - "улучшение" действительно работает на отсортированном списке.
    Вывод №2(побочный) - функция пузырьковой сортировки по убыванию зачастую выполняется быстрее, чем функция 
сортировки по возрастанию. Сперва думал, что связано с тем, что исходный список кэшируется в памяти и подгружается 
затем быстрее подгружается по запросу интрепретатора, но повторный запуск этой же функции сортировки по возрастанию 
показал результат хуже, чем ранее запущенной функции сортировки по убыванию. Удивительно, но факт. Судя по всему, это 
чистое совпадение.
"""
