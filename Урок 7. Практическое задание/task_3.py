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
from statistics import median

def gnom_sort(obj_lst):
    j = 0
    while j < len(obj_lst):
        if j == 0 or obj_lst[j] >= obj_lst[j - 1]:
            j += 1
        else:
            obj_lst[j], obj_lst[j - 1] = obj_lst[j - 1], obj_lst[j]
            j -= 1
    return obj_lst

def sort_median(lst_obj):
    return gnom_sort(lst_obj)[median_user]

def split_median(lst_obj):
    for el in lst_obj:
        left_m = [el2 for el2 in lst_obj if el2 < el]
        right_m = [el2 for el2 in lst_obj if el2 > el]
        if len(left_m) == len(right_m) or abs(len(left_m) - len(right_m)) < lst_obj.count(el):
            return el

def max_median(lst_obj):
    for i in range(len(lst_obj) // 2):
        lst_obj.remove(max(lst_obj))
    return max(lst_obj)

median_user = int(input("Необходимо ввести значение m: "))
obj_list = [randint(0, 1000000) for i in range(2 * median_user + 1)]
print(sort_median(obj_list))
print(median(obj_list[:]))
print(split_median(obj_list[:]))
print(max_median(obj_list[:]))
