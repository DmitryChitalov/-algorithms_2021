"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы.

Сортировка должна быть реализована в
виде функции.

Обязательно доработайте алгоритм (сделайте его умнее)!

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение
Обязательно сделайте замеры времени обеих реализаций
и обосновать дала ли оптимизация эффективность

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию.

Сделайте выводы!!!
Опишите в чем была ваша доработка и помогла ли вам доработка??
"""

from timeit import timeit
from random import randint

def bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        n += 1
    return lst_obj

def bubble_sort_opt(lst_obj):
    n = 1
    while n < len(lst_obj):
        is_no_action = True
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
                is_no_action = False
        if is_no_action:
            break
        n += 1
    return lst_obj


def bubble_sort_opt2(lst_obj):
    n = 1
    last_el_move = len(lst_obj) - n
    while n < len(lst_obj):
        mem = last_el_move
        for i in range(last_el_move):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
                last_el_move = i
        if last_el_move == mem:
            break
        n += 1
    return lst_obj

orig_list = [randint(-100, 100) for _ in range(10)]
# orig_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(orig_list)
print(bubble_sort(orig_list[:]))
# print(bubble_sort_opt(orig_list[:]))
# print(bubble_sort_opt2(orig_list[:]))
# exit()

list_param = [10, 100, 1000]
func_list = ['bubble_sort', 'bubble_sort_opt', 'bubble_sort_opt2']
max_len = len(max(func_list, key=len))

for param in list_param:
    print(f'Сравним варианты для массива из ({param}) элементов:')
    for el in func_list:
        print(f'Функция {el}:'.ljust(max_len + 10, '_'),
              timeit(el + '(orig_list[:])', setup='orig_list = [randint(-100, 100) for _ in range(param)]',
                     number=100, globals=globals()))


'''
(bubble_sort_opt)
Предложенная "Идея доработки: если за проход по списку не совершается ни одной перестановки, то завершение" 
работает только на небольших и/или частично отсортированных массивах. (см статистику)
Это обусловлено накладными расходами по избыточному изменению флага перестановки (is_no_action) в ходе каждого 
обмена значениями рядом стоящих элементов, его принудительному обнулению и проверке на измененность.

(bubble_sort_opt2)
Можем предположить, что не всегда необходимо делать проход от первого до последнего элемента границы, 
которая после каждого прохода смещается с шагом -1 в сторону начала массива. 
Будем устанавливать эту границу (last_el_move) по индексу последнего "переставленного" элемента.
Также, оставим выход при попроверке на завершение сортировки (mem) 

Честно говоря, складывается впечатление, что лучше метод заменить на более прогрессивный, показывающий более
лучшие результаты на больших множествах сортировки. Как говорится, "Сколько ВАЗ не тюнингуй, МЕРСЕДЕС не получится" 

Аналитика:
Сравним варианты для массива из (10) элементов:
Функция bubble_sort:______ 0.0030078709999999953
Функция bubble_sort_opt:__ 0.00171404
Функция bubble_sort_opt2:_ 0.0015830260000000151
Сравним варианты для массива из (100) элементов:
Функция bubble_sort:______ 0.12311623200000002
Функция bubble_sort_opt:__ 0.125769099
Функция bubble_sort_opt2:_ 0.11211293000000006
Сравним варианты для массива из (1000) элементов:
Функция bubble_sort:______ 13.195855755
Функция bubble_sort_opt:__ 13.373739753
Функция bubble_sort_opt2:_ 13.087470364000001
'''