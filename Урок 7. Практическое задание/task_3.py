"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные по длине части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы.

Задачу можно решить без сортировки исходного массива.

Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках: Шелла, Гномья, Кучей...

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
from random import randint
from statistics import median


# Без сортировки
def median_from_cycle(lst):
    for i in range(int((len(lst) - 1) / 2)):
        lst.pop(lst.index(min(lst)))
        lst.pop(lst.index(max(lst)))

    return lst[0]


# Сортировка кучей
def heap_sort(lst):
    for start in range(int((len(lst) - 1) / 2), -1, -1):
        heap_sift(lst, start, len(lst) - 1)

    for end in range(len(lst) - 1, 0, -1):
        lst[end], lst[0] = lst[0], lst[end]
        heap_sift(lst, 0, end - 1)

    return lst


def heap_sift(lst, start, end):
    root = start

    while True:

        child = root * 2 + 1
        if child > end:
            break

        if child + 1 <= end and lst[child] < lst[child + 1]:
            child += 1

        if lst[root] < lst[child]:
            lst[root], lst[child] = lst[child], lst[root]
            root = child
        else:
            break


# Медиана после сортировки кучей
def median_from_heap(lst):
    median_idx = int((len(heap_sort(lst)) - 1) / 2)
    return lst[median_idx]


m = 2

arr = [randint(1, 10) for _ in range(2 * m + 1)]

print(f'        Сгенерированный массив:     {arr}')
print(f'        Отсортированный массив:     {heap_sort(arr[:])}')
print(f'       Контроль через median():     {median(arr[:])}')
print(f'        Медиана без сортировки:     {median_from_cycle(arr[:])}')
print(f'Медиана после сортировки кучей:     {median_from_heap(arr[:])}')
