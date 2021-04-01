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
from statistics import median as med
from random import choice, shuffle, randint


def median(array, k=None):
    if len(array) == 1:
        return array[0]
    if k is None:
        k = ((len(array) - 1) / 2)
    chosen = choice(array)
    left = [x for x in array if x < chosen]
    right = [x for x in array if x > chosen]
    chosens = [x for x in array if x == chosen]
    if len(left) > k:
        return median(left, k)
    elif k < len(left) + len(chosens):
        return chosen
    else:
        return median(right, k - len(left) - len(chosens))


m = 100
my_list = list(range(2 * m + 1))
shuffle(my_list)
print(median(my_list))
print(med(my_list))

# Проверка:

for i in range(1000):
    some_list = [randint(-100, 100) for x in range(2 * m + 1)]
    assert median(some_list) == med(some_list)
else:
    print("Проверка выполнена успешно")

