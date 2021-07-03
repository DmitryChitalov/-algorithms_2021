"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы.

Сортировка должна быть реализована в виде функции.

Обязательно доработайте алгоритм (сделайте его умнее).

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение. Обязательно сделайте замеры времени обеих реализаций
и обосновать дала ли оптимизация эффективность

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию.

Сделайте выводы!!!
Опишите в чем была ваша доработка и помогла ли вам доработка??
"""

from random import randint, randrange
from timeit import timeit

k = int(input('Введите количество элементов списка: '))
source_list = [randrange(-100, 100) for _ in range(k)]
print(f'Исходный список: {source_list}')
print()


def bubble_sort_versa_1(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        n += 1
    return lst_obj


list_sorted_versa_1 = bubble_sort_versa_1(source_list[:])
print(f'Отсортированный по убыванию список: {list_sorted_versa_1}')


def bubble_sort_versa_2(lst_obj):
    n = 1
    while n < len(lst_obj):
        sort_count = 0
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
                sort_count += 1
        if sort_count == 0:
            return f'Отсортированный по убыванию список: {lst_obj}'
        n += 1


print(bubble_sort_versa_2(source_list[:]))
print()

print('В функцию bubble_sort_versa_2 передаю уже отсортированный список:')
print(bubble_sort_versa_2(list_sorted_versa_1))

print()
print('Измеряем время выполнения функций с числом запусков 10000:')
print()
print('Функция без доработки:')
print(timeit('bubble_sort_versa_1(source_list[:])', globals=globals(), number=10000))
print()
print('Функция с доработкой (завершение выполнения, если за проход по списку не совершается ни одной сортировки):')
print(timeit('bubble_sort_versa_2(source_list[:])', globals=globals(), number=10000))
print()
print('Функция с доработкой (передается отсортированный список):')
print(timeit('bubble_sort_versa_2(list_sorted_versa_1)', globals=globals(), number=10000))


# Результаты при n=10:

# Введите количество элементов списка: 10
# Исходный список: [-6, -35, -53, -5, -32, 9, -39, -40, -43, 60]
#
# Отсортированный по убыванию список: [60, 9, -5, -6, -32, -35, -39, -40, -43, -53]
# Отсортированный по убыванию список: [60, 9, -5, -6, -32, -35, -39, -40, -43, -53]
#
# В функцию bubble_sort_versa_2 передаю уже отсортированный список:
# Отсортированный по убыванию список: [60, 9, -5, -6, -32, -35, -39, -40, -43, -53]
#
# Измеряем время выполнения функций с числом запусков 10000:
#
# Функция без доработки:
# 0.4595107999999999
#
# Функция с доработкой (завершение выполнения, если за проход по списку не совершается ни одной сортировки):
# 0.5888953000000003
#
# Функция с доработкой (передается отсортированный список):
# 0.11035649999999997


# Вывод:
# Оптимизация функции не дала положительного эффекта: время выполнения увеличилось за счет введения новой переменной-счетчика
# сортировок, ее изменения, а также необходимости делать проверку значения счетчика после каждого прохода
# (если после прохода счетчик остаются равен нулю, то есть не происходит ни одной сортировки, значит, список уже отсортирован,
# и дальнейшие проходы (если они есть) не нужны.
# Однако если передать в функцию уже отсортированный список, то экономия времени на выполнение функции значительна.
# однако в случае с рандомными списками такая вероятность при большом количестве элементов и большом их диапазоне их значений
# практически равна нулю.
