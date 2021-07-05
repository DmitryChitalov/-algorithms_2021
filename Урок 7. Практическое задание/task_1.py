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

def bubble_sort_op(lst_obj):
    n = 1
    stop_timer = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] > lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
                stop_timer = 1
            else:
                stop_timer += 1
        if stop_timer == len(lst_obj):
            return lst_obj
        n += 1
    return lst_obj


orig_list1 = [i for i in range(10)]
orig_list2 = [i for i in range(100)]
orig_list3 = [i for i in range(1000)]

# замеры 10
print("Неоптимизированная функция на 10 с заранее отсортированным списком: ",
    timeit.timeit(
        "bubble_sort(orig_list1[:])",
        globals=globals(),
        number=1000))

# замеры 100
print("Неоптимизированная функция на 100 с заранее отсортированным списком: ",
    timeit.timeit(
        "bubble_sort(orig_list2[:])",
        globals=globals(),
        number=1000))

# замеры 1000
print("Неоптимизированная функция на 1000 с заранее отсортированным списком: ",
    timeit.timeit(
        "bubble_sort(orig_list3[:])",
        globals=globals(),
        number=1000))


# замеры 10
print("Оптимизированная функция на 10 с заранее отсортированным списком: ",
    timeit.timeit(
        "bubble_sort_op(orig_list1[:])",
        globals=globals(),
        number=1000))

# замеры 100
print("Оптимизированная функция на 100 с заранее отсортированным списком: ",
    timeit.timeit(
        "bubble_sort_op(orig_list2[:])",
        globals=globals(),
        number=1000))

# замеры 1000
print("Оптимизированная функция на 1000 с заранее отсортированным списком: ",
    timeit.timeit(
        "bubble_sort_op(orig_list3[:])",
        globals=globals(),
        number=1000))



"""
    Вывод: Оптимизировал запрос и в итоге обнаружил очень хороший прирост. 
    Резултаты замеров:
            Неоптимизированная функция на 10:  0.005676800000000003
            Оптимизированная функция на 10:  0.0009713000000000013
            Неоптимизированная функция на 100:  0.24236389999999997
            Оптимизированная функция на 100:  0.006882400000000011
            Неоптимизированная функция на 1000:  29.785738499999997
            Оптимизированная функция на 1000:  0.0794990999999996
            
        Оптимизировал с помощью дополнительного счётчика, который каждый раз увеличивается, если элементы не меняются
        местами, но если хотя бы раз элементы меняются, то этот новый счётчик обнуляется, а выходит из функции только
        в том случае, если этот новый счётчик доходит до необходимого значения, в моём примере я взял длинну массива, то
        есть если счётчик сравнивается с длинной массива, то функция запускает return массива.
        
        Оптимизация очень сильно помогла, особо сильно виден прирост на больших значениях, честно говоря не ожидал таких
        результатов.
"""


orig_list = [random.randint(-100, 100) for _ in range(10)]

# замеры 10
print("Неоптимизированная функция на 10: ",
    timeit.timeit(
        "bubble_sort(orig_list[:])",
        globals=globals(),
        number=1000))

# замеры 10
print("Оптимизированная функция на 10: ",
    timeit.timeit(
        "bubble_sort_op(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [random.randint(-100, 100) for _ in range(100)]

# замеры 100
print("Неоптимизированная функция на 100: ",
    timeit.timeit(
        "bubble_sort(orig_list[:])",
        globals=globals(),
        number=1000))

# замеры 100
print("Оптимизированная функция на 100: ",
    timeit.timeit(
        "bubble_sort_op(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [random.randint(-100, 100) for _ in range(1000)]

# замеры 1000
print("Неоптимизированная функция на 1000: ",
    timeit.timeit(
        "bubble_sort(orig_list[:])",
        globals=globals(),
        number=1000))

# замеры 1000
print("Оптимизированная функция на 1000: ",
    timeit.timeit(
        "bubble_sort_op(orig_list[:])",
        globals=globals(),
        number=1000))


"""
    Дополнение: Оптимизация в итоге отрабатывает намного быстрее заранее отсортированные списки, ну а у 
        неотсортированных оптимизация немного увеличивает время выполнения, но не то чтобы на много, поэтому всё же
        думаю можно считать оптимизацию успешной.
    
    Результаты замеров:
            Неоптимизированная функция на 10:  0.005639399999999739
            Оптимизированная функция на 10:  0.006414100000000644
            Неоптимизированная функция на 100:  0.5302869999999977
            Оптимизированная функция на 100:  0.5514600000000023
            Неоптимизированная функция на 1000:  64.2310933
            Оптимизированная функция на 1000:  73.3345253
"""
