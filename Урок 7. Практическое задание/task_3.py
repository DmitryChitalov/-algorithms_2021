"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным
образом. Найдите в массиве медиану. Медианой называется элемент ряда, делящий
его на две равные по длине части: в одной находятся элементы, которые не меньше
 медианы, в другой – не больше медианы.

Задачу можно решить без сортировки исходного массива.

Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках: Шелла, Гномья, Кучей...

Важно: стройте массив именно по формуле 2m+1
Потому что параметр m вам пригодится при поиске медианы, когда массив будет
отсортирован.
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
from random import randint
from statistics import median


def shell_sort(lst):            # сортировка Шелла
    cm = len(lst) // 2          # conditional middle - условная середина
    while cm > 0:
        for val in range(cm, len(lst)):
            current_val = lst[val]
            position = val

            while position >= cm and lst[position - cm] > current_val:
                lst[position] = lst[position - cm]
                position -= cm
                lst[position] = current_val
        cm //= 2
    return lst


def median_without_sort(lst):
    for i in range(len(lst) // 2):
        lst.pop(lst.index(max(lst)))
    return max(lst)


m = int(input('Введите значение m для построения массива: \n'))
my_list = [randint(0, 100) for _ in range(m * 2 + 1)]
print(my_list)
print(f'Меридиана массива: {shell_sort(my_list[:])[m]}, с сортировкой Шелла')
print(f'Меридиана массива: {median_without_sort(my_list[:])}, без сортировки')
print(f'Меридиана массива: {median(my_list[:])}, проверка через функцию')
