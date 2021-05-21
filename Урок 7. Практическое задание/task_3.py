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
from random import choice, randint
from statistics import median
from timeit import repeat, default_timer


def quick_select_median(lst_obj, pivot_fn=choice):
    if len(lst_obj) % 2 == 1:
        return quick_select(lst_obj, len(lst_obj) / 2, pivot_fn)
    else:
        return 0.5 * (quick_select(lst_obj, len(lst_obj) / 2 - 1, pivot_fn) +
                      quick_select(lst_obj, len(lst_obj) / 2, pivot_fn))


def quick_select(lst_obj, k, pivot_fn):
    if len(lst_obj) == 1:
        return lst_obj[0]

    pivot = pivot_fn(lst_obj)

    lows = [el for el in lst_obj if el < pivot]
    highs = [el for el in lst_obj if el > pivot]
    pivots = [el for el in lst_obj if el == pivot]

    if k < len(lows):
        return quick_select(lows, k, pivot_fn)
    elif k < len(lows) + len(pivots):
        # Нам повезло и мы угадали медиану
        return pivots[0]
    else:
        return quick_select(highs, k - len(lows) - len(pivots), pivot_fn)


def median_stat(lst_obj):
    return median(lst_obj)


def new_lists():
    orig_list1 = [randint(-100, 100) for _ in range(10)]
    orig_list2 = [randint(-100, 100) for _ in range(100)]
    orig_list3 = [randint(-100, 100) for _ in range(1000)]
    orig_list4 = [randint(-100, 100) for _ in range(10000)]
    orig_list5 = [randint(-100, 100) for _ in range(100000)]

    return orig_list1, orig_list2, orig_list3, orig_list4, orig_list5


orig_list = [randint(-100, 100) for _ in range(6)]
print(orig_list)
print(sorted(orig_list[:]))
print(median_stat(orig_list[:]), quick_select_median(orig_list[:]), end='\n\n')

explore_functions = ['quick_select_median', 'median_stat']
for test_number in range(1, 3):
    print(f'Тест {test_number}', end='\n\n')
    explore_lists = new_lists()

    for function in explore_functions:
        print(f'Функция {function}')

        for explore_list in explore_lists:
            time_sec = min(repeat(
                f'{function}({explore_list[:]})', globals=globals(), timer=default_timer, repeat=3, number=1))

            print(f'Elements: {len(explore_list)}, best time: {round(time_sec, 4)} сек')
        print('')

# Тест 1

# Функция quick_select_median                              Функция median_stat
# Elements: 10, best time: 0.0 сек                         Elements: 10, best time: 0.0 сек
# Elements: 100, best time: 0.0003 сек                     Elements: 100, best time: 0.0 сек
# Elements: 1000, best time: 0.0017 сек                    Elements: 1000, best time: 0.0002 сек
# Elements: 10000, best time: 0.0205 сек                   Elements: 10000, best time: 0.0018 сек
# Elements: 100000, best time: 0.1431 сек                  Elements: 100000, best time: 0.0184 сек

# Тест 2

# Функция quick_select_median                              Функция median_stat
# Elements: 10, best time: 0.0 сек                         Elements: 10, best time: 0.0 сек
# Elements: 100, best time: 0.0002 сек                     Elements: 100, best time: 0.0 сек
# Elements: 1001, best time: 0.0005 сек                    Elements: 1001, best time: 0.0001 сек
# Elements: 10001, best time: 0.0084 сек                   Elements: 10001, best time: 0.0018 сек
# Elements: 100001, best time: 0.0607 сек                  Elements: 100001, best time: 0.0186 сек

# Алгоритм quick_select_median найдена на просторах интернета, особо ничего не переделывал.
# Доказано, что в лучшем случае, он будет иметь линейную сложность. что примерно так и отражается на результатах тестов.
# В худшем случае сложность может возрасти до квадратичной, когда барьрный элемент (pivot) будет всегда выбираться
# только максимальным или только минимальным.
# Кроме того, медиана будет средним арифмитическим между двумя средними при четном количестве элементов в списке,
# что как минимум удваивает время выполнения для алгоритма quick_select_median.
# Несмотря на линейную сложность в лучшем случае, алгоритм нахождения медианы из модуля statistics всё равно быстрее =)
