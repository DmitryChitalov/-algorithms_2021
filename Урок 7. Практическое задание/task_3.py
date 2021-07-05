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

import random
import timeit

# Сначала попробовал реализовать поиск медианы по уже заданному списку
"""
my_list = [-12, -12, -6, 1, 6, 9, 9]
average_num = round(sum(my_list)/len(my_list))
print(sum(my_list)/len(my_list))
print(average_num)
difference_el = [abs((i - average_num)) for i in my_list]
print(difference_el)
print(min(difference_el))
print(difference_el.index((min(difference_el))))
print(f'Медиана списка: {my_list[(difference_el.index((min(difference_el))))]}.')
"""


def func_median(my_list):
    average_num = round(sum(my_list) / len(my_list))
    difference_el = [abs((i - average_num)) for i in my_list]
    return f'Медиана списка: {my_list[(difference_el.index((min(difference_el))))]}.'

rand_num = 2 * ((random.randint(0, 10000))) + 1
print(f'Случайное число равно: {rand_num}')
orig_list = [random.randint(-100, 100) for i in range(rand_num)]
print(func_median(orig_list))

print('Время затраченное на поиск медианы:', timeit.timeit("""
import random
def func_median(my_list):
    average_num = round(sum(my_list) / len(my_list))
    difference_el = [abs((i - average_num)) for i in my_list]
    return f'Медиана списка: {my_list[(difference_el.index((min(difference_el))))]}.'
rand_num = 2 * ((random.randint(0, 10000))) + 1
orig_list = [random.randint(-100, 100) for i in range(rand_num)]
func_median(orig_list)
""", number=1000))



"""
    Результаты замеров:
        Случайное число равно: 15205
        Медиана списка: 0.
        Время затраченное на поиск медианы: 6.485537
"""
