"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные по длине части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы.

Задачу можно решить без сортировки исходного массива.

Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках: Шелла, Гномья, Кучей...

Важно: стройте массив именно по формуле 2m+1
Потому что параметр m вам пригодится при поиске медианы, когда массив будет отсортирован.
Этот парамет m вам нужно запрашивать у пользователя.

[5, 3, 4, 3, 3, 3, 3]

[3, 3, 3, 3, 3, 4, 5]

my_lst
new_lts

arr[m]


from statistics import median

[3, 4, 3, 3, 5, 3, 3]

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


def median_array(array: list):
    more = 0
    less = 0
    equal = 0
    for i in range(len(array)):
        for j in range(len(array)):
            if array[i] < array[j]:
                more += 1
            elif array[i] > array[j]:
                less += 1
            elif array[i] == array[j] and i != j:
                equal += 1
        if more == less or abs(more-less) <= equal:
            return array[i]
        else:
            more = 0
            less = 0
            equal = 0


def shake_sort(lst_obj: list):
    lst_len = len(lst_obj)
    reversd = True
    start = 0
    end = lst_len - 1

    while True:
        reversd = False
        for i in range(start, end):
            if lst_obj[i] > lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
                reversd = True
        if not reversd:
            break
        reversd = False
        end = end - 1
        for i in range(end - 1, start - 1, -1):
            if lst_obj[i] > lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
                reversd = True
        start = start + 1
    return lst_obj


def build_heap(lst_obj, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and lst_obj[i] < lst_obj[left]:
        largest = left

    if right < n and lst_obj[largest] < lst_obj[right]:
        largest = right

    if largest != i:
        lst_obj[i], lst_obj[largest] = lst_obj[largest], lst_obj[i]

        build_heap(lst_obj, n, largest)


def heap_sort(lst_obj):
    lst_len = len(lst_obj)

    for i in range(lst_len, -1, -1):
        build_heap(lst_obj, lst_len, i)

    for i in range(lst_len-1, 0, -1):
        lst_obj[i], lst_obj[0] = lst_obj[0], lst_obj[i]
        build_heap(lst_obj, i, 0)
    return lst_obj


m = int(input('Введите параметр m: '))
arr = [randint(0, 10) for n in range(2 * m + 1)]
print(arr)
print('Медиана по стандартному методу:', median(arr))
print('Медиана по функции:', median_array(arr))
print('Медиана по отсортированному массиву (шейкер):', shake_sort(arr[:])[m])
print('Медиана по отсортированному массиву (куча):', heap_sort(arr[:])[m])
