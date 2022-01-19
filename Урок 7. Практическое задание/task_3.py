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


def quick_sort(lst):
    """Быстрая сортировка Хоара"""
    if len(lst) > 1:
        x = lst[random.randint(0, len(lst) - 1)]
        low = [el for el in lst if el < x]
        equal = [el for el in lst if el == x]
        hi = [el for el in lst if el > x]
        lst = quick_sort(low) + equal + quick_sort(hi)

    return lst


if __name__ == '__main__':
    m = int(input('Введите число "m": '))
    test_list = [random.randint(-100, 100) for _ in range(2 * m + 1)]
    result = quick_sort(test_list)
    print(f'Sorted list: {result}, median: {result[m]}')

"""
Введите число "m": 5
Sorted list: [-82, -45, -37, -35, -35, -25, 6, 8, 15, 71, 74], median: -25
"""
