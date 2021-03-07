"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные по длине части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы.

Задачу можно решить без сортировки исходного
массива.

Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках: Шелла, Гномья, Кучей...

[5, 3, 4, 3, 3, 3, 3]

[3, 3, 3, 3, 3, 4, 5]

my_lst
new_lts

arr[m]


from statistics import median

[3, 4, 3, 3, 5, 3, 3]


left.clear()
right.clear()


m = 3
len = 7
i
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


# Первый вариант с сортировкой при помощи алгоритма Шелла
def shell(data):
    inc = len(data) // 2
    while inc:
        for i, el in enumerate(data):
            while i >= inc and data[i - inc] > el:
                data[i] = data[i - inc]
                i -= inc
            data[i] = el
        inc = 1 if inc == 2 else int(inc * 5.0 / 11)
    return data


# Вариант с созданием списков
def my_func(lst):
    left = []
    right = []
    for i in lst:
        for j in lst:
            if i > j:
                left.append(j)
            elif i < j:
                right.append(j)

        if len(left) == len(right):
            return i
        left.clear()
        right.clear()


# Вариант с удалением максимального числа
def max_del(lst):
    for i in range(len(lst) // 2):
        lst.remove(max(lst))
    return max(lst)


user_input = int(input('Введите натуральное число: '))
massive_len = (2 * user_input + 1)
a = [randint(0, 500) for _ in range(massive_len)]
print(a)
print('Медиана для сгенерированого отсортировоного  списка', shell(a[:])[user_input])
print('Медиана для сгенерированого не отсортировоного списка при помощи моей функции', my_func(a[:]))
print('Медиана при помощи удаления максимального числа', max_del(a[:]))
print('Медиана при помощи встроенной функции для проверки правильности', median(a))
