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
import random
import timeit
import copy
from statistics import median

m = int(input('Введите m: '))
lst_obj = [random.randint(0,15) for _ in range(2*m+1)]
print(f'lst_obj: {lst_obj}')

def help_shell_sort(data):
    def shell_sort(data):
        last_index = len(data) - 1
        step = len(data)//2
        while step > 0:
            for i in range(step, last_index + 1, 1):
                j = i
                delta = j - step
                while delta >= 0 and data[delta] > data[j]:
                    data[delta], data[j] = data[j], data[delta]
                    j = delta
                    delta = j - step
            step //= 2
        return data

    sort_obj = shell_sort(lst_obj[:])
    #print(f'shell sort: {sort_obj}')
    return sort_obj[m]


print(f'shell mediana = {help_shell_sort(lst_obj[:])}')



copy_lst = copy.deepcopy(lst_obj)


def my_mediana(data):
    def my_max(data):
        max = 0
        for i in range(len(data)):
            if data[i] > max:
                max = data[i]
        return max
    def my_remove(data):
        data.remove(my_max(data))
        return data
    for i in range(m):
        my_remove(data)
    return my_max(data)



print(f'моя медиана = {my_mediana(copy_lst[:])}')
print(f'медиана из модуля statistics = {median(lst_obj)}')

def stat_mediana(data):
    return median(data)



print(
    timeit.timeit(
        "help_shell_sort(lst_obj[:])",
        globals=globals(),
        number=1000))

print(
    timeit.timeit(
        "my_mediana(copy_lst[:])",
        globals=globals(),
        number=1000))

print(
    timeit.timeit(
        "stat_mediana(lst_obj[:])",
        globals=globals(),
        number=1000))

"""
Искал медиану 3 способами:
1. сортировка Шелла
2. предложенный на уроке способ с поиском максимального элемента
3. воспользовался подулем statistics

Замер 1
0.2521068999999998  shell_sort
0.24700070000000007 моя функция
0.00605840000000013 median из statistics

Замер 2
0.12767650000000064  shell_sort
0.22045159999999964  моя функция
0.004589300000000129 median из statistics

Замер 3
0.13436730000000008  shell_sort
0.19775049999999994  моя функция
0.004877299999999973 median из statistics
"""
