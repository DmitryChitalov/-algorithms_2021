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
from timeit import timeit

# Решение с гномьей сортировкой
m = int(input('Введите число: '))
lst_obj = [random.randint(0, 100) for _ in range(0, 2 * m + 1)]
print(lst_obj)


def with_sort(lst):
    data = lst

    def gnome(data):
        i, size = 1, len(data)
        while i < size:
            if data[i - 1] <= data[i]:
                i += 1
            else:
                data[i - 1], data[i] = data[i], data[i - 1]
                if i > 1:
                    i -= 1
        return data

    gnome(data)
    return data[m]


print(with_sort(lst_obj))
print(median(lst_obj))

# Решение без сортировки исходного массива
m = int(input('Введите число: '))
lst_obj = [random.randint(0, 100) for _ in range(0, 2 * m + 1)]
print(lst_obj)


def my_median(lst):
    i = 1
    while i <= m:
        lst.remove(max(lst))
        i += 1
    return max(lst)


print(my_median(lst_obj[:]))
print(median(lst_obj))

print('С сортировкой')  # 0.796556029 Самое медленное время выполнения
print(timeit('with_sort(lst[:])', setup='lst = [random.randint(0, 100) for _ in range(0, 2 * 10 + 1)]',
             globals=globals(), number=10000))
print('Без сортировки')  # 0.04169495400000045 Среднее время выполнения, более простой и читаемый код
print(timeit('my_median(lst[:])', setup='lst = [random.randint(0, 100) for _ in range(0, 2 * 10 + 1)]',
             globals=globals(), number=10000))
print('Медиана')  # 0.014758260999999884 Оптимальный вариант, время выполнения кода минимально
print(timeit('median(lst[:])', setup='lst = [random.randint(0, 100) for _ in range(0, 2 * 10 + 1)]',
             globals=globals(), number=10000))
