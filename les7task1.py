import random
import timeit

#Обычный вариант сортировки списка
def sort_by_bubble(lst):
    n = 1
    while n < len(lst):
        for i in range(len(lst)-n):
            if lst[i] < lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
        n += 1
    return lst

#Улучшенный вариант. Получается в процессе выполнения программы
#отсортированная часть словаря исключается из дальнейшей
#сортировки, что дает прирост производительности. Так же если
#За проход по циклу нет ни одной сортировки (точнее не совершается
#ни одна сортировка), то происходит прерывание цикла.
def sort_by_bubble_updated(lst):
    n = 1
    end_of_list = 0
    while n < len(lst):
        break_count = 1
        for i in range(len(lst)-n):
            if lst[i] < lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
                break_count -= 1
        if break_count == 1:
            return lst
        end_of_list += 1
        n += 1
    return lst


new_list_10 = [random.randint(-100, 100) for _ in range(10)]
# print(orig_list_10)
# print(bubble_sort_rev2(orig_list_10))
new_list_100 = [random.randint(-100, 100) for _ in range(100)]
new_list_1000 = [random.randint(-100, 100) for _ in range(1000)]
print(timeit.timeit("sort_by_bubble(new_list_10[:])", globals=globals(), number=100))
print(timeit.timeit("sort_by_bubble_updated(new_list_10[:])", globals=globals(), number=100))
print(timeit.timeit("sort_by_bubble(new_list_100[:])", globals=globals(), number=100))
print(timeit.timeit("sort_by_bubble_updated(new_list_100[:])", globals=globals(), number=100))
print(timeit.timeit("sort_by_bubble(new_list_1000[:])", globals=globals(), number=100))
print(timeit.timeit("sort_by_bubble_updated(new_list_1000[:])", globals=globals(), number=100))

"""Вот результаты измерений:
0.0008741000000000027
0.0008998000000000027
0.048070100000000004
0.050131999999999996
4.9409336
5.5837338
"""