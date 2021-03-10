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
import statistics
from random import randint

# Генерируем список 2m + 1
m = int(input('Введите m: '))
ls = [randint(1, 30) for i in range(2 * m + 1)]


# 1 вариант с отсортированным списком

def gnome_sort(list):
    i, size = 1, len(list)
    while i < size:
        if list[i - 1] <= list[i]:
            i += 1
        else:
            list[i - 1], list[i] = list[i], list[i - 1]
            if i > 1:
                i -= 1
    return f'{list = }\nmediana = {list[m]}'


print(f'Исходный список = {ls}\n')

print(f'Вариант с отсортированным списком (гномья)')
print(gnome_sort(ls))
print()
print(f'Вариант со statistics.median')
print(f'{statistics.median(ls) = }')



