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


MIN_NUMBER = 1
MAX_NUMBER = 9

def gnome_sort(lst):
    """
    Гномья сортировка
    :param lst: несортированный список
    :return: отсортированный список
    """
    i = 1
    size = len(lst)
    while i < size:
        if lst[i - 1] <= lst[i]:
            i += 1
        else:
            lst[i - 1],lst[i] = lst[i],lst[i - 1]
            if i > 1:
                i -= 1
    return lst

def shell_sort(lst):
    """
    Сортировка методом Шелла
    :param lst: несортированный список
    :return: отсортированный список
    """
    inc = len(lst) // 2
    while inc:
        for i, el in enumerate(lst):
            while i >= inc and lst[i - inc] > el:
                lst[i] = lst[i - inc]
                i -= inc
            lst[i] = el
        inc = 1 if inc == 2 else int(inc * 5.0 / 11)
    return lst

m = int(input("Введите m: "))
user_list = [randint(MIN_NUMBER, MAX_NUMBER) for _ in range(2 * m + 1)]

gnome_user_list = gnome_sort(user_list[:])
shell_user_list = shell_sort(user_list[:])

print(f'Исходный список: {user_list}')
print(f'Гномья сортировка: {gnome_user_list}')
print(f'Гномья медиана: {gnome_user_list[m]}')
print(f'Сортировка Шелла: {shell_user_list}')
print(f'Медиана Шелла: {shell_user_list[m]}')
