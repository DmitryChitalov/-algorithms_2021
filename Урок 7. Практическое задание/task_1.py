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


# пузырковая сортировка
def buble_sort(enter_mas):
    long = len(enter_mas)
    while long > 0:
        for i in range(long):
            if i + 1 < long:
                if enter_mas[i] < enter_mas[i + 1]:
                    enter_mas[i], enter_mas[i + 1] = enter_mas[i + 1], enter_mas[i]
        long -= 1
    return enter_mas


# пузырковая сортировка 2
def buble_sort2(enter_mas):
    long = len(enter_mas)
    flag = True
    while flag:
        if long > 0:
            # если не будет перестановки, то нового цикла не будет
            flag = False
            for i in range(long):
                if i + 1 < long:
                    if enter_mas[i] < enter_mas[i + 1]:
                        enter_mas[i], enter_mas[i + 1] = enter_mas[i + 1], enter_mas[i]
                        # если была перестановка, то флаг на выполнение ещё одиного цикла
                        flag = True
            long -= 1
        else:
            break

    return enter_mas


n = 10
spam = [randint(-100, 100) for i in range(n)]
print(spam)
print(buble_sort(spam[:]))
print(buble_sort2(spam[:]))

# print(timeit("buble_sort([randint(-100, 100) for i in range(50)])", globals=globals(), number=100000))
# print(timeit("buble_sort2([randint(-100, 100) for i in range(50)])", globals=globals(), number=100000))
""" на небольших списках есть выигрыш по времени 5 - 10 %
список из 3 случайных элементов второй алгоритм чуть быстрее
buble_sort  = 3.376897104
buble_sort2 = 3.211471945
список из 4 случайных элементов второй алгоритм чуть быстрее
buble_sort  = 4.703201995
buble_sort2 = 4.315714155
список из 5 случайных элементов второй алгоритм чуть быстрее
buble_sort  = 5.9135
buble_sort2 = 5.6505
"""
