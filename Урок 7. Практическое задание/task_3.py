"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные по длине части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы.

Задачу можно решить без сортировки исходного
массива.

Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках: Шелла, Гномья, Кучей...

[5, 3, 4, 3, 3, 3, 3]

[3, 3, 3, 3, 3, 4, 5]

my_lst
new_lts

arr[m]


from statistics import median

[3, 4, 3, 3, 5, 3, 3]


left.clear()
right.clear()


m = 3
len = 7
i
left = []
right = []

left == right and

for i in
    for
    left == right
    left.clear()
    right.clear()


"""

from timeit import timeit
from statistics import median
import random


def chek_time(f):
    return timeit(f"{f}", globals=globals(), number=10000)


def create_lst(m):
    return [random.randint(1, 100) for _ in range(2 * m + 1)]


def search_median_max(data):
    data = data[:]
    for _ in range(len(data) // 2):
        data.remove(max(data))
    return max(data)


def gnome_sort(lst, m):
    lst = lst[:]
    i = 1
    while i < len(lst):
        if lst[i - 1] <= lst[i]:
            i += 1
        else:
            tmp = lst[i]
            lst[i] = lst[i - 1]
            lst[i - 1] = tmp
            i -= 1
            if i == 0:
                i = 1
    return lst[m]


m = int(input("Введите m: "))
orig_lst = create_lst(m)
print(f"Созданный список:\n{orig_lst}")
print(f"Реализация через max: {search_median_max(orig_lst)}")
print(f"Реализация через гномью сортировку(медиана находится по индексу m): {gnome_sort(orig_lst, m)}")
print(f"Для проверки, функция median: {median(orig_lst)}")

orig_list_10 = create_lst(10)
orig_list_100 = create_lst(100)
orig_list_1000 = create_lst(1000)
print(f"Затрачено времени на поиск медианы через max. 10 элементов:"
      f"\n{chek_time('search_median_max(orig_list_10)')}")
print(f"Затрачено времени на поиск медианы через max. 100 элементов:"
      f"\n{chek_time('search_median_max(orig_list_100)')}")

print(f"Затрачено времени на поиск медианы через гномью сортировку. 10 элементов:"
      f"\n{chek_time('gnome_sort(orig_list_10[:], 10)')}")
print(f"Затрачено времени на поиск медианы через гномью сортировку. 100 элементов:"
      f"\n{chek_time('gnome_sort(orig_list_100[:], 100)')}")

print(f"Затрачено времени на поиск медианы через функцию median. 10 элементов:"
      f"\n{chek_time('median(orig_list_10[:])')}")
print(f"Затрачено времени на поиск медианы через функцию median. 100 элементов:"
      f"\n{chek_time('median(orig_list_100[:])')}")

"""
Аналитика:
Самый медленная функция с сортировкой. Так как требуется каждый раз сортировать список.
Далее идет функция с использованием max, без сортировки, за счет чего она выполняется быстрее.
Как и предполагалось, встроенная функция будет выполняться быстрее всех из оптимизированных алгоритмов выполнения.

Замеры:
Затрачено времени на поиск медианы через max. 10 элементов:
0.03590369999999998
Затрачено времени на поиск медианы через max. 100 элементов:
1.8026646999999998
Затрачено времени на поиск медианы через гномью сортировку. 10 элементов:
0.2555185
Затрачено времени на поиск медианы через гномью сортировку. 100 элементов:
22.339449799999997
Затрачено времени на поиск медианы через функцию median. 10 элементов:
0.004940900000001136
Затрачено времени на поиск медианы через функцию median. 100 элементов:
0.04562830000000062
"""
