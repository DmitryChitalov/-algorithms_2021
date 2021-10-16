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


from statistics import median
from random import randint


def create_random_list(num):
    unsorted_list = [randint(-100, 100) for _ in range(2 * num + 1)]
    print('Неотсортированный список:', unsorted_list)
    return unsorted_list


def find_median(num):
    data = create_random_list(num)
    for _ in range(int(len(data) / 2)):
        data.remove(max(data))
    print('Ответ: ', end='')
    return max(data)


def find_median_full(num):
    data = create_random_list(num)
    inc = len(data) // 2
    while inc:
        for i, el in enumerate(data):
            while i >= inc and data[i - inc] > el:
                data[i] = data[i - inc]
                i -= inc
            data[i] = el
        inc = 1 if inc == 2 else int(inc * 5.0 / 11)
    print('Ответ: ', end='')
    return data[num]


def check_answer(data):
    return median(data)


if __name__ == '__main__':
    print(find_median(int(input('Введите число: '))))
    print(find_median_full(int(input('Введите число: '))))

