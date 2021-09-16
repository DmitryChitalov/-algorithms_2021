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
from numpy import median
import random
import time
import memory_profiler
#
# m = int(input('Введите значение: '))
#
# random_list = [random.randint(0, 10) for i in range(2 * m + 1)]
# print(random_list)
# lst_max = []
# lst_min = []
# main = random_list.pop(m)
# print(random_list)
# print(main)
#
# for el in random_list:
#     if el > main:
#         lst_max.append(el)
#     elif el <= main:
#         lst_min.append(el)
#
# lst_min.append(main)
# print(lst_min + lst_max)


def time_count_and_memory(callback):
    def wrapper(*object_):
        start_in = time.perf_counter()
        callback(*object_)
        end_in = time.perf_counter() - start_in
        print(f'{end_in:.10f}')
        m1 = memory_profiler.memory_usage()
        m2 = memory_profiler.memory_usage()
        mem_diff = m2[0] - m1[0]
        print(mem_diff)
        return object_, mem_diff
    return wrapper


m = int(input('Введите значение: '))
random_list = [random.randint(0, 10) for i in range(2 * m + 1)]
print(random_list)


@time_count_and_memory
def without_sort(random_list_):
    lst_max = []
    lst_min = []
    main = round(median(random_list_))
    random_list_.remove(main)
    for el in random_list_:
        if el > main:
            lst_max.append(el)
        elif el <= main:
            lst_min.append(el)
    lst_min.append(main)

    print(lst_min + lst_max, main)


without_sort(random_list.copy())


@time_count_and_memory
def without_sort(random_list_):
    print(sorted(random_list_), sorted(random_list_)[m])


without_sort(random_list.copy())


# Как видим, функция sorted() намного лучше по времени и функционалу,  чем собственно-написанная функция.