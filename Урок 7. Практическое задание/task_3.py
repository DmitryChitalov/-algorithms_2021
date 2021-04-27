"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные по длине части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы.

Задачу можно решить без сортировки исходного
массива.

Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках: Шелла, Гномья, Кучей...
"""
from statistics import median
from random import randint
from timeit import timeit


def without_sort(_list):
    temp = _list[:]
    for _ in range(len(_list) // 2):
        temp.remove(min(temp))
    return min(temp)


def gnome_sort(_list):
    s_list = _list[:]
    i = 1
    while i < len(s_list):
        if s_list[i - 1] <= s_list[i]:
            i += 1
        else:
            temp = s_list[i]
            s_list[i] = s_list[i - 1]
            s_list[i - 1] = temp
            i -= 1
            if i == 0:
                i = 1
    return s_list


def with_sort(_list):
    sorted_list = gnome_sort(_list)
    return sorted_list[len(sorted_list) // 2]


my_lst = [5, 3, 4, 3, 3, 3, 3]

print('statistics.median:', median(my_lst))
print('without_sort:', without_sort(my_lst))
print('with_sort:', with_sort(my_lst))
print('my_lst:', my_lst)

print('\n *** Время выполнения ***\n')

new_lst = [randint(0, 100) for _ in range(1001)]

print('statistics.median(new_lst):', median(new_lst))
print('without_sort(new_lst):', without_sort(new_lst))
print('with_sort:(new_lst)', with_sort(new_lst))

print()

print('statistics.median (11):',
      timeit(
          "median(new_lst[:11])",
          globals=globals(),
          number=100))
print('without_sort (11):',
      timeit(
          "without_sort(new_lst[:11])",
          globals=globals(),
          number=100))
print('with_sort (11):',
      timeit(
          "with_sort(new_lst[:11])",
          globals=globals(),
          number=100))

print()

print('statistics.median (101):',
      timeit(
          "median(new_lst[:101])",
          globals=globals(),
          number=100))
print('without_sort (101):',
      timeit(
          "without_sort(new_lst[:101])",
          globals=globals(),
          number=100))
print('with_sort (101):',
      timeit(
          "with_sort(new_lst[:101])",
          globals=globals(),
          number=100))

print()

print('statistics.median (1001):',
      timeit(
          "median(new_lst)",
          globals=globals(),
          number=100))
print('without_sort (1001):',
      timeit(
          "without_sort(new_lst)",
          globals=globals(),
          number=100))
print('with_sort (1001):',
      timeit(
          "with_sort(new_lst)",
          globals=globals(),
          number=100))

"""
Результаты: 

statistics.median: 3
without_sort: 3
with_sort: 3
my_lst: [5, 3, 4, 3, 3, 3, 3]

 *** Время выполнения ***

statistics.median(new_lst): 52
without_sort(new_lst): 52
with_sort:(new_lst) 52

statistics.median (11): 5.58190000000125e-05
without_sort (11): 0.00022648599999999797
with_sort (11): 0.0013820129999999875

statistics.median (101): 0.00034582499999999405
without_sort (101): 0.007646627999999989
with_sort (101): 0.09557450899999997

statistics.median (1001): 0.008497072999999966
without_sort (1001): 0.7239482599999999
with_sort (1001): 11.48872719

"""
