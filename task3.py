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
from statistics import median
import random


m = int(input('введите длинну: '))
my_list = [random.randint(0, 10) for i in range(2 * m + 1)]
print('исходный массив ', my_list)
def gnome(my_list):
    i = 1
    length = len(my_list)
    while i < length:
        if my_list[i - 1] <= my_list[i]:
            i += 1
        else:
            my_list[i - 1], my_list[i] = my_list[i], my_list[i - 1]
            if i > 1:
                i -= 1
    return my_list


print('отсортированный массив ', gnome(my_list))
print('медиана ', my_list[len(my_list)//2])
print('проверка медианы ', median(my_list))

#медианой является позиция m в массиве