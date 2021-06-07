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

# как в уроке, но по убыванию
def bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        n += 1
    return lst_obj


orig_list = [random.randint(-100, 100) for _ in range(10)]

print(orig_list)
print(bubble_sort(orig_list))


print(
    timeit.timeit(
        "bubble_sort(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [random.randint(-100, 100) for _ in range(100)]

# замеры 100
print(
    timeit.timeit(
        "bubble_sort(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [random.randint(-100, 100) for _ in range(1000)]

# замеры 1000
print(
    timeit.timeit(
        "bubble_sort(orig_list[:])",
        globals=globals(),
        number=1000))



"""
0.007448299999999998
0.7391278
80.6800633 - вышел быстрее чем в примере
"""
# с прерыванием, не уверен, но работает быстрее


def bubble_sort_while(lst_obj):
    n = 1
    counter = 0
    while n < len(lst_obj):
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
                counter += 1
        if not counter:
            break
        else:
            n += 1
    return lst_obj


test_list = [[100, 40, 20, 10, 9, 5, 4, 2, 1, -1, -4] for _ in range(10)]
print(test_list)
print(bubble_sort_while(test_list))

print(
    timeit.timeit(
        "bubble_sort_while(test_list[:])",
        globals=globals(),
        number=1000))

test_list = [[100, 40, 20, 10, 9, 5, 4, 2, 1, -1, -4] for _ in range(100)]

# замеры 100
print(
    timeit.timeit(
        "bubble_sort_while(test_list[:])",
        globals=globals(),
        number=1000))

test_list = [[100, 40, 20, 10, 9, 5, 4, 2, 1, -1, -4] for _ in range(1000)]

# замеры 1000
print(
    timeit.timeit(
        "bubble_sort_while(test_list[:])",
        globals=globals(),
        number=1000))

orig_list = [random.randint(-100, 100) for _ in range(10)]

print(orig_list)
print(bubble_sort_while(orig_list))


print(
    timeit.timeit(
        "bubble_sort_while(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [random.randint(-100, 100) for _ in range(100)]

# замеры 100
print(
    timeit.timeit(
        "bubble_sort_while(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [random.randint(-100, 100) for _ in range(1000)]

# замеры 1000
print(
    timeit.timeit(
        "bubble_sort_while(orig_list[:])",
        globals=globals(),
        number=1000))