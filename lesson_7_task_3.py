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

my_list = list(map(int, input('Введите через запятую список чисел для поиска медианы: ').split(',')))


def find_median(list_obj):
    n = len(list_obj) // 2
    while n != 0:
        list_obj.pop(list_obj.index(max(list_obj)))
        n -= 1
    return max(list_obj)


new_list = sorted(my_list)  # для проверки median
print(f'Медиана, найденная c использованием find_median: {find_median(my_list)}.')
print(f'Медиана, найденная c использованием median: {median(new_list)}.')
