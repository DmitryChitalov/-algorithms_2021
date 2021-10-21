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


def select_med(lst, k, spot=random.choice):
    spot = spot(lst)
    low = [i for i in lst if i < spot]
    high = [i for i in lst if i > spot]
    equally = [i for i in lst if i == spot]

    if k < len(low):
        return select_med(low, k, spot=random.choice)
    elif k < len(low) + len(equally):
        return equally[0]
    else:
        return select_med(high, k - len(low) - len(equally), spot=random.choice)


user_number = int(input('Введите число: '))

some_lst = [random.randint(0, 100) for i in range(user_number * 2 + 1)]
print(some_lst)

print(select_med(some_lst, user_number))

"""
С помощью интернета решил таким образом без сортировки.
"""