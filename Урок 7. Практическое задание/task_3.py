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
import random
from statistics import median


def gnome(data):
    i = 1
    size = len(data)
    while i < size:
        if data[i - 1] <= data[i]:
            i += 1
        else:
            data[i - 1], data[i] = data[i], data[i - 1]
            if i > 1:
                i -= 1
    return data


def find_median_var1(some_list):
    lst = some_list[:]
    for i in range(len(some_list)//2):
        lst.remove(max(lst))
    return max(lst)


def find_median_var2(some_list):
    lst = gnome(some_list[:])
    return lst[len(lst) // 2]  # можно передавать сюда переменную num, чтоб сэкономить память


# num = int(input('Введите натуральное число: '))
num = 3
my_list = [random.randint(0, 50) for _ in range(2 * num + 1)]
print('Исходный массив:', my_list)

print('Первая реализация:', find_median_var1(my_list))
print('Вторая реализация, с гномьей сортировкой:', find_median_var2(my_list))

print('Для проверки найдем медиану встроенной функцией:', median(my_list))
