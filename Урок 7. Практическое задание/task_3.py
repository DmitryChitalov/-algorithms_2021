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
import random


def gnome(mask):
    i = 1
    while i < len(mask):
        if mask[i - 1] <= mask[i]:
            i += 1
        else:
            mask[i - 1], mask[i] = mask[i], mask[i - 1]
            if i > 1:
                i -= 1
    return mask


n = int(input())
m = [random.randint(0, 100) for el in range(2 * n + 1)]
gnome(m)
print(m)


def gnome_sort():
    return gnome(m)[len(m) // 2]


print(gnome_sort())
