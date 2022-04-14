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
from random import randint
print('Прогламма для поиска медианы в массиве размером  2m + 1')
m = int(input('Введите число m для определения длины списка: '))
user_list = []
for i in range(0, 2 * m + 1):
    user_list.append(randint(1, 1000000))  # для простоты ограничила верхний предел 1000000, можно указать доугое число


def find_median(list_obj):
    n = len(list_obj) // 2
    while n != 0:
        list_obj.pop(list_obj.index(max(list_obj)))
        n -= 1
    return max(list_obj)


new_list = sorted(user_list)  # для проверки
median_index = len(user_list) // 2  # для проверки
print(f'Исходный список: {user_list}')
print(f'Медиана, найденная c использованием find_median: {find_median(user_list)}.')
print(f'Медиана, найденная в отсортированном списке (проверка): {new_list[median_index]}.')
