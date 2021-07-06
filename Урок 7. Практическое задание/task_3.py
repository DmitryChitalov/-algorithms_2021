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


from statistics import median
import random
import timeit


def del_max(lst_obj):
    for _ in range(m):
        lst_obj.remove(max(lst_obj))
    med = max(lst_obj)
    return f'Для массива {a} значение медианы равно {med}, индекс медианы равен {a.index(med)}'


def gnom_sort(lst_obj):
    i = 1
    j = 2  # индекс элемента, на котором остановился гном
    size = len(lst_obj)
    while i < size:
        if lst_obj[i - 1] < (lst_obj[i]):
            i = j
            j += 1
        else:
            lst_obj[i - 1], lst_obj[i] = lst_obj[i], lst_obj[i-1]
            i -= 1
            if i == 0:
                i = j
                j += 1
    return f'Для массива {a} значение медианы равно {lst_obj[m]}, индекс медианы равен {m}'


m = int(input('Ведите значение m'))
length = 2 * m + 1
a = [random.randint(0, 50) for _ in range(length)]
print(f'Медиана массива {a} равна {median(a[:])}, индекс медианы равен {m}')
print(del_max(a[:]))
print(gnom_sort(a[:]))

stmt = [
        'del_max(a[:])',
        'gnom_sort(a[:])'
    ]

for st in stmt:
    print(f'на выполение функции {st} затрачено времени: '
          f'{timeit.timeit(st, setup="a =[random.randint(0, 50) for _ in range(10)]", number=1000, globals=globals())}')

for st in stmt:
    print(f'на выполение функции {st} затрачено времени: '
          f'{timeit.timeit(st, setup="a =[random.randint(0, 50) for _ in range(100)]", number=1000, globals=globals())}')

for st in stmt:
    print(f'на выполение функции {st} затрачено времени: '
          f'{timeit.timeit(st, setup="a =[random.randint(0, 50) for _ in range(1000)]", number=1000, globals=globals())}')


"""
Метод удаления максимальных значений намного эффективнее гномьей сортировки, т.к. метод гномье сортировки может
достигать сложность O(n^2)
на выполение функции del_max(a[:]) затрачено времени: 0.002595600000000031
на выполение функции gnom_sort(a[:]) затрачено времени: 0.004588700000000001
на выполение функции del_max(a[:]) затрачено времени: 0.008619000000000154
на выполение функции gnom_sort(a[:]) затрачено времени: 0.3257730000000001
на выполение функции del_max(a[:]) затрачено времени: 0.05258750000000001
на выполение функции gnom_sort(a[:]) затрачено времени: 36.271869
"""
