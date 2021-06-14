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
from timeit import timeit

my_list = [randint(-100, 100) for num in range(99)]


def sort_by_shell(any_list):
    center = len(any_list) // 2
    while center > 0:
        for i in range(len(any_list) - center):
            j = i
            while j >= 0 and any_list[j] > any_list[j + center]:
                any_list[j], any_list[j + center] = any_list[j + center], any_list[j]
                j -= 1
        center //= 2

    return any_list


def find_median(any_lst):
    quot, rem = divmod(len(any_lst), 2)
    if rem:
        return any_lst[quot]
    return sum(any_lst[quot - 1:quot + 1]) / 2


def median_unsorted(any_list):
    center = len(any_list) // 2
    while True:
        maximum = any_list[0]
        for num in any_list:
            if num > maximum:
                maximum = num
        any_list.remove(maximum)
        if center == 0:
            return maximum
        center -= 1


print(f'shell_sort:\n{sort_by_shell(my_list[:])}')
print(f'Медиана для списка выше: {find_median(sort_by_shell(my_list[:]))}')
print(f'Проверка через median: {median(my_list[:])}')
print(f'Медиана без сортировки: {median_unsorted(my_list[:])}')

print('Время выполнения find_median(shell_sort): ', timeit('find_median(sort_by_shell(my_list[:]))', globals=globals(),
                                                           number=10000))
print('Время выполнения statistics_median: ', timeit('median(my_list[:])', globals=globals(),
                                                     number=10000))
print('Время выполнения median_unsorted: ', timeit('median_unsorted(my_list[:])', globals=globals(),
                                                   number=10000))
"""
Время выполнения find_median(shell_sort):  1.3833398
Время выполнения statistics_median:  0.024225299999999894
Время выполнения median_unsorted:  0.8888303000000002

Вариант с сортировкой Шелла самый медленный, поиск медианы без сортировки на втором месте т.к. "сортирует" только 
половину списка, встроенная функция вне конкуренции.
"""