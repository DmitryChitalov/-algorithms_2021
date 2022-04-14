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
Этот параметр m вам нужно запрашивать у пользователя.

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


def shell_sort(lst):
    n = len(lst) // 2
    while n:
        for i, el in enumerate(lst):
            while i >= n and lst[i - n] > el:
                lst[i] = lst[i - n]
                i -= n
            lst[i] = el
        n = 1 if n == 2 else int(n * 5.0 / 11)
    return lst


def array_size():
    n = int(input('Введите число элементов массива: '))
    if n > 1 and n % 2 != 0:
        return n
    print('Число элементов массива должно быть нечетным и больше 0, попробуйте ещё раз')
    return array_size()


def median_array(lst):
    shell_sort(lst)
    return lst[int((len(lst) - 1) / 2)]


def median_array_without_sorting(lst):
    length = len(lst) // 2
    n = 0
    while n != length:
        lst.pop(lst.index(max(lst)))
        n += 1
    return max(lst)


array = [randint(-50, 50) for _ in range(array_size())]

number = 10000

print(f'Исходный массив: {array}')
print(f'Отсортированный массив методом Шелла: {shell_sort(array[:])}')

print(f'Медиана median_array: {median_array(array[:])}, время исполнения на {number} запусков: '
      f'{timeit("median_array(array[:])", globals=globals(), number=number)}')


print(f'Медиана median_array_without_sorting: {median_array_without_sorting(array[:])}, '
      f'время исполнения на  {number} запусков: '
      f'{timeit("median_array_without_sorting(array[:])", globals=globals(), number=number)}')


print(f'Медиана statistic.median: {median(array[:])}, время исполнения на  {number} запусков: '
      f'{timeit("median(array[:])", globals=globals(), number=number)}')

# print(array)


'''
Немного изменил, не число 'm' вводит пользователь, а длину массива (удобнее все-таки для понимания)

С сортировкой методом Шелла нахождение медианы выходит дольше всего по времени, без сортировки почти в двое быстрее,
с сортировкой на небольших массивах. 
В массивах с числом элементов больше ~147 время выравнивается. Если количество элементов увеличивать, 
то время поиска медианы увеличивается методом без сортировки по сравнению с сортировкой Шелла.
Метод median библиотеки statistic в несколько раз быстрее находит медиану, чем предложенные выше функции.




Введите число элементов массива: 1001
Медиана median_array: -1, время исполнения на  10000 запусков: 16.7469489
Медиана median_array_without_sorting: -1, время исполнения на  10000 запусков: 71.6898998
Медиана statistic.median: -1, время исполнения на  10000 запусков: 0.7926865999999961

'''
