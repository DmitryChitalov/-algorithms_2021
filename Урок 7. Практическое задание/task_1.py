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
from random import randint
from timeit import timeit


def bubble_sort_original(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj) - n):
            if lst_obj[i] > lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        n += 1
    return lst_obj


def bubble_sort_reverse(lst_obj):
    n = len(lst_obj)
    while n > 1:
        for i in range(len(lst_obj) - 1, len(lst_obj) - n, -1):
            if lst_obj[i] < lst_obj[i - 1]:
                lst_obj[i], lst_obj[i - 1] = lst_obj[i - 1], lst_obj[i]
        n -= 1
    return lst_obj


def bubble_sort_reverse_mod(lst_obj):
    n = len(lst_obj)
    while n > 1:
        # Модификация
        flag = 0
        for i in range(n - 1):
            if lst_obj[i] > lst_obj[i + 1]:
                flag = 1
        if flag == 0:
            break
        #############
        for i in range(len(lst_obj) - 1, len(lst_obj) - n, -1):
            if lst_obj[i] < lst_obj[i - 1]:
                lst_obj[i], lst_obj[i - 1] = lst_obj[i - 1], lst_obj[i]
        n -= 1
    return lst_obj


real_list = [randint(-100, 100) for _ in range(10)]
print(real_list)
print(f"Оригинальный пузырёк - {bubble_sort_original(real_list)}")
print(f"Обратный пузырёк -     {bubble_sort_reverse(real_list)}")

# Замеры 10
print("Замеры 10")
print(
    timeit(
        "bubble_sort_original(real_list[:])",
        globals=globals(),
        number=1000))
print(
    timeit(
        "bubble_sort_reverse(real_list[:])",
        globals=globals(),
        number=1000))
print(
    timeit(
        "bubble_sort_reverse_mod(real_list[:])",
        globals=globals(),
        number=1000))

# Замеры 100
real_list = [randint(-100, 100) for _ in range(100)]
print("Замеры 100")
print(
    timeit(
        "bubble_sort_original(real_list[:])",
        globals=globals(),
        number=1000))
print(
    timeit(
        "bubble_sort_reverse(real_list[:])",
        globals=globals(),
        number=1000))
print(
    timeit(
        "bubble_sort_reverse_mod(real_list[:])",
        globals=globals(),
        number=1000))

# Замеры 1000
real_list = [randint(-100, 100) for _ in range(1000)]
print("Замеры 1000")
print(
    timeit(
        "bubble_sort_original(real_list[:])",
        globals=globals(),
        number=1000))
print(
    timeit(
        "bubble_sort_reverse(real_list[:])",
        globals=globals(),
        number=1000))
print(
    timeit(
        "bubble_sort_reverse_mod(real_list[:])",
        globals=globals(),
        number=1000))

"""
[-39, -89, 59, 50, -15, 97, -79, 66, 40, 34]

Оригинальный пузырёк - [-89, -79, -39, -15, 34, 40, 50, 59, 66, 97]
Обратный пузырёк -     [-89, -79, -39, -15, 34, 40, 50, 59, 66, 97]

Замеры 10
0.004000300000000002
0.005170299999999999
0.0007520999999999986

Замеры 100
0.48434350000000004
0.43439890000000003
0.5239267

Замеры 1000
52.6697854
55.2565172
66.4056666

Суть доработки: Флажок, равный нулю, получает значение 1, если хоть одна перестановка произошла
после прохождения по всему циклу. Если флажок так и остался нулём, то, соответственно 
массив уже отсортирован.

Вывод: с модификацией алгоритм будет выполняться быстрее, только если массив действительно изначально 
отсортирован. В ином же случае, смысла вставлять проверку нет.

"""