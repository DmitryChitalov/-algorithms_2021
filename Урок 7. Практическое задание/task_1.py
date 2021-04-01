"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы.

Сортировка должна быть реализована в
виде функции.

Обязательно доработайте алгоритм (сделайте его умнее)!

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение.
Обязательно сделайте замеры времени обеих реализаций
и обосновать дала ли оптимизация эффективность

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
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        n += 1
    return lst_obj


def bubble_sort_modify(lst_obj):
    n = 1
    while n < len(lst_obj):
        is_change = False
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
                is_change = True
        if not is_change:
            break
        n += 1
    return lst_obj


orig_list = [random.randint(-100, 100) for _ in range(10)]
print('Исходный массив:', orig_list)  # чтоб список не был отсортирован перед замерами, функцию применяем к копии
print('Отсортированный массив:', bubble_sort(orig_list[:]))
print('Модифицированная функция:', bubble_sort_modify(orig_list[:]))
print()

print('Результаты замеров:')

# замеры 10
print('10 измерений')
print('Исходная функция:', timeit.timeit(
        "bubble_sort(orig_list[:])",
        globals=globals(),
        number=1000))  # -> 0.012880494

print('Модифицированная функция:', timeit.timeit(
        "bubble_sort_modify(orig_list[:])",
        globals=globals(),
        number=1000))  # -> 0.012642699

orig_list = [random.randint(-100, 100) for _ in range(100)]
print()

# замеры 100
print('100 измерений')
print('Исходная функция:', timeit.timeit(
        "bubble_sort(orig_list[:])",
        globals=globals(),
        number=1000))  # -> 0.945243038

print('Модифицированная функция:', timeit.timeit(
        "bubble_sort_modify(orig_list[:])",
        globals=globals(),
        number=1000))  # -> 0.94148695

orig_list = [random.randint(-100, 100) for _ in range(1000)]
print()

# замеры 1000
print('1000 измерений')
print('Исходная функция:', timeit.timeit(
        "bubble_sort(orig_list[:])",
        globals=globals(),
        number=1000))  # -> 92.881145492

print('Модифицированная функция:', timeit.timeit(
        "bubble_sort_modify(orig_list[:])",
        globals=globals(),
        number=1000))  # -> 93.82600822699999

'''
Модификация состояла в завершении цикла при отсутствии сортировки.
Замеры показали, что модификация не дала улучшения по времени, потому что вероятность 
получить сразу отсортированный массив и выйти из цикла ничтожно мала.
'''
