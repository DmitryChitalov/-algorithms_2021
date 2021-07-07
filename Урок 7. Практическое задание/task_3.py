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


# Создаем массив случайных цифр по формуле
m = int(input('Введите число: \n'))
num_lst_m = list(random.randrange(0, 10) for el in range((2 * int(m)) + 1))
print(f'Получен список: {num_lst_m}')
print(f'Медиана списка по формуле библиотеки statistics: {median(num_lst_m)}')


# функция под поставленную задачу.
def median_for_task(n, items):
    pivot = random.choice(items)

    lesser = [item for item in items if item < pivot]
    if len(lesser) > n:
        return select_nth(n, lesser)
    n -= len(lesser)

    numequal = items.count(pivot)
    if numequal > n:
        return pivot
    n -= numequal

    greater = [item for item in items if item > pivot]
    return select_nth(n, greater)


print(f'Медианное значение по формеле median_for_task(): {median_for_task(m, num_lst_m)}')


# Исходный код для расчета медианы
def select_nth(n, items):
    pivot = random.choice(items)

    lesser = [item for item in items if item < pivot]
    if len(lesser) > n:
        return select_nth(n, lesser)
    n -= len(lesser)

    numequal = items.count(pivot)
    if numequal > n:
        return pivot
    n -= numequal

    greater = [item for item in items if item > pivot]
    return select_nth(n, greater)


def median(items):
    if len(items) % 2:
        return select_nth(len(items)//2, items)
    else:
        left = select_nth((len(items)-1) // 2, items)
        right = select_nth((len(items)+1) // 2, items)

        return (left + right) / 2


print(f'Медианное значение по функции median(): {median(num_lst_m)}')


"""
Если верно понял задание - необходимо представить код, который находит медиану (можно с сортировкой)
Нашел в сети метод получения медианы - https://coderoad.ru/24101524/Поиск медианы списка-Python

Результат работы скрипта.
Введите число: 
5
Получен список: [4, 7, 0, 6, 6, 0, 0, 6, 2, 2, 0]
Медиана списка по формуле библиотеки statistics: 2
Медианное значение по формеле median(): 2
Медианное значение по формеле median_for_task(): 2
"""