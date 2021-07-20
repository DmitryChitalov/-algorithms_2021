"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные по длине части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы.

Задачу можно решить без сортировки исходного массива.

Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках: Шелла, Гномья, Кучей...

Важно: стройте массив именно по формуле 2m+1
Потому что параметр m вам пригодится при поиске медианы, когда массив будет отсортирован.
Этот парамет m вам нужно запрашивать у пользователя.

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
import statistics

def  create_array():
    """Create data"""
    return list(random.randint(0,100) for i in range(int(input('Введите число m:'))*2+1))

def quick_sort(in_lst):
    """Quick sort"""
    if len(in_lst) < 2:
        return in_lst
    less = [i for i in in_lst[1:] if i <= in_lst[0]]
    big = [i for i in in_lst[1:] if i > in_lst[0]]
    return quick_sort(less) + [in_lst[0]] + quick_sort(big)

lst = create_array()
print('Исходный массив:')
print(lst)
print('Отсортированный массив:')
print(quick_sort(lst))
print(f'Медиана:{quick_sort(lst)[len(lst)//2]}')
print(f'Медиана, посчитанная модулем statistics:{statistics.median(lst)}')
