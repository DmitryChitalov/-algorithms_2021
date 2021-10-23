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


#Методом оптимизированной гномьей сортировки
def search_median_with_sort(lst):
    i, j, size = 1, 2, len(lst)
    while i < size:
        if lst[i - 1] <= lst[i]:
            i, j = j, j + 1
        else:
            lst[i - 1], lst[i] = lst[i], lst[i - 1]
            i -= 1
            if i == 0:
                i, j = j, j + 1
    return lst[len(lst)//2]

def search_median_without_sort(lst):
    for i in range(len(lst)//2):
        lst.pop(lst.index(max(lst)))
    return max(lst)

m = int(input('Введите значение m для построения массива:'))
lst = [random.randint(0, 100) for _ in range(2 * m + 1)]

print(lst)
print(f'Медиана массива: {search_median_with_sort(lst)}')
print(f'Медиана массива: {search_median_without_sort(lst)}')


