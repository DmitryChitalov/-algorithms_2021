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
import timeit
import random


def gnome(data):
    i, size = 1, len(data)
    while i < size:
        if data[i - 1] <= data[i]:
            i += 1
        else:
            data[i - 1], data[i] = data[i], data[i - 1]
            if i > 1:
                i -= 1
    return data[m]


if __name__ == '__main__':
    natural_number = int(input('Please enter number natural: '))
    orig_lst = [random.randint(0, 50) for _ in range(2*natural_number + 1)]
    print(orig_lst[:])
    orig_list = [random.randint(-100, 100) for _ in range(100)]
    print('sort range(100)', timeit.repeat('orig_list[:].sort()', globals=globals(), number=(10**3)))
    print('sorted range(100)', timeit.repeat('sorted(orig_list)', globals=globals(), number=(10**3)))
    print(timeit.repeat('gnome(orig_list[:])', globals=globals(), number=(10**3)))
    orig_list = [random.randint(0, 100) for _ in range(1000)]
    print('sort range(1000)', timeit.repeat('orig_list[:].sort()', globals=globals(), number=(10 ** 3)))
    print('sorted range(1000)', timeit.repeat('sorted(orig_list)', globals=globals(), number=(10 ** 3)))
    print(timeit.repeat('gnome(orig_list[:])', globals=globals(), number=(10**3)))
    """ Результаты: 
    [2.572095439, 2.2244473240000002, 2.249986316, 2.2133835249999994, 2.248025462000001]
    [237.623175705, 235.61256120900003, 235.81549159900004, 236.03719692000004, 236.46828936399993]
    Это медленее чем сортировка методом пузырьком, его результаты в задании 1, а пузырек медленнее чем сортировка слиянием,
    слинием медленнее встроенных функий sort, sorted поэтому с уверенностью контсатирую факт
    что гномья сортировка медленнее всех методов что выше приведены
    Сложность- O(n)
    замеры встроеных функций
    sort range(100) [0.011826131000000004, 0.015269455999999987, 0.00958474799999999, 0.018215013000000002, 0.008847504000000006]
sorted range(100) [0.00663634099999999, 0.010745066999999997, 0.011307836000000016, 0.011373977000000007, 0.0063985750000000174]
sort range(1000) [0.16142175900000003, 0.206803061, 0.20011882599999997, 0.17007312100000005, 0.16969452000000007]
sorted range(1000) [0.16777015799999995, 0.15467993400000002, 0.1509663429999999, 0.15318834000000003, 0.14893763800000004]
    
    """
