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


def loop_1(list_item):
    num = 1
    while num < len(list_item):
        for i in range(len(list_item) - num):
            if list_item[i] < list_item[i + 1]:
                list_item[i], list_item[i + 1] = list_item[i + 1], list_item[i]
        num += 1
    return list_item


def loop_2(list_item):
    num = 1
    while num < len(list_item):
        go = False
        for i in range(len(list_item) - num):
            if list_item[i] < list_item[i + 1]:
                list_item[i], list_item[i + 1] = list_item[i + 1], list_item[i]
                go = True
        if not go:
            break
        num += 1
    return list_item


list_pattern = [random.randint(-100, 100) for _ in range(12)]

print('Сгенерированный список:\n', list_pattern)
print()
print('Отсортированный список по убыванию:\n', loop_1(list_pattern[:]))
print()
print('Отсортированный список по убыванию модифицированной функцией:\n', loop_2(list_pattern[:]))

list_pattern = [random.randint(-100, 100) for _ in range(1000)]
print()
print('Время обычной функции:')
print(timeit.timeit("loop_1(list_pattern[:])", globals=globals(), number=1000))
print()
print('Время модифицированной функции:')
print(timeit.timeit("loop_2(list_pattern[:])", globals=globals(), number=1000))


'''
Использована переменная которая отвечает за выход из цикла. Выходить из цикла если за один проход нет ни одной 
перестановки. Оптимизация ничего не дала и время чуть выросло из-за того, что чаще всего он 
заканчивает изменения на 4 из пяти проходов для num. Цикл выполняется пятый раз, но при нем условие не меняется.

Исходный список: 
[33, -79, 6, 28, -38, 1, -91, -1, -46, 0, -17, -10] 
Отсортированный список по убыванию: 
[33, 28, 6, 1, 0, -1, -10, -17, -38, -46, -79, -91] 
Отсортированный список по убыванию модифицированной функцией: 
[33, 28, 6, 1, 0, -1, -10, -17, -38, -46, -79, -91] 
Время обычной функции: 53.73198843499995
Время модифицированной 
функции: 54.73322164299998 '''