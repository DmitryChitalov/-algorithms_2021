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
from statistics import median


# 1
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


n = (random.randint(0, 100) * 2) + 1
lst_1 = [random.randint(0, 100) for _ in range(n)]
lst_1_new = shell(lst_1[:])
print("Old:", lst_1, "New:", lst_1_new, sep="\n")
m = (len(lst_1_new) - 1) // 2
print("Элемент медианы:", lst_1_new[m], "медиана на позиции(по индекусу):",m)
# 2
lst_2 = lst_1[:]
for i in range((len(lst_2[:]) - 1) // 2):
    del lst_2[lst_2.index(max(lst_2))]
print("Медиана:", max(lst_2))


# 3
def median_1(lst):
    left = []
    right = []
    for i in range(len(lst)):
        for j in range(len(lst)):
            if lst[j] <= lst[i]:
                left.append(lst[j])
            if lst[j] >= lst[i]:
                right.append(lst[j])
        if len(left) == len(right):
            return f"индекс(списка без сартировки) : {i} медиана: {lst[i]}"
        if len(lst) - 1 == i:
            return left, right, i, lst[i] # иногда выскакивает не находя медиану
        left.clear()
        right.clear()
"""Ошибку не удалось мне найти"""

print(median_1(lst_1))

print("Проверка:", median(lst_1))
