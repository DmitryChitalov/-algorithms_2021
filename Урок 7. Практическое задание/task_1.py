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


"""Сортировка пузырьком"""


import timeit
import random


def bubble_sort(lst_obj):
   n = 1
   while n < len(lst_obj):
      for i in range(len(lst_obj) - n):
         if lst_obj[i] < lst_obj[i + 1]:
            lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
      n += 1
   return lst_obj


def bubble_sort_opt(lst_obj):
   n = len(lst_obj)
   for j in range(n):
      k = False
      for i in range(0, n-j-1):
         if lst_obj[i] < lst_obj[i + 1]:
            lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
            k = True
      if k == False:
         return lst_obj
   return lst_obj


orig_list = [random.randint(-100, 100) for _ in range(10)]

# замеры 10_1
print(
    timeit.timeit(
        "bubble_sort(orig_list[:])",
        globals=globals(),
        number=1000))
print(f'{orig_list}\n'
      f'{bubble_sort(orig_list)}')

orig_list_2 = [random.randint(-100, 100) for _ in range(10)]

# замеры 10_2
print(
    timeit.timeit(
        "bubble_sort_opt(orig_list_2[:])",
        globals=globals(),
        number=1000))
print(f'{orig_list_2}\n'
      f'{bubble_sort_opt(orig_list_2)}')

orig_list = [random.randint(-100, 100) for _ in range(100)]

# замеры 100_1
print(
    timeit.timeit(
        "bubble_sort(orig_list[:])",
        globals=globals(),
        number=1000))
print(f'{orig_list}\n'
      f'{bubble_sort(orig_list)}')

orig_list_2 = [random.randint(-100, 100) for _ in range(100)]

# замеры 100_2
print(
    timeit.timeit(
        "bubble_sort_opt(orig_list_2[:])",
        globals=globals(),
        number=1000))
print(f'{orig_list_2}\n'
      f'{bubble_sort_opt(orig_list_2)}')

orig_list = [random.randint(-100, 100) for _ in range(1000)]

# замеры 1000_1
print(
    timeit.timeit(
        "bubble_sort(orig_list[:])",
        globals=globals(),
        number=1000))
print(f'{orig_list}\n'
      f'{bubble_sort(orig_list)}')

orig_list_2 = [random.randint(-100, 100) for _ in range(1000)]

# замеры 1000_2
print(
    timeit.timeit(
        "bubble_sort_opt(orig_list_2[:])",
        globals=globals(),
        number=1000))
print(f'{orig_list_2}\n'
      f'{bubble_sort_opt(orig_list_2)}')

"""
Аналитика:
Мои замеры без оптимизации
10
0.011055100000000005
[-41, 26, 1, -73, -19, 78, 32, 36, 60, -31]
[78, 60, 36, 32, 26, 1, -19, -31, -41, -73]
100
0.6405109999999999
1000
70.00333640000001

После оптимизации
10
0.006997200000000009
[-23, 17, -60, 79, 0, 90, 46, 69, -63, -91]
[90, 79, 69, 46, 17, 0, -23, -60, -63, -91]
100
0.5997452999999999
1000
71.6518326

На 1000 оптимизированный алгоритм стал несколько замедленнее. Но при небольших размерах массива, скорость быстрее.
"""

