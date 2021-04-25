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
from random import randint


def shell(list_num):
    inc = len(list_num) // 2
    while inc:
        for i, el in enumerate(list_num):
            while i >= inc and list_num[i - inc] > el:
                list_num[i] = list_num[i - inc]
                i -= inc
            list_num[i] = el
        inc = 1 if inc == 2 else int(inc * 5.0 / 11)
    return list_num


m = 3
list_num = [randint(1, 50) for el in range(2 * m + 1)]
print(shell(list_num[:]))