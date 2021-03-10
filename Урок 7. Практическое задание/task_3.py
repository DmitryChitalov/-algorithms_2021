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
'''Использование гномьей сортировки'''
from random import randint


def gnome_sort(lst, size):
    i = 1
    while i < size:
        if (lst[i - 1] <= lst[i]):
            i += 1
        else:
            tmp = lst[i]
            lst[i] = lst[i - 1]
            lst[i - 1] = tmp
            i -= 1
            if (i == 0):
                i = 1
    return lst


m = int(input("Введите целое значение m: "))
lists = [randint(0, 100) for i in range(2 * m + 1)]
print('Сгенерировано:', lists)
newlists = gnome_sort(lists, len(lists))
print('Отсортировано:', newlists)

print(f"Медиана: {newlists[m]}")
