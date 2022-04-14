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
from timeit import timeit


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
    # print(f'quick_sort: {timeit("quick_sort(test_list)", globals=globals(), number=10000)}')
    print(f'sorted: {timeit("sorted(test_list)", globals=globals(), number=10000)}')
    print(f'Медиана: {quick_sort(test_list)[m]}')
"""
Без сортировки решить задачу не получилось.
Провел сравнения сортировки по Хоару и встроенной функции sorted.
Замеры делались отдельно.
Встроенная функция sorted значительно быстрее (т.к. "под капотом" у нее
более быстрый C++)


Введите число "m": 100
quick_sort: 3.885599599999999
sorted: 0.07710120000000131
Медиана: 2
"""
