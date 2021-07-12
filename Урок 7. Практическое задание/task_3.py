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
m = int(input('Введите значение m = '))

from random import randint

lst = [randint(0, 100) for x in range(m * 2 + 1)]
print(f'Исходный массив - {lst}')


def shell_sort(lst_obj):
    gap = len(lst_obj) // 2
    while gap > 0:
        for i in range(gap, len(lst_obj)):
            temp = lst_obj[i]
            j = i
            while j >= gap and lst_obj[j - gap] > temp:
                lst_obj[j] = lst_obj[j - gap]
                j = j - gap
            lst_obj[j] = temp
        gap = gap // 2
    return lst_obj


print(f'Отсортированный - {shell_sort(lst.copy())}')
print(f'Медиана - {shell_sort(lst.copy())[m]}')
