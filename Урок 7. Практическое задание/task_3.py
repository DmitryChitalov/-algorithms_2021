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
from timeit import timeit
from statistics import median
from random import randint, choice
from numpy import median as med


# Встпроенные методы
def find_median(li):
    return sorted(li)[m]


# statistics
def find_median_st(li):
    return median(li)


# попробуем сортировку Шелла
def find_median_shell(li):
    inc = len(li) // 2
    while inc:
        for i, el in enumerate(li):
            while i >= inc and li[i - inc] > el:
                li[i] = li[i - inc]
                i -= inc
            li[i] = el
        inc = 1 if inc == 2 else int(inc * 5.0 / 11)
    return li[m]


# Медиана от numpy
def find_median_numpy(li):
    return int(med(li))


# этот способ озвучивался на уроке, поэтому не интересно, там все было сказано
def median_les(li):
    for v in range(m):
        li.remove(max(li))
    return max(li)


# А вот теперь попробуем творчески подойти к решению вопроса. Например, рекурсия. В основу алгоритма положим мысль,
# что если мы будем постоянно делить массив по произвольной точке, раскидывая большие и меньшие значения,
# на определенном этапе мы придем к медиане массива. При этом выбор относительно того, какой массив загонять в
# рекурсию будем делать на основании его длины. По сути делаем то же, что в median_les, но не удаляя элементы,
# а просто разбивая массив, что должно приносить существенную выгоду на длинных массивах
def divide_list(li, rank):
    point = choice(li)  # Выберем некоторую случайную величину в массиве
    smaller_list = [x for x in li if x < point]  # сюда соберем все элементы меньше ее
    equal_num = sum([x == point for x in li])  # тут будет кол-ва совападающих с начальной точкой элементов
    bigger_list = [x for x in li if x > point]  # сюда соберем все элементы больше ее
    if len(smaller_list) > rank:  # Проверяем длину массива меньших чисел
        return divide_list(smaller_list, rank)
    elif len(smaller_list) + equal_num > rank:  # Если длина меньших + кол-во одинаковых больше половины длины
        # входного массива - возвращаем точку, это и есть медиана
        return point
    else:
        return divide_list(bigger_list, rank - len(smaller_list) - equal_num)  # ну тут понятно, загоняем больший
        # лист, но длину массива ограничиваем, вычитая длину массива с меньшими и кол-во одинаковых


if __name__ == '__main__':
    for m in [20, 50, 100, 1000]:
        ms = [randint(0, 100) for x in range(2 * m + 1)]
        print(f'Результаты для m = {m} :')
        print(find_median.__name__, find_median(ms[:]), timeit('find_median(ms[:])', globals=globals(), number=1000))
        print(find_median_st.__name__, find_median_st(ms[:]),
              timeit('find_median_st(ms[:])', globals=globals(), number=1000))
        print(find_median_shell.__name__, find_median_shell(ms[:]),
              timeit('find_median_shell(ms[:])', globals=globals(), number=1000))
        print(find_median_numpy.__name__, find_median_numpy(ms[:]),
              timeit('find_median_numpy(ms[:])', globals=globals(), number=1000))
        print(median_les.__name__, median_les(ms[:]), timeit('median_les(ms[:])', globals=globals(), number=1000))
        print(divide_list.__name__, divide_list(ms[:], len(ms) // 2),
              timeit('divide_list(ms[:], len(ms)//2)', globals=globals(), number=1000))
        print('#' * 15)

"""
Результаты для m = 20 :
find_median 35 0.000897099999999984  1
find_median_st 35 0.0011089000000000793 2
find_median_shell 35 0.026370800000000028 6
find_median_numpy 35 0.023028699999999902 5
median_les 35 0.012603200000000037  3
divide_list 35 0.015951700000000013 4
###############
Результаты для m = 50 :
find_median 53 0.0031144000000000727  2
find_median_st 53 0.0025984000000000007 1
find_median_shell 53 0.0803777 6
find_median_numpy 53 0.02498800000000012 3
median_les 53 0.06342419999999982  5
divide_list 53 0.036953400000000025 4
###############
Результаты для m = 100 :
find_median 48 0.005642400000000158 1
find_median_st 48 0.008853499999999848 2
find_median_shell 48 0.16959619999999997 5
find_median_numpy 48 0.029239999999999933 3
median_les 48 0.24096950000000006 6
divide_list 48 0.06827230000000006 4
###############
Результаты для m = 1000 :
find_median 50 0.151991 2
find_median_st 50 0.15266500000000005 3
find_median_shell 50 3.2247693 5
find_median_numpy 50 0.12304539999999964 1
median_les 50 22.359197899999998 6
divide_list 50 0.5950236999999987 4
###############
"""
# Итого, мы видим, что быстрее всех отрабатывают встроенная sorted и statictics. Но на длинных листах уже Numpy
# показывает лучшие результаты(на мелких он проигрывает из-за необходимости создавать свои объекты). Вариант с урока
# неплох только на мелких списках и успешно уходит в конец очереди с увеличением длины списка, видимо, из-за большого
# количества итераций с массивами. Как ни странно, но рекурсия показывает ровные, стабильные результаты на любых
# массивах, держась на 4 месте, причем скорость исполнения функции растет вовсе не драматически. Сортировка шелла
# предсказуемо медленная, на мелких списках пятая, на крупных опережает вариант с урока.
