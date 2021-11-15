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

import copy
import random
import statistics
import timeit

number_cycles = 100000
user_number = int(input("Введите число: "))


def gener_numb(us_num):    # тут сгенерируем массив
    gen_number = [random.randint(0, 100) for _ in range(us_num * 2 + 1)]
    return gen_number


list_number = gener_numb(user_number)
list_number_1 = copy.deepcopy(list_number)    # для поиска в неотсортированном списке


# сортировка
def shell(seq):    # Метод сортировки Шелла.
    cycles = len(seq) // 2
    while cycles:
        for i, elem in enumerate(seq):
            while i >= cycles and seq[i - cycles] > elem:
                seq[i] = seq[i - cycles]
                i -= cycles
            seq[i] = elem
        cycles = 1 if cycles == 2 else int(cycles * 5.0 / 11)

    return seq


# поиск медианы по индексу (user_number)
def search_m_sort(num):
    return f'Медиана равна: {num[user_number]}. Индекс: {user_number}'


# предположим неизвестно введённое пользователем значение,
# а дан только неотсортированный массив
# поиск медианы. (неотсортированный список)
def search_m(num):    # метод удаления макимальных значений
    counter_stop = 0
    len_list = (len(num) // 2)
    while counter_stop != len_list:    # тут удалим все макс значения, проходы до половины длины списка
        num.pop(num.index(max(num, key=lambda i: int(i))))
        counter_stop += 1
    return f'В неотсортированном массиве: \n{list_number_1} \n' \
           f'Медиана равна: {max(num, key=lambda i: int(i))}\n'


# поиск медианы. (отсортированный список)
def search_m_1(num):    # метод удаления макимальных значений
    return f'В отсортированном массиве: \n{list_number_1} \n' \
           f'Медиана равна: {max(num[0:-(len(num) // 2)], key=lambda i: int(i))}\n'


# поиск медианы списка встроенной функцией statistics.
def search_m_statistics(list_numb):
    return f'В отсортированном массиве: \n{list_numb}\n' \
           f'Медиана равна: {statistics.median(list_numb)}'


print(f'Время работы: {timeit.timeit("shell(list_number[:])", globals=globals(), number=number_cycles)}'
      f'\n{shell(list_number)}')

print(f'Время работы: {timeit.timeit("shell(list_number[:])", globals=globals(), number=number_cycles)}'
      f'\n{search_m_sort(list_number[:])}')

print(f'Время работы: {timeit.timeit("search_m(list_number_1[:])", globals=globals(), number=number_cycles)}'
      f'\n{search_m(list_number_1[:])}')

print(f'Время работы: {timeit.timeit("search_m_1(list_number[:])", globals=globals(), number=number_cycles)}'
      f'\n{search_m_1(list_number[:])}')

print(f'Время работы: '
      f'{timeit.timeit("search_m_statistics(list_number[:])", globals=globals(), number=number_cycles)}'
      f'\n{search_m_statistics(list_number[:])}')


"""
Введено число: 10

Время работы: 3.419938299979549 - метод сортировки Шелла
Время работы: 1.92724490002729 - поиск медианы по индексу (в отсортированном списке)
Время работы: 7.241007399978116 - метод удаления макимальных значений (для неотсортированного списка)
Время работы: 0.9760737000033259 - метод удаления макимальных значений (для отсортированного списка)
Время работы: 0.6825518000405282 - поиск медианы списка встроенной функцией statistics


вывод:
встроенная функция statistics.median находит медиану быстрее.

самым медленный - метод удаления макимальных значений (для неотсортированного списка).

PS: 
метод удаления макимальных значений (для отсортированного списка) быстрее, чем
поиск медианы по индексу (в отсортированном списке)
"""

