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


def quickselect_median(l, pivot_fn=random.choice):
    if len(l) % 2 == 1:
        return quickselect(l, len(l) / 2, pivot_fn)
    else:
        return 0.5 * (quickselect(l, len(l) / 2 - 1, pivot_fn) +
                      quickselect(l, len(l) / 2, pivot_fn))


def quickselect(l, k, pivot_fn):
    """
    Выбираем k-тый элемент в списке l (с нулевой базой)
    :param l: список числовых данных
    :param k: индекс
    :param pivot_fn: функция выбора pivot, по умолчанию выбирает случайно
    :return: k-тый элемент l
    """
    if len(l) == 1:
        assert k == 0
        return l[0]

    pivot = pivot_fn(l)

    lows = [el for el in l if el < pivot]
    highs = [el for el in l if el > pivot]
    pivots = [el for el in l if el == pivot]

    if k < len(lows):
        return quickselect(lows, k, pivot_fn)
    elif k < len(lows) + len(pivots):
        # Нам повезло и мы угадали медиану
        return pivots[0]
    else:
        return quickselect(highs, k - len(lows) - len(pivots), pivot_fn)


def generate_list(m: int):
    return [random.randint(-100, 100) for _ in range(m)]


def median(l):
    l = sorted(l)
    if len(l) % 2 == 1:
        return l[len(l) // 2]
    else:
        return 0.5 * (l[len(l) // 2 - 1] + l[len(l) // 2])


m = int(input('Введите размер массива: '))
l = generate_list(m)
print(l)
print(quickselect_median(l))
print(median(l[:]))
print(
    f"Поиск медианы функией quickselect составила {timeit.timeit('quickselect_median(l[:])', globals=globals(), number=1000)} секунд")
print(
    f"Поиск медианы функией median составила {timeit.timeit('median(l[:])', globals=globals(), number=1000)} секунд")

# решение за линейное время
# также существует и менее оптимальное решение через сортировку массива
# используя quicksort, скорость алгоритма увеличится до nlogn
#однако несмотря на то, что ассимптотически первый алогритм лучше, на практике
# вторая показывает результат чуть ли е в 10 раз лучше. Возможно это связано с
#затратами на время создания списков Lows, highs, pivots
