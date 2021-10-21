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

# Через сортировку (Гномья)

def gnome(arr,i = 1):
    while i < len(arr):
        if arr[i - 1] <= arr[i]:
            i += 1
        else:
            arr[i - 1], arr[i] = arr[i], arr[i - 1]
            if i > 1:
                i -= 1
    return arr

def sort_med(arr):
    arr = gnome(arr)
    return arr[m]
    # если бы массив был четным:
    # if len(arr) % 2 == 1:
    #     return arr[len(arr) // 2]
    # else:
    #     return 0.5 * (arr[len(arr) // 2 - 1] + arr[len(arr) // 2])

# Без сортировки

def quickselect_median(arr, pivot_fn=random.choice):
    return quickselect(arr, m, pivot_fn)
    # if len(l) % 2 == 1:
    #     return quickselect(l, len(l) / 2, pivot_fn)
    # else:
    #     return 0.5 * (quickselect(l, len(l) / 2 - 1, pivot_fn) +
    #                   quickselect(l, len(l) / 2, pivot_fn))


def quickselect(arr, k, pivot_fn):

    pivot = pivot_fn(arr)

    lows = [el for el in arr if el < pivot]
    highs = [el for el in arr if el > pivot]
    pivots = [el for el in arr if el == pivot]

    if k < len(lows):
        return quickselect(lows, k, pivot_fn)
    elif k < len(lows) + len(pivots):
        return pivots[0]
    else:
        return quickselect(highs, k - len(lows) - len(pivots), pivot_fn)

m = int(input('Введите число median (m):'))
ln_arr = 2 * m + 1
print(ln_arr)
sim_arr = [random.randint(-100, 100) for _ in range(ln_arr)]
print(sim_arr)
print(sorted(sim_arr))
print(sort_med(sim_arr))
print(quickselect_median(sim_arr))