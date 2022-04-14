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
from random import randint
from timeit import timeit


def bubble_sort(s_list):
    for i in range(len(s_list)):
        for j in range(len(s_list)-1):
            if s_list[j] < s_list[j+1]:
                s_list[j], s_list[j+1] = s_list[j+1], s_list[j]
    return s_list


def while_bubble_sort(s_list):
    el = 1
    while el < len(s_list):
        for i in range(len(s_list)-el):
            if s_list[i] < s_list[i+1]:
                s_list[i], s_list[i+1] = s_list[i+1], s_list[i]
        el += 1
    return s_list


def flag_bubble_sort(s_list, flag=True):
    el = 1
    while el < len(s_list):
        for i in range(len(s_list)-1):
            if s_list[i] < s_list[i+1]:
                s_list[i], s_list[i + 1] = s_list[i + 1], s_list[i]
                flag = False
        if flag:
            break
        el += 1
    return s_list


rand_list = [randint(-100, 100) for _ in range(10)]
rand_list_2 = [randint(-100, 100) for _ in range(100)]
rand_list_3 = [randint(-100, 100) for _ in range(1000)]

print(f'Time for main bubble sort. 10 elements: '
      f'{timeit("bubble_sort(rand_list)[:]", globals=globals(), number=100)}\n'
      f'Time for main bubble sort. 100 elements: '
      f'{timeit("bubble_sort(rand_list_2)[:]", globals=globals(), number=100)}\n'
      f'Time for main bubble sort. 1000 elements: '
      f'{timeit("bubble_sort(rand_list_3)[:]", globals=globals(), number=100)}\n'
      f'{"~"*70}\n'
      f'Time for while bubble sort. 10 elements: '
      f'{timeit("while_bubble_sort(rand_list)[:]", globals=globals(), number=100)}\n'
      f'Time for while bubble sort. 100 elements: '
      f'{timeit("while_bubble_sort(rand_list_2)[:]", globals=globals(), number=100)}\n'
      f'Time for while bubble sort. 1000 elements: '
      f'{timeit("while_bubble_sort(rand_list_3)[:]", globals=globals(), number=100)}\n'
      f'{"~"*70}\n'
      f'Time for flag bubble sort. 10 elements: '
      f'{timeit("flag_bubble_sort(rand_list)[:]", globals=globals(), number=100)}\n'
      f'Time for flag bubble sort. 100 elements: '
      f'{timeit("flag_bubble_sort(rand_list_2)[:]", globals=globals(), number=100)}\n'
      f'Time for flag bubble sort. 1000 elements: '
      f'{timeit("flag_bubble_sort(rand_list_3)[:]", globals=globals(), number=100)}\n')


"""
Сортировка без оптимизации увеличивается по времени работы с увеличением количества элементов. 
Сортировка с оптимизацией, аналогична сортировке без оптимизации, но время выполненения скоращается примерно вдвое, 
в сравнении с аналогичными условиями для сортировки без оптимизации. 
Сортировка с флагом (не повторять использование элемента, если он уже на своем месте) работает значительно быстрее двух
других вариантов сортировок. 

В целом, если использовать пузырьковую сортировку, то только с условием не повторять использование объекта, если он на
своем месте. 

Замеры:
Time for main bubble sort. 10 elements: 0.0006651580006291624
Time for main bubble sort. 100 elements: 0.0545012439997663
Time for main bubble sort. 1000 elements: 7.04544243700002
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Time for while bubble sort. 10 elements: 0.0004968020002706908
Time for while bubble sort. 100 elements: 0.03753244600011385
Time for while bubble sort. 1000 elements: 3.2023953450006957
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Time for flag bubble sort. 10 elements: 8.522999996785074e-05
Time for flag bubble sort. 100 elements: 0.0005913900004088646
Time for flag bubble sort. 1000 elements: 0.007098597998265177
"""
