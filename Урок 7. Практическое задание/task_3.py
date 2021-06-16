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
"""
Вывод: Тут вывод явно напрашивается только один, встроенная функция работает намного быстрее любой сортировки написанной
нами. В данном случае был рассмотрен метод Гномьей сортировки.
"""
from timeit import timeit
import random
from statistics import median


def gnome_sort(lst_obj):
    i = 1
    j = 2
    while i < len(lst_obj):
        if lst_obj[i - 1] <= lst_obj[i]:
            i = j
            j += 1
        else:
            lst_obj[i - 1], lst_obj[i] = lst_obj[i], lst_obj[i - 1]
            i -= 1
            if i == 0:
                i = j
                j += 1
    return lst_obj


m = int(input('Введите натуральное число: '))
orig_list = [random.randint(0, 100) for _ in range(2 * m + 1)]

print(f'Медиана Гномьей сортировки: {gnome_sort(orig_list[:])[m]}')
print(f'Поиск с помощью Гномьей сортировки: '
      f'{timeit("gnome_sort(orig_list[:])[m]", globals=globals(), number=1000)}')
print(f'Медиана из библиотеки statistics: {median(orig_list)}')
print(f'Поиск функецией из библиотеки statistics: '
      f'{timeit("median(orig_list[:])", globals=globals(), number=1000)}')

