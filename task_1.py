"""
Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100]. Выведите на экран
исходный и отсортированный массивы.
"""
import timeit
import random


def bubble_sort_1(lst_obj):
    # сортировка в обратном порядке
    n = len(lst_obj)
    while n > 0:
        for i in range(len(lst_obj)-1, 0, -1):
            if lst_obj[i-1] > lst_obj[i]:
                lst_obj[i-1], lst_obj[i] = lst_obj[i], lst_obj[i-1]
        n -= 1
    return lst_obj


def bubble_sort_2(lst_obj):
    """
    Доработка № 1: если за проход по списку не совершается ни одной сортировки,
    то завершение. Для этого создаем флаг, который говорит нам - отсортирован
    список или нет.
    :param lst_obj:
    :return: sorted list_obj
    """
    n = len(lst_obj)
    while n > 0:
        is_sorted = True
        for i in range(len(lst_obj)-1, 0, -1):
            if lst_obj[i-1] > lst_obj[i]:
                lst_obj[i-1], lst_obj[i] = lst_obj[i], lst_obj[i-1]
                is_sorted = False
        if is_sorted:
            break
        n -= 1
    return lst_obj


def bubble_sort_3(lst_obj):
    """
    Доработка № 2: Уменьшение числа итераций.
    :param lst_obj:
    :return: sorted list_obj
    """
    n = 0
    while n < len(lst_obj):
        is_sorted = True
        for i in range(len(lst_obj) - 1, n, -1):
            if lst_obj[i - 1] > lst_obj[i]:
                lst_obj[i - 1], lst_obj[i] = lst_obj[i], lst_obj[i - 1]
                is_sorted = False
        if is_sorted:
            break
        n += 1
    return lst_obj


def my_print(*args):
    print('=-' * 50)
    print(f'Кол-во элементов: {len(args[0])}\nИсходный список:\n{args[0]}')
    print(f'Отсортированный список:\n{args[1]}')


orig_list_10 = [random.randint(-100, 100) for _ in range(10)]
orig_list_100 = [random.randint(-100, 100) for _ in range(100)]
orig_list_1000 = [random.randint(-100, 100) for _ in range(1000)]

# замеры 10
sorted_list_10 = bubble_sort_3(orig_list_10[:])
my_print(orig_list_10, sorted_list_10)

print(f'Сортировка функцией №1:'
      f'{timeit.timeit("bubble_sort_1(orig_list_10[:])",globals=globals(),number=1000)}')
print(f'Сортировка функцией №2:'
      f'{timeit.timeit("bubble_sort_2(orig_list_10[:])",globals=globals(),number=1000)}')
print(f'Сортировка функцией №3:'
      f'{timeit.timeit("bubble_sort_3(orig_list_10[:])",globals=globals(),number=1000)}')

# замеры 100
sorted_list_100 = bubble_sort_3(orig_list_100[:])
my_print(orig_list_100, sorted_list_100)

print(f'Сортировка функцией №1:'
      f'{timeit.timeit("bubble_sort_1(orig_list_100[:])",globals=globals(),number=1000)}')
print(f'Сортировка функцией №2:'
      f'{timeit.timeit("bubble_sort_2(orig_list_100[:])",globals=globals(),number=1000)}')
print(f'Сортировка функцией №3:'
      f'{timeit.timeit("bubble_sort_3(orig_list_100[:])",globals=globals(),number=1000)}')

# замеры 1000
sorted_list_1000 = bubble_sort_3(orig_list_1000[:])
my_print(orig_list_1000, sorted_list_1000)

print(f'Сортировка функцией №1:'
      f'{timeit.timeit("bubble_sort_1(orig_list_1000[:])",globals=globals(),number=1000)}')
print(f'Сортировка функцией №2:'
      f'{timeit.timeit("bubble_sort_2(orig_list_1000[:])",globals=globals(),number=1000)}')
print(f'Сортировка функцией №3:'
      f'{timeit.timeit("bubble_sort_3(orig_list_1000[:])",globals=globals(),number=1000)}')


"""
10 элементов
Сортировка функцией №1: 0.019692100000000004 / 0.013538100000000011
Сортировка функцией №2: 0.0160261            / 0.012060100000000004
Сортировка функцией №3: 0.009984500000000007 / 0.007888299999999987

100 элементов
Сортировка функцией №1: 0.9579902            / 0.8887467
Сортировка функцией №2: 0.8143288            / 0.8037537
Сортировка функцией №3: 0.5771211999999999   / 0.617829

1000 элементов
Сортировка функцией №1: 109.8006263          / 105.52803630000001
Сортировка функцией №2: 107.39068680000001   / 98.12128570000002
Сортировка функцией №3: 74.58644069999997    / 68.45603840000001

Вывод.
Доработка № 1 полезная в двух случаях:
 - если каким-то случайным образом список уже отсортирован.
    Чтобы проверить это я передал на вход функции № 2 отсортированный список из 1000 элементов.
    исходная функция: 109.03988070000001
    доработанная:     0.07123419999999925
 - если элементы при сортировке "встают" на свои позиции раньше, чем мы закончим проход по списку.
   В некоторых случаях (в отладчике удалось посмотреть) проход прекращается при n = 4 на десяти элементах.
Т.о. добиться ускорения можно, но результат - 2%.

Доработка № 3 даёт ощутимый прирост скорости - 25-30%
"""
