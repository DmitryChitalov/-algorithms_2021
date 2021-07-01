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
import timeit
import random
from statistics import median

lst = [random.randint(1, 100) for _ in range(2 * (int(input('Введите длину массива: '))) + 1)]
lst2 = list(lst[:])


def shell_sort(lst):
    gap = len(lst) // 2

    while gap > 0:
        for value in range(gap, len(lst)):
            current_value = lst[value]
            position = value

            while position >= gap and lst[position - gap] > current_value:
                lst[position] = lst[position - gap]
                position -= gap
                lst[position] = current_value

        gap //= 2
    return lst


lst = shell_sort(lst)


def median_lst(list_obj):
    n = len(list_obj) // 2
    while n != 0:
        list_obj.pop(list_obj.index(max(list_obj)))
        n -= 1
    return max(list_obj)


print('Медиан равен ', median_lst(lst))
print('Проверка функцией', median(lst2))
print('Время Шелла ',
      timeit.timeit(
          "shell_sort(lst[:])",
          globals=globals(),
          number=1000))
