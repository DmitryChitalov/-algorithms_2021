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
from statistics import median


def shell_sort(tagret_list):
    gap = len(tagret_list) // 2
    while gap > 0:
        for i in range(gap, len(tagret_list)):
            temp = tagret_list[i]
            j = i
            while j >= gap and tagret_list[j - gap] > temp:
                tagret_list[j] = tagret_list[j - gap]
                j = j - gap
            tagret_list[j] = temp
        gap = gap // 2
    return tagret_list, tagret_list[m]


m = int(input(f'Введите значение m:\n'))
test_list = [randint(0, 100) for x in range(2*m + 1)]
result, m_result = shell_sort(test_list.copy())
print(f'Исходный список: {test_list}\n'
      f'Отсортированный список: {result}\n'
      f'Медиана: {m_result}\n'
      f'Проверка медианы: {median(result)}')
