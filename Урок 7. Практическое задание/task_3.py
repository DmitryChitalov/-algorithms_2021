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
Этот параметр m вам нужно запрашивать у пользователя.

[5, 3, 4, 3, 3, 3, 3]
[1, 8, 3, 5, 6, 9, 1]
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


"""
Использована сортировка Шелла и метод нахождения медианы без сортировки
"""


def shell_sorting(some_list):
    """Shell's sorting"""
    interval = len(some_list) // 2
    while interval:
        for i, el in enumerate(some_list):
            while i >= interval and some_list[i - interval] > el:
                some_list[i] = some_list[i - interval]
                i -= interval
            some_list[i] = el
        interval = 1 if interval == 2 else int(interval * 5.0 / 11)
    median = some_list[len(some_list)//2]
    return some_list, median


def my_centre(some_list):
    """Median without sorting"""
    half = len(some_list) // 2
    for i in range(half):
        some_list.remove(max(some_list))
    return some_list


def start():
    """Starting function"""
    print("Будет построен массив размером 2m + 1 и найдена его медиана.")
    while True:
        try:
            my_num = int(input("Введите значение m: "))
            if my_num < 1:
                raise ValueError
            break
        except ValueError:
            print('Требуется положительное целое число больше 0. Попробуйте еще раз')
    my_rand_int_list = [randint(0, 100) for i in range(2 * my_num + 1)]
    print(f"Построен неотсортированный массив {my_rand_int_list}")
    centre = max(my_centre(my_rand_int_list[:]))
    print(f"Медианой массива является число {centre}")
    my_median = shell_sorting(my_rand_int_list[:])
    print(f"Проверка: сортировка Шелла, медиана: {my_median[1]}, массив: {my_median[0]}")
    my_sorted = sorted(my_rand_int_list)
    print(f"Проверка: функция sorted, медиана: {my_sorted[my_num]}, "
          f"отсортированный массив: {my_sorted}")


start()
