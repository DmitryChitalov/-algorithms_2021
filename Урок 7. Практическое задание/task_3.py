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

"""
import random
from statistics import median
from timeit import timeit

m = int(input('Введите количество элементов '))
my_lst = [random.randint(1, 100) for i in range(2 * m + 1)]
copy_lst = my_lst[:]
print('Исходный список ', my_lst[:])


# СОРТИРОВКА ШЕЛЛА
def shell(data):
    inc = len(data) // 2
    while inc:
        for i, el in enumerate(data):
            while i >= inc and data[i - inc] > el:
                data[i] = data[i - inc]
                i -= inc
            data[i] = el
        inc = 1 if inc == 2 else int(inc * 5.0 / 11)
    return data


# БЕЗ СОРТИРОВКИ

def without_sort(_data: list) -> list:
    center = len(_data) // 2
    for i in range(center):
        _data.remove(max(_data))
    return max(_data)


new_lst = shell(my_lst[:])
print('Отсортированный список методом Шелла', new_lst[:])
print('Время сортировки Шелла составило: ',
      timeit(
          "shell(my_lst[:])",
          globals=globals(),
          number=1000))

print('Время функции без сортировки составило: ',
      timeit(
          "without_sort(my_lst[:])",
          globals=globals(),
          number=1000))

my_median = new_lst[m]
print('Найденная медиана списка с помощью сортировки Шелла равна ', my_median)
print('Найденная медиана списка без помощи сортировки',
      without_sort(my_lst[:]))
print('Медиана, найденная встроенной функцией равна ', median(my_lst[:]))
