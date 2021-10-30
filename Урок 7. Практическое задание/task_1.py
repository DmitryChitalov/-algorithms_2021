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
import random
import timeit


# Только отсортирован по убывынию
def bubble_sort_rev1(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj)-1, 0, -1):
            if lst_obj[i-1] > lst_obj[i]:
                lst_obj[i], lst_obj[i-1] = lst_obj[i-1], lst_obj[i]
        n += 1
    return lst_obj


# Помимо сортировки по убыванию, на каждой итерации исключает
# отсортированную часть словаря из дальнейшей сортировки
# Даёт прирост производительности примерно на треть
def bubble_sort_rev2(lst_obj):
    n = 1
    end_of_lst = 0
    while n < len(lst_obj):
        for i in range(len(lst_obj)-1, end_of_lst, -1):
            if lst_obj[i-1] > lst_obj[i]:
                lst_obj[i], lst_obj[i-1] = lst_obj[i-1], lst_obj[i]
        end_of_lst += 1
        n += 1
    return lst_obj


# Добавляет ко второму решению доработку в виде прерывания цикла, в случае, если
# за проход по списку не совершается ни одной сортировки
# Даёт прирост производительности по сравнению со вторым решением в случае, когда список
# близок к отсортированному состоянию (при рандоме сработало только на маленьких списках)
def bubble_sort_rev3(lst_obj):
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
# print(orig_list_10)
# print(bubble_sort_rev2(orig_list_10))
orig_list_100 = [random.randint(-100, 100) for _ in range(100)]
orig_list_1000 = [random.randint(-100, 100) for _ in range(1000)]


print(
    timeit.timeit(
        "bubble_sort_rev1(orig_list_10[:])",
        globals=globals(),
        number=1000))
print(
    timeit.timeit(
        "bubble_sort_rev2(orig_list_10[:])",
        globals=globals(),
        number=1000))
print(
    timeit.timeit(
        "bubble_sort_rev3(orig_list_10[:])",
        globals=globals(),
        number=1000))

print(
    timeit.timeit(
        "bubble_sort_rev1(orig_list_100[:])",
        globals=globals(),
        number=1000))
print(
    timeit.timeit(
        "bubble_sort_rev2(orig_list_100[:])",
        globals=globals(),
        number=1000))
print(
    timeit.timeit(
        "bubble_sort_rev3(orig_list_100[:])",
        globals=globals(),
        number=1000))


print(
    timeit.timeit(
        "bubble_sort_rev1(orig_list_1000[:])",
        globals=globals(),
        number=1000))
print(
    timeit.timeit(
        "bubble_sort_rev2(orig_list_1000[:])",
        globals=globals(),
        number=1000))
print(
    timeit.timeit(
        "bubble_sort_rev3(orig_list_1000[:])",
        globals=globals(),
        number=1000))

# 0.009578531000443036
# 0.9281126919995586
# 0.5635126490014954
# 0.6178539870015811
# 95.92789458400148
# 66.91305277799984
# 70.77575181900102
