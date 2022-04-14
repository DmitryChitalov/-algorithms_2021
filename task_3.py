"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные по длине части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы.

Задачу можно решить без сортировки исходного массива.

Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках: Шелла, Гномья, Кучей...

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
import timeit
import random
from statistics import median


def user_input():
    while True:
        usr_input = input('Введите натуральное число: ')
        try:
            if int(usr_input) > 0:
                return int(usr_input)
            else:
                print('Натуральные - числа больше, чем "0"!!!')
        except ValueError:
            print('Вы ввели не натуральное число! Попробуйте ещё раз.')


def gnome_sort(lst_obj):
    n = 1
    k = 2
    while n < len(lst_obj):
        if lst_obj[n - 1] <= lst_obj[n]:
            n = k
            k += 1
        else:
            lst_obj[n - 1], lst_obj[n] = lst_obj[n],lst_obj[n - 1]
            n -= 1
            if n == 0:
                n = k
                k += 1
    return lst_obj


def median_search_2(lst_obj):
    """
    Алгоритм поиска медианы через удаление максимальных элементов до достижения середины списка.
    :param lst_obj:
    :return: median
    """
    for _ in range(len(lst_obj) // 2):
        lst_obj.remove(max(lst_obj))
    return max(lst_obj)


def median_search_3(lst_obj):
    for elem in lst_obj:
        left = [elem2 for elem2 in lst_obj if elem2 < elem]
        right = [elem2 for elem2 in lst_obj if elem2 > elem]
        if len(left) == len(right) or abs(len(left) - len(right)) < lst_obj.count(elem):
            return elem


m = user_input()
my_list = [random.randint(0, 100) for _ in range(2 * m + 1)]

print(f'Медиана, найденная в сортированном списке: {gnome_sort(my_list[:])[m]}')
print(f'Медиана, найденная в несортированном списке. Вариант № 1: {median_search_2(my_list[:])}')
print(f'Медиана, найденная в несортированном списке. Вариант № 2: {median_search_3(my_list[:])}')
print(f'Медиана, найденная встроенной функцией: {median(my_list)}')
print('*' * 50)

# Измерение времени

print(f'Поиск в сортированном списке: '
      f'{timeit.timeit("gnome_sort(my_list[:])[m]",globals=globals(),number=1000)}')
print(f'Поиск в несортированном списке. Вариант № 1: '
      f'{timeit.timeit("median_search_2(my_list[:])",globals=globals(),number=1000)}')
print(f'Поиск в несортированном списке. Вариант № 2: '
      f'{timeit.timeit("median_search_3(my_list[:])",globals=globals(),number=1000)}')
print(f'Поиск в несортированном списке встроенной функцией: '
      f'{timeit.timeit("median(my_list[:])",globals=globals(),number=1000)}')


"""
Для нахождения медианы использовал 4 способа: встроенная функция median, отсортированный массив гномьим методом,
способом через удаление максимального элемента (вариант № 1) и через посроение левых и правых частей (вариант № 2). 
При числе m = 500:
Поиск в сортированном списке:                       64.9601704
Поиск в несортированном списке. Вариант № 1:        7.901983900000005
Поиск в несортированном списке. Вариант № 2:        6.46798299999999
Поиск в несортированном списке встроенной функцией: 0.09820729999999855

Получилось, что самая быстрая это встроенная функция.
Ей уступает метод удаления максимальных элементов, и метод построения левых и правых частей.
Медленнее всех - через гномью сортировку.
"""
