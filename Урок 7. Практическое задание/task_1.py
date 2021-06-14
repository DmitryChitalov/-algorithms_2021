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
from timeit import timeit

random_list = [randint(-100, 100) for _ in range(20)]
test_list = sorted(random_list)
test_list.reverse()


def bubble_sort_1(lst):
    for i in range(len(lst) - 1):
        for j in range(len(lst) - i - 1):
            if lst[j] < lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst


def bubble_sort_2(lst):
    swap = False
    for i in range(len(lst) - 1):
        for j in range(len(lst) - i - 1):
            if lst[j] < lst[j + 1]:
                swap = True
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
        if not swap:
            return lst
    return lst


print(random_list)
print(bubble_sort_1(random_list[:]))
print(bubble_sort_2(random_list[:]))

print("Время сортировки до доработки")
print(timeit("bubble_sort_1(random_list[:])", globals=globals(), number=10000))
print("Время сортировки после доработки")
print(timeit("bubble_sort_2(random_list[:])", globals=globals(), number=10000))
print("Время сортировки отсортированного массива")
print(timeit("bubble_sort_2(test_list[:])", globals=globals(), number=10000))


"""
Доработка дает оптимизацию только в том случае, когда на вход функции подается отсортированный массив,
то есть наша функция ничего не делает, кроме проверки всех элементов.
Вероятность построить рандомно отсортированный список из большого количества элементов ничтожно мала, 
поэтому доработка в данном случае бесполезна.
"""