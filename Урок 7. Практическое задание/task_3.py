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


from statistics import median
import random

number_of_el = input('Введите количество элементов: ')
while not number_of_el.isdigit() or not int(number_of_el):
    number_of_el = input('Ошибка! Должно быть введено натуральное число.\n Повторите ввод количества элементов: ')
m = int(number_of_el) * 2 + 1
my_list = [random.randint(0, m * 50) for _ in range(m)]
copy_list = my_list[:]
print('Исходный массив:', my_list)


median(copy_list)


def median_1(lst):
    quotient, remainder = divmod(len(lst), 2)
    if remainder:
        return sorted(lst)[quotient]
    return sum(sorted(lst)[quotient - 1:quotient + 1]) / 2


def median_2(lst):
    sort_lst = sorted(lst)
    len_lst = len(lst)
    index = (len_lst - 1) // 2
    if len_lst % 2:
        return sort_lst[index]
    else:
        return (sort_lst[index] + sort_lst[index + 1]) / 2.0


def median_3(lst):
    lst.sort()
    mid = len(lst) // 2
    return (lst[mid] + lst[~mid]) / 2


print(f"Медиана: {median_1(copy_list)}")
print(f"Медиана: {median_2(copy_list)}")
print(f"Медиана: {median_3(copy_list)}")