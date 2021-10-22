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
import timeit


def bubble_sort(li):
    n = 1
    while n < len(li):
        for i in range(len(li) - 1):
            if li[i] < li[i + 1]:
                li[i], li[i + 1] = li[i + 1], li[i]
        n += 1
    return li


def bubble_sort_check(li):
    n = 1
    check = True
    while n < len(li):
        if n == 2 and check:
            break
        for i in range(len(li) - 1):
            if li[i] < li[i + 1] and n == 1:
                check = False
                li[i], li[i + 1] = li[i + 1], li[i]
            elif li[i] < li[i + 1]:
                li[i], li[i + 1] = li[i + 1], li[i]
        n += 1
    return li


# длина списка 10
d = [randint(-100, 100) for _ in range(10)]
# исходный спссок
print(d)
# отсортированный список
print(bubble_sort(d))

# замеры на несортированном списке
print(timeit.timeit('bubble_sort(d[:])', globals=globals(), number=100))
print(timeit.timeit('bubble_sort_check(d[:])', globals=globals(), number=100))

# замеры на сортированном списке
d = sorted(d, reverse=True)
print(timeit.timeit('bubble_sort(d[:])', globals=globals(), number=100))
print(timeit.timeit('bubble_sort_check(d[:])', globals=globals(), number=100))

# длина списка 100
d = [randint(-100, 100) for _ in range(100)]
print(d)

# замеры на несортированном списке
print(timeit.timeit('bubble_sort(d[:])', globals=globals(), number=100))
print(timeit.timeit('bubble_sort_check(d[:])', globals=globals(), number=100))

# замеры на сортированном списке
d = sorted(d, reverse=True)
print(timeit.timeit('bubble_sort(d[:])', globals=globals(), number=100))
print(timeit.timeit('bubble_sort_check(d[:])', globals=globals(), number=100))

# длина списка 1000
d = [randint(-100, 100) for _ in range(1000)]
print(d)

# # замеры на несортированном списке
print(timeit.timeit('bubble_sort(d[:])', globals=globals(), number=100))
print(timeit.timeit('bubble_sort_check(d[:])', globals=globals(), number=100))

# замеры на сортированном списке
d = sorted(d, reverse=True)
print(timeit.timeit('bubble_sort(d[:])', globals=globals(), number=100))
print(timeit.timeit('bubble_sort_check(d[:])', globals=globals(), number=100))

'''Выполнил доработку скрипта, создал переменную check для проверки сортировки списка
на первом цикле. Если сортировки на первом цикле не было то список уже отсартирован и нужно выходить из цикла.
Результаты замеров при длине = 10:  bubble_sort(d[:])         0.003028045
                                    bubble_sort_check(d[:])   0.004674598
                   отсортированный спсисок                 
                   при длине = 10:  bubble_sort(d[:])         0.002768456
                                    bubble_sort_check(d[:])   0.000451117

                   при длине = 100: bubble_sort(d[:])         0.240167756
                                    bubble_sort_check(d[:])   0.488567388
                   отсортированный спсисок 
                   при длине = 100: bubble_sort(d[:])         0.163427157
                                    bubble_sort_check(d[:])   0.004838370
                   
                   при длине = 1000: bubble_sort(d[:])         25.6636363
                                     bubble_sort_check(d[:])   41.7342985
                   отсортированный спсисок 
                   при длине = 1000: bubble_sort(d[:])         17.1931960
                                     bubble_sort_check(d[:])   0.03753347
Вывод: Если список заведомо отсортирован, что врятли, то на длине массива = 10 видно что функция с доработкой имеет 
       приймущество примерно в 5 раз, а с увилечением массива разница во временни выполнения функций становится 
       еще больще! Ну а если на вход получаем рандомный массив то функция с доработкой выполняется дольше 
       примерно в 2 раза.
       В общем, я бы не стал использовать доработанную функцию в данной реализвции.'''
