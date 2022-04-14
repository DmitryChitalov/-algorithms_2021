import random
import timeit


def sort_by_bubble(lst):
    n = 1
    while n < len(lst):
        for i in range(len(lst)-n):
            if lst[i] < lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
        n += 1
    return lst

def sort_by_bubble_updated(lst):
    n = 1
    while n < len(lst):
        marker = True
        for i in range(len(lst)-n):
            if lst[i] < lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
                marker = False
        if marker:
            break
        n += 1
    return lst


new_list = [random.randint(-100, 100) for i in range(1000)]
print(f"Исходный список: {new_list}")
print(f"Результат первой функции без улучшений: {sort_by_bubble(new_list)}")
print(f"Результат второй функции с улучшениями: {sort_by_bubble_updated(new_list)}")
print(timeit.timeit("sort_by_bubble(new_list)", globals=globals(), number=100))
print(timeit.timeit("sort_by_bubble_updated(new_list)", globals=globals(), number=100))

"""Вот результаты измерений:
4.8517906
4.8780227

Можно заметить, что результаты почти идентичны, а значит в большинстве случаев 
(не отсортированный заранее массив) в доработке нет необходимости.
"""