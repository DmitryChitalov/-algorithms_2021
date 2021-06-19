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

def median_wo_sort(cur_lst):
    mid = len(cur_lst) // 2
    while True:
        max = cur_lst[0]
        for el in cur_lst:
            if el > max:
                max = el
        cur_lst.remove(max)
        if mid == 0:
            return max
        mid -= 1

num = int(input('Введите число элементов: '))
orig_list = [random.randint(0, 10) for _ in range(2*num+1)]
print(orig_list)
print('Медиана:', median_wo_sort(orig_list[:]))