"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы.
Сортировка должна быть реализована в виде функции.
Обязательно доработайте алгоритм (сделайте его умнее).

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение. Обязательно сделайте замеры времени обеих реализаций
и укажите дала ли оптимизация эффективность.

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию.
Сделайте выводы!!!
Опишите в чем была ваша доработка и помогла ли вам доработка??
"""

import timeit
import random


def bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] > lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        n += 1
    return lst_obj


orig_list = [random.randint(-100, 100) for _ in range(10)]
print(f'Новый массив: {orig_list}')
print(f'Отсортированный по возрастанию: {bubble_sort(orig_list)}')
print('')

def bubble_sort_reverse(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        n += 1
    return lst_obj

orig_list = [random.randint(-100, 100) for _ in range(10)]
print(f'Новый массив: {orig_list}')
print(f'Отсортированный по убыванию: {bubble_sort_reverse(orig_list)}')
print('')

print('Идея доработки №1 - если за проход по списку не совершается ни одной сортировки, то завершение.')
def bubble_sort_reverse_break(lst_obj):
    n = 1
    count_break = 0
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                count_break += 1
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
            elif i == (len(lst_obj)-2) and n == 1 and count_break < 1:
                return lst_obj
        n += 1
    return lst_obj

#orig_list = [11, 9, 8, 7, 5, 4, 2, 1, 1] # Проверка идеального случая

orig_list = [random.randint(-100, 100) for _ in range(10)] # Проверка работоспособности # на рандомном примере

print(f'Новый массив: {orig_list}')
print(f'Идея доработки №1: {bubble_sort_reverse_break(orig_list)}')
print('')

print('Идея доработки №2 - не совершать лишнюю итерацию, когда максимальный элемент уже попал в конец' )
def bubble_sort_reverse_break_min_iteration(lst_obj):
    n = 1
    count_break = 0
    count_iteration = 0
    while n < len(lst_obj):
        for i in range(len(lst_obj)-count_iteration-n):
            if lst_obj[i] < lst_obj[i+1]:
                count_break += 1
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
            elif i == (len(lst_obj)-2) and n == 1 and count_break < 1:
                print('z nen')
                return lst_obj
        n += 1
        count_iteration += 1
    return lst_obj

orig_list = [random.randint(-100, 100) for _ in range(10)]
#orig_list = [9, 18, 7, 5, 4, 2, 9]
#orig_list =[64, -3, 92, 78, 12, -1, 41, 71, 24, -78]
print(f'Новый массив: {orig_list}')
print(f'Идея доработки №2: {bubble_sort_reverse_break_min_iteration(orig_list)}')
print('')
print('Замеры')
orig_list = [random.randint(-100, 100) for i in range(1000)]
print(
    timeit.timeit(
        "bubble_sort(orig_list[:])",
        globals=globals(),
        number=100))
print(
    timeit.timeit(
        "bubble_sort_reverse(orig_list[:])",
        globals=globals(),
        number=100))
print(
    timeit.timeit(
        "bubble_sort_reverse_break(orig_list[:])",
        globals=globals(),
        number=100))
print(
    timeit.timeit(
        "bubble_sort_reverse_break_min_iteration(orig_list[:])",
        globals=globals(),
        number=100))

# Замеры
"""
14.3101364
14.029707700000001
28.3965838
12.684936100000002
"""

"""
Выводы:
Удивительно, но ловля исключения, требует не мало времени.
Соединив исключение и удаление лишних итераций, положительно повлияло на замеры по времени.
"""

