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
from statistics import median
from random import randint
from memory_profiler import memory_usage
from timeit import default_timer


# Здесь тоже используем декоратор
def my_decor(func):
    def check_optimize(*args):
        t1 = default_timer()
        m1 = memory_usage()
        result = func(*args)
        m2 = memory_usage()
        t2 = default_timer()
        mem_res = m2[0] - m1[0]
        time_res = t2 - t1
        return f'Память: {mem_res},\nВремя: {time_res},\nРезультат: {result}'
    return check_optimize


my_list = [randint(-100, 100) for i in range(10000 * 2 + 1)]


# Проверка:
@my_decor
def med_decor(med_list):
    return median(med_list)


# Без использования сортировки:
@my_decor
def get_med(med_list):
    max_list = []
    list_med = int((len(med_list) - 1) / 2)
    while len(max_list) <= list_med:
        el = max(med_list)
        max_list.append(el)
        med_list.remove(el)
    return max_list[list_med]


# C использованием сортировки:
def fast_sort(sort_list):
    if len(sort_list) < 1:
        return sort_list
    else:
        divide = sort_list[len(sort_list) // 2]
        left = []
        mid = []
        right = []
        for i in sort_list:
            if i > divide:
                right.append(i)
            elif i < divide:
                left.append(i)
            else:
                mid.append(i)
        return fast_sort(left) + mid + fast_sort(right)


@my_decor
def med_sort(med_list):
    med_pos = int((len(med_list) - 1) / 2)
    return fast_sort(med_list)[med_pos]


print(med_decor(my_list[:]))
print(get_med(my_list[:]))
print(med_sort(my_list[:]))


'''
Память: 0.08203125,
Время: 0.22002090000000002,
Результат: 0
Память: 0.0625,
Время: 4.2163653,
Результат: 0
Память: 0.36328125,
Время: 0.23328170000000004,
Результат: 0
Как всегда, можем видеть, что встроенная функция наиболее оптимзирована, так как имеет
наименьшие затраты по времени и памяти. В свою очередь сортировка не уступает ей по
скорости, но затраты памяти в разы больше. Ну а функция без сортировки, как и ожидалось,
требует не так много памяти, но выполняется крайне медленно. 
''' 
