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


from random import randint
from timeit import timeit, default_timer


def time_it(func):
    def wrapper(numb):
        start_time = default_timer()
        func(numb)
        print(default_timer() - start_time)
    return wrapper


@time_it
def simple_bubble_sort(lst):
    for i in range(len(lst)-1):
        for j in range(len(lst)-i-1):
            if lst[j] < lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]


@time_it
def upgraded_bubble_sort(lst):
    for i in range(len(lst)-1):
        stop_flag = True
        for j in range(len(lst)-i-1):
            if lst[j] < lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                stop_flag = False
        if stop_flag:
            break


source_list = [randint(-100, 100) for _ in range(5000)]
sorted_list = source_list[:]
print("Неоптимизированная BubbleSort:")
simple_bubble_sort(sorted_list)
sorted_list = source_list[:]
print("Оптимизированная BubbleSort:")
upgraded_bubble_sort(sorted_list)

'''
Неоптимизированная BubbleSort:
2.5091845999999998
Оптимизированная BubbleSort:
2.3541432

Оптимизация позволяет не выполнять лишних итераций, когда список уже отсортирован. Данная оптимизация может 
привести к большому выигрышу по времени, если список частично отсортирован и самые большие элементы находятся в 
левой части списка, или никакого выигрыша не будет вообще, если наибольший элемент занимает последнюю позицию в списке.
В моем примере оптимизированный алгоритм сортирует быстрее, но не существенно (замер проводился на 5000 элементах в списке).
Сложность оптимизированного и неоптимизированного варианта одинаковая - O(n^2).
'''

#print(timeit("bubble_sort(", globals=globals(), number=1000))