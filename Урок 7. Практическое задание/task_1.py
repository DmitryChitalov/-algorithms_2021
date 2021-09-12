"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы.

Сортировка должна быть реализована в виде функции.

Обязательно доработайте алгоритм (сделайте его умнее).

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение. Обязательно сделайте замеры времени обеих реализаций
и укажите дала ли оптимизация эффективность.

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию.

Сделайте выводы!!!
Опишите в чем была ваша доработка и помогла ли вам доработка??
"""

import random
import memory_profiler
from timeit import default_timer


def mem_time(func):
    def wrapper(*args, **kwargs):
        m_start = memory_profiler.memory_usage()
        t_start = default_timer()
        res = func(*args, **kwargs)
        t_stop = default_timer()
        m_stop = memory_profiler.memory_usage()
        print(f'Память: {m_stop[0] - m_start[0]} MiB, Время: {format((t_stop - t_start) * 1000000, ".1f")} мкс.')
        return res

    return wrapper


def bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        n += 1
    return lst_obj


def bubble_sort_count(lst_obj):
    n = 1
    count = 0
    while n < len(lst_obj):
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
                count += 1  # Добавил счётчик сортировки
        if count == 0:
            break
        n += 1
    return lst_obj


orig_list = [random.randint(-100, 100) for _ in range(30)]
print(orig_list)


@mem_time
def func_1():
    print(f'До доработки: \n{bubble_sort(orig_list[:])}')


@mem_time
def func_2():
    print(f'После доработки: \n{bubble_sort_count(orig_list)}')
    # Специально не писал orig_list[:], чтобы следующая функция прошлась по уже отсортированному массиву,
    # чтобы проверить доработку.


@mem_time
def func_3():
    print(f'После доработки (отсортированный): \n{bubble_sort_count(orig_list[:])}')


func_1()
func_2()
func_3()

"""
[-17, 40, 44, 10, 97, -92, -49, 1, -74, -71, -17, 49, -27, 100, 31, -66, -48, 76, 13, 82, 88, 38, -2, 98, -96, -54, -11, 29, -98, 43]
[100, 98, 97, 88, 82, 76, 49, 44, 43, 40, 38, 31, 29, 13, 10, 1, -2, -11, -17, -17, -27, -48, -49, -54, -66, -71, -74, -92, -96, -98]
До доработки: 
Память: 0.01953125 MiB, Время: 181.4 мкс.
После доработки: 
Память: 0.0 MiB, Время: 175.9 мкс.
После доработки (отсортированный): 
Память: 0.0 MiB, Время: 53.4 мкс.

Доработка даёт хороший выигрыш по времени, только если за проход по списку не совершается ни одной сортировки.
"""
