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

from statistics import median
from random import randint
from timeit import timeit


def median_max(arr):
    lst = arr
    for i in range(0, len(arr) // 2):
        lst.remove(max(lst))
    return max(lst)


def shell_sort(arr):
    inc = len(arr) // 2
    while inc:
        for i, el in enumerate(arr):
            while i >= inc and arr[i - inc] > el:
                arr[i] = arr[i - inc]
                i -= inc
            arr[i] = el
        inc = 1 if inc == 2 else int(inc * 5.0 / 11)
    return arr


def median_sort(arr):
    x = shell_sort(arr)
    return x[int((len(x) - 1) / 2)]


m1 = 5
m2 = 50
m3 = 500
list_10 = [randint(0, 1000) for _ in range(2 * m1 + 1)]
list_100 = [randint(0, 1000) for _ in range(2 * m2 + 1)]
list_1000 = [randint(0, 1000) for _ in range(2 * m3 + 1)]

print(
    timeit(
        "median(list_10[:])",
        globals=globals(),
        number=1000))
print(
    timeit(
        "median_sort(list_10[:])",
        globals=globals(),
        number=1000))
print(
    timeit(
        "median_max(list_10[:])",
        globals=globals(),
        number=1000))
print("===============================================")
print(
    timeit(
        "median(list_100[:])",
        globals=globals(),
        number=1000))
print(
    timeit(
        "median_sort(list_100[:])",
        globals=globals(),
        number=1000))
print(
    timeit(
        "median_max(list_100[:])",
        globals=globals(),
        number=1000))
print("===============================================")
print(
    timeit(
        "median(list_1000[:])",
        globals=globals(),
        number=1000))
print(
    timeit(
        "median_sort(list_1000[:])",
        globals=globals(),
        number=1000))
print(
    timeit(
        "median_max(list_1000[:])",
        globals=globals(),
        number=1000))
print("===============================================")
"""
Для нахождения медианы использовал 3 способа: встроенная функция median, отсортированный массив методом Шелла и
способом через удаление макс. элемента. При замерах на массиве в 1000 элементов результаты следующие:
0.14008559999999992 - median
5.954709200000001 - shell
13.329686899999999 - remove_max
Соответственно самая быстрая это встроенная функция, самая медленная - через удаление макс., метод с сортировкой
расположился между ними.
"""
