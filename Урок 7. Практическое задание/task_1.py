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
import random
import timeit
'''
Sort descending.

Сортировка по убывынию.
'''
def bubble_sort_1(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj)-1, 0, -1):
            if lst_obj[i-1] > lst_obj[i]:
                lst_obj[i], lst_obj[i-1] = lst_obj[i-1], lst_obj[i]
        n += 1
    return lst_obj

'''
Descending sorting + is eliminated at each iteration
sorted part of the dictionary from further sorting
Gives a performance increase of 30%.

Сортировка по убыванию + на каждой итерации исключается
отсортированная часть словаря из дальнейшей сортировки
Даёт прирост производительности  на 30%.
'''

def bubble_sort_2(lst_obj):
    n = 1
    end_of_lst = 0
    while n < len(lst_obj):
        for i in range(len(lst_obj)-1, end_of_lst, -1):
            if lst_obj[i-1] > lst_obj[i]:
                lst_obj[i], lst_obj[i-1] = lst_obj[i-1], lst_obj[i]
        end_of_lst += 1
        n += 1
    return lst_obj

'''
Added loop interruption if no sorting is performed during the pass
Gives a performance increase compared to the second solution in the case when the list
close to sorted state or on small lists.

Добавлено прерывание цикла, в  случае, если за проход не совершается ни одной сортировки
Даёт прирост производительности по сравнению со вторым решением в случае, когда список
близок к отсортированному состоянию или на небольших списках. на больших списках
преимуществ нет.
'''
def bubble_sort_3(lst_obj):
    n = 1
    end_of_lst = 0
    while n < len(lst_obj):
        break_counter = 1
        for i in range(len(lst_obj)-1, end_of_lst, -1):
            if lst_obj[i-1] > lst_obj[i]:
                lst_obj[i], lst_obj[i-1] = lst_obj[i-1], lst_obj[i]
                break_counter -= 1
        if break_counter == 1:
            return lst_obj
        end_of_lst += 1
        n += 1
    return lst_obj


orig_list_10 = [random.randint(-100, 100) for _ in range(10)]
print(f'Original list, non sorted: {orig_list_10}')
print(f'Buble sorted: {bubble_sort_2(orig_list_10)}')
orig_list_100 = [random.randint(-100, 100) for _ in range(100)]
orig_list_1000 = [random.randint(-100, 100) for _ in range(1000)]


print(
    timeit.timeit(
        "bubble_sort_1(orig_list_10[:])",
        globals=globals(),
        number=1000))
print(
    timeit.timeit(
        "bubble_sort_2(orig_list_10[:])",
        globals=globals(),
        number=1000))
print(
    timeit.timeit(
        "bubble_sort_3(orig_list_10[:])",
        globals=globals(),
        number=1000))

print(
    timeit.timeit(
        "bubble_sort_1(orig_list_100[:])",
        globals=globals(),
        number=1000))
print(
    timeit.timeit(
        "bubble_sort_2(orig_list_100[:])",
        globals=globals(),
        number=1000))
print(
    timeit.timeit(
        "bubble_sort_3(orig_list_100[:])",
        globals=globals(),
        number=1000))


print(
    timeit.timeit(
        "bubble_sort_1(orig_list_1000[:])",
        globals=globals(),
        number=1000))
print(
    timeit.timeit(
        "bubble_sort_2(orig_list_1000[:])",
        globals=globals(),
        number=1000))
print(
    timeit.timeit(
        "bubble_sort_3(orig_list_1000[:])",
        globals=globals(),
        number=1000))


"""
C:\Users\79115\AppData\Local\Programs\Python\Python39\python.exe "C:/Users/79115/Desktop/2 Урок Алгоритмы/Урок 2. Коды примеров/Algorithm7.1.py"
Original list, non sorted: [-15, -39, 63, 77, 1, 33, 99, 89, -73, -91]
Buble sorted: [-91, -73, -39, -15, 1, 33, 63, 77, 89, 99]
0.007960099999999998
0.006253700000000001
0.0011265000000000025

0.8322575
0.49139960000000005
0.5155642999999999

92.2075096
62.4448524
68.27973020000002

Process finished with exit code 0

"""
