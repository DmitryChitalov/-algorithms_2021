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

from random import random


def find_median(my_list):
    list_copy = my_list
    left = []  # список значений слева от медианы
    right = []  # список значений справа от медианы
    for i in range(len(list_copy)):  # проходим весь список
        for j in range(len(list_copy)):  # проходим весь список во вложенном цикле
            if list_copy[i] > list_copy[j]:  # если j-й элемент меньше i-го - добавляем в "левый" список
                left.append(list_copy[j])
            if list_copy[i] < list_copy[j]:  # если j-й элемент больше i-го - добавляем в "правый" список
                right.append(list_copy[j])
            if list_copy[i] == list_copy[j] and i > j:
                left.append(list_copy[j])   # если j-й элемент равен i-му и расположен раньше - добавляем в "левый" список
            if list_copy[i] == list_copy[j] and i < j:
                right.append(list_copy[j])  # если j-й элемент равен i-му и расположен раньше - добавляем в "правый" список
        if len(left) == len(right):  # когда после прохода вложенного цикла длина "левого" списка равна длине "правого"
            return list_copy[i]  # значит на позиции i - медиана
        left.clear()  # очищаем "левый" и "правый" списки для следующего прохода
        right.clear()  # по внутреннему циклу

m = 10  # длина массива - 2m + 1
my_list = [round(random() * 100, 2) for _ in range(2 * m + 1)]

print(my_list)  # выводим массив
print("Медиана: ", find_median(my_list[:]))
