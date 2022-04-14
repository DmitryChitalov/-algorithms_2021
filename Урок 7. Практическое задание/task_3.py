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
import timeit

m = int(input('Введите число: '))
orig_list = [random.randint(0, 100) for _ in range(2 * m + 1)]
print(orig_list)


# 1 вариант решения гномьей сортировкой
def gnome_sort(lst):
    i, size = 1, len(lst)
    while i < size:
        if lst[i - 1] <= lst[i]:
            i += 1
        else:
            lst[i - 1], lst[i] = lst[i], lst[i - 1]
            if i > 1:
                i -= 1
    return lst


def find_median_1(arr):
    lst = gnome_sort(arr)
    return lst[m]


print(f'Медиана массива с сортировкой: {find_median_1(orig_list[:])}')

orig_list_2 = [random.randint(0, 100) for _ in range(10)]

print(f'Время выполнения с gnome_sort при 10 элементах: '
      f'{timeit.timeit("find_median_1(orig_list_2[:])", globals=globals(), number=1000)}')

orig_list_3 = [random.randint(0, 100) for _ in range(100)]

print(f'Время выполнения с gnome_sort при 100 элементах: '
      f'{timeit.timeit("find_median_1(orig_list_3[:])", globals=globals(), number=1000)}')

orig_list_4 = [random.randint(0, 100) for _ in range(1000)]

print(f'Время выполнения с gnome_sort при 1000 элементах: '
      f'{timeit.timeit("find_median_1(orig_list_4[:])", globals=globals(), number=1000)}')


# 2 вариант
def find_median_2(arr):
    [arr.remove(max(arr)) for _ in range(len(arr) // 2)]
    return max(arr)


print(f'Медиана массива без сортировки: {find_median_2(orig_list[:])}')

orig_lst_1 = [random.randint(0, 100) for _ in range(10)]

print(f'Время выполнения функции без сортировки при 10 элементах: '
      f'{timeit.timeit("find_median_2(orig_lst_1[:])", globals=globals(), number=1000)}')

orig_lst_2 = [random.randint(0, 100) for _ in range(100)]

print(f'Время выполнения функции без сортировки при 100 элементах: '
      f'{timeit.timeit("find_median_2(orig_lst_2[:])", globals=globals(), number=1000)}')

orig_lst_3 = [random.randint(0, 100) for _ in range(1000)]

print(f'Время выполнения функции без сортировки при 1000 элементах: '
      f'{timeit.timeit("find_median_2(orig_lst_3[:])", globals=globals(), number=1000)}')

'''
Время выполнения с gnome_sort при 10 элементах: 0.014635772000000102
Время выполнения с gnome_sort при 100 элементах: 0.8513317979999999
Время выполнения с gnome_sort при 1000 элементах: 97.513505038
Время выполнения функции без сортировки при 10 элементах: 0.0024269270000019105
Время выполнения функции без сортировки при 100 элементах: 0.08010415100000046
Время выполнения функции без сортировки при 1000 элементах: 7.4185698690000095
Вывод: реализация без сортировки показала более быстрые результаты, чем вариант с гномьей сортировкой. 
'''
