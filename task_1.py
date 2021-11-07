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

def bubble_sort_optimize(lst_obj):
    n = 1

    while n < len(lst_obj):
        sorted = True #Для оптимизации (Цикл завершается, если замен больше не происходит)

        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
                sorted = False

        if sorted == True:
            #print(f'количество выполненных замен {n}')
            break

        n += 1
    return lst_obj

def bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        # print(f'количество выполненных замен {n}')
        n += 1
    return lst_obj

orig_list = [random.randint(-100, 100) for _ in range(10)]



# замеры 10
print(
    timeit.timeit(
        "bubble_sort_optimize(orig_list[:])",
        globals=globals(),
        number=1000))

print(
    timeit.timeit(
        "bubble_sort(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [random.randint(-100, 100) for _ in range(100)]

# замеры 100
print(
    timeit.timeit(
        "bubble_sort_optimize(orig_list[:])",
        globals=globals(),
        number=1000))

print(
    timeit.timeit(
        "bubble_sort(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [random.randint(-100, 100) for _ in range(1000)]

# замеры 1000
print(
    timeit.timeit(
        "bubble_sort_optimize(orig_list[:])",
        globals=globals(),
        number=1000))

print(
    timeit.timeit(
        "bubble_sort(orig_list[:])",
        globals=globals(),
        number=1000))


"""
замеры на 10 значений
0.013755100000000006 - оптимизированная
0.015581900000000003 - не оптимизированная
===========
замеры на 100 значений
1.2388474 - оптимизированная
1.216003 - не оптимизированная
===========
замеры на 1000 значений
129.63395450000002 - оптимизированная
131.6329278 - не оптимизированная
"""

"""
В среднем оптимизированная функция выполняется быстрее но не намного
разница в 2-3 секунды на больших значениях  не существенна
также были и случаи запусков когда не оптимизированная выполнялась быстрее
поэтому смысла в данной доработке нету так как вероятность более ранней отсортированности очень мала 
"""