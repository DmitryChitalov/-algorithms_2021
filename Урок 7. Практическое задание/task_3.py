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
        return quick_select(lst_obj, len(lst_obj) // 2, pivot_fn)


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
        return pivots[0]
    else:
        return quick_select(highs, k - len(lows) - len(pivots), pivot_fn)


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


def select_median_with_shell_sort(lst_obj):
    shell(lst_obj)
    return lst_obj[len(lst_obj) // 2]


def median_stat(lst_obj):
    return median(lst_obj)


def new_lists():
    orig_list1 = [randint(-100, 100) for _ in range(11)]
    orig_list2 = [randint(-100, 100) for _ in range(101)]
    orig_list3 = [randint(-100, 100) for _ in range(1001)]
    orig_list4 = [randint(-100, 100) for _ in range(10001)]
    orig_list5 = [randint(-100, 100) for _ in range(100001)]

    return orig_list1, orig_list2, orig_list3, orig_list4, orig_list5


orig_list = [randint(-100, 100) for _ in range(5)]
print(orig_list)
print(sorted(orig_list[:]))
print(median_stat(orig_list[:]), quick_select_median(orig_list[:]), select_median_with_shell_sort(orig_list[:]),
      end='\n\n')

explore_functions = ['quick_select_median', 'median_stat', 'select_median_with_shell_sort']
for test_number in range(1, 3):
    print(f'Тест {test_number}', end='\n\n')
    explore_lists = new_lists()

    for function in explore_functions:
        print(f'Функция {function}')

        for explore_list in explore_lists:
            time_sec = min(repeat(
                f'{function}({explore_list[:]})', globals=globals(), timer=default_timer, repeat=3, number=1))

            print(f'El: {len(explore_list)}, best time: {round(time_sec, 4)} sec')
        print('')

# Тест 1

# Функция quick_select_median             Функция median_stat                     Функция select_median_with_shell_sort
# El: 11, best time: 0.0 sec              El: 11, best time: 0.0 sec              El: 11, best time: 0.0 sec
# El: 101, best time: 0.0001 sec          El: 101, best time: 0.0 sec             El: 101, best time: 0.0005 sec
# El: 1001, best time: 0.0007 sec         El: 1001, best time: 0.0001 sec         El: 1001, best time: 0.0067 sec
# El: 10001, best time: 0.0097 sec        El: 10001, best time: 0.0017 sec        El: 10001, best time: 0.0897 sec
# El: 100001, best time: 0.0593 sec       El: 100001, best time: 0.0186 sec       El: 100001, best time: 1.0689 sec
# El: 1000001, best time: 0.7588 sec      El: 1000001, best time: 0.1931 sec

# Тест 2

# Функция quick_select_median             Функция median_stat                     Функция select_median_with_shell_sort
# El: 11, best time: 0.0 sec              El: 11, best time: 0.0 sec              El: 11, best time: 0.0 sec
# El: 101, best time: 0.0001 sec          El: 101, best time: 0.0 sec             El: 101, best time: 0.0004 sec
# El: 1001, best time: 0.0009 sec         El: 1001, best time: 0.0001 sec         El: 1001, best time: 0.0069 sec
# El: 10001, best time: 0.0044 sec        El: 10001, best time: 0.0017 sec        El: 10001, best time: 0.0879 sec
# El: 100001, best time: 0.0447 sec       El: 100001, best time: 0.0186 sec       El: 100001, best time: 1.0487 sec
# El: 1000001, best time: 0.5578 sec      El: 1000001, best time: 0.1908 sec

# Алгоритм quick_select_median находит медиану рекурсивно путём разложения на подсписки и дальнейшего поиска в том
# подсписке, где она оказалась. Крайних случаев тут два, одни из них когда список упразднится до одного элемента
# из-за выбора барьерного элемента всегда либо максимальным, либо минимальным, в этом случае сложность будет O(n^2);
# второй - когда медиана оказывается в подсписке с выбранным барьерным элементом (pivot),
# в лучшем случае сложность O(n) - когда была сразу выбрана медиана в качестве барьерного элемента
# Такая реализация алгоритма работает для списков с нечетным количеством элементов

# Сортировка Шелла имеет лучшую временную сложность O(n log^2 n)
# и для поиска медианы затрачивает больше временных ресурсов
