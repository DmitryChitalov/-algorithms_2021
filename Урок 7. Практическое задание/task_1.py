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
from random import randint

N = 100
a = []
for i in range(N):
    a.append(randint(-100, 99))

 
def sort_example(num):
    for i in range(len(num)):
        for j in range(len(num)-i-1):
            if num[j] < num[j+1]:
                num[j], num[j+1] = num[j+1], num[j]
    return num

def sort_example_smart(num):
    stop = 0
    for i in range(len(num)):
        for j in range(len(num)-1):
            if num[j] < num[j+1]:
                num[j], num[j+1] = num[j+1], num[j]
                stop = 1
        if stop == 0:
            break
    return num 
 
print(f"Текущий массив {a}")
print(timeit.timeit("sort_example(a)",
                    setup="from __main__ import sort_example, a", number=100))
print(timeit.timeit("sort_example_smart(a)",
                    setup="from __main__ import sort_example_smart, a", number=100))
# Выполнение скрипта намного быстрее, мы не идём до конца, а прекращаем как только наше текущее знаечени перестаёт быть меньше следующего

