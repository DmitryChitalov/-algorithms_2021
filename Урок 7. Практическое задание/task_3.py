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
from statistics import median


def get_data_from_user() -> list:
    while True:
        el_count = input("Список строится по формуле 2m + 1. Введите m: ")
        print(el_count)
        if el_count.isdigit():
            el_count = int(el_count)
            break
        else:
            print("Вы ввели что-то не то. Заходим на новый круг!")

    return [random.randint(0, 50) for _ in range(2 * el_count + 1)]


orig_list = get_data_from_user()
med_index = orig_list
print("Оригинальный список: ")
print(*orig_list)

print("Медиана из модуля statistics: ", median(orig_list))

# Если я правильно понял задание и мне не нужно писать руками функцию max.
for _ in range(int(len(orig_list) / 2)):
    orig_list.remove(max(orig_list))

print("Медиана полученная удалением максимальных элементов: ", max(orig_list))

