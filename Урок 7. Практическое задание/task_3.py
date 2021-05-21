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
import random
from statistics import median


m = int(input('Введите натуральное число: '))
lst = [random.randint(0, 50) for _ in range(2 * m + 1)]
print(lst)
print(median(lst))
print('___statistics median___')


def my_median(l):
    # Шелла
    mid = len(l) // 2
    while mid > 0:
        for el in range(mid, len(l)):
            current = l[el]
            position = el
            while position >= mid and l[position - mid] > current:
                l[position] = l[position - mid]
                position -= mid
                l[position] = current
        mid //= 2
    # print(l)
    # median
    if len(l) % 2 == 1:
        return l[len(l) // 2]
    else:
        return 0.5 * (l[len(l) / 2 - 1] + l[len(l) / 2])


print(my_median(lst))
print('___my median___')