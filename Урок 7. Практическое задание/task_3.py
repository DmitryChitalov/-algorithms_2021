from random import randint
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


def find_median(lst):
    left_hand = []
    right_hand = []
    for elems in lst:
        median = elems
        for elements in lst:
            if (elements < median) and (elements != median):
                left_hand.append(elements)
            elif (elements > median) and (elements != median):
                right_hand.append(elements)
        if len(left_hand) == len(right_hand):
            return median
        left_hand.clear()
        right_hand.clear()


my_lst = [randint(-100, 100) for x in range(5)]
print(my_lst)
print(find_median(my_lst))