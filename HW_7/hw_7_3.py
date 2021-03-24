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
from timeit import timeit
import random


def median_func(lst_obj):
    for i in range(len(lst_obj) // 2):
        lst_obj.remove(max(lst_obj))
    return max(lst_obj)


orig_list = [random.randint(0, 100) for _ in range(100)]
print(orig_list)
my_median = median_func(orig_list[:])
in_median = median(orig_list)
print('Моя функция', timeit('median_func(orig_list[:])', globals=globals(), number=1000))
print(my_median)
print('Встроеная функций', timeit('median(orig_list)', globals=globals(), number=1000))
print(in_median)

'''
моя функция: 0.36155940000000003
встроенная функция: 0.010583200000000015 
встроенная функция работает в разы быстрее 
'''

