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


def median(list_obj, mid):
    list_temp = list_obj[:]
    for el in range(mid):
        list_temp.remove(max(list_temp))
    return max(list_temp)


m = int(input('Введите число: '))
test_list = [random.randint(0, 100) for _ in range(2 * m + 1)]

print(f'Сгенерированный массив: {test_list}')
print(f'Медианный элемент: {median(test_list, m)}')
print(f'Отсортированный массив: {sorted(test_list[:])}')
