"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Хотя в примерах к уроку уже есть вариант реализации слияния,
попробуйте предложить другой (придумать или найти)

И попытаться сделать замеры на массивах разной длины: 10, 100, 1000, ...

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""
from collections import defaultdict
import timeit
import random

def merge_sort(lst_obj):
    if len(lst_obj) > 1:
        center = len(lst_obj) // 2
        left = lst_obj[:center]
        right = lst_obj[center:]

        merge_sort(left)
        merge_sort(right)

        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lst_obj[k] = left[i]
                i += 1
            else:
                lst_obj[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            lst_obj[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            lst_obj[k] = right[j]
            j += 1
            k += 1
        return lst_obj

orig_list = [random.randint(0, 50) for _ in range(10)]
print(f"Random list with 10 elems via merge method: {orig_list}")
print(timeit.timeit("merge_sort(orig_list[:])", globals=globals(), number=1000))
print(f"Sorted list: {merge_sort(orig_list)}\n")

orig_list = [random.randint(0, 50) for _ in range(100)]
print(f"Random list with 100 elems via merge method: {orig_list}")
print(timeit.timeit("merge_sort(orig_list[:])", globals=globals(), number=1000))
print(f"Sorted list: {merge_sort(orig_list)}\n")

orig_list = [random.randint(0, 50) for _ in range(1000)]
print(f"Random list with 1000 elems via merge method: {orig_list}")
print(timeit.timeit("merge_sort(orig_list[:])", globals=globals(), number=1000))
print(f"Sorted list: {merge_sort(orig_list)}\n")

"""
Results: 
0.0197342 , 0.2648907, 3.6077425 
"""

# Сортировка Шелла
def shell_sort(lst_obj):
    center = len(lst_obj) // 2
    while center > 0:
        for i in range(len(lst_obj) - center):
            k = i
            while k >= 0 and lst_obj[k + center]:
                lst_obj[k], lst_obj[k + center] = lst_obj[k + center], lst_obj[k]
                k -= 1
        center //= 2
    return lst_obj

shell_list = [random.randint(0, 50) for _ in range(10)]
print(f"Random list with 10 elems via shell method: {shell_list}")
print(timeit.timeit("merge_sort(orig_list[:])", globals=globals(), number=1000))
print(f"Sorted list: {merge_sort(shell_list)}\n")

shell_list = [random.randint(0, 50) for _ in range(100)]
print(f"Random list with 100 elems via shell method: {shell_list}")
print(timeit.timeit("merge_sort(orig_list[:])", globals=globals(), number=1000))
print(f"Sorted list: {merge_sort(shell_list)}\n")

shell_list = [random.randint(0, 50) for _ in range(1000)]
print(f"Random list with 1000 elems via shell method: {shell_list}")
print(timeit.timeit("merge_sort(orig_list[:])", globals=globals(), number=1000))
print(f"Sorted list: {merge_sort(shell_list)}\n")

"""
Results: 
3.0649441000000004 , 3.1320540999999995, 3.205499100000001
Как можем увидеть с увеличением количества элементов незначительно возрастает время обработки. Как сравнение: метод на 
стыке 1000 элементов - > производительность у Шелла выше, чем у слияния.
"""

#сортировка подсчетом

def count_func(lst_obj):
    count_el = defaultdict(int)
    for i in lst_obj:
        count_el[i] += 1
    lst_obj = []
    while count_el:
        volm = min(count_el)
        for _ in range(count_el[volm]):
            lst_obj.append(volm)
        count_el.pop(min(count_el))
    return lst_obj

count_list = [random.randint(0, 50) for _ in range(10)]
print(f"Random list with 10 elems via count method: {count_list}")
print(timeit.timeit("merge_sort(orig_list[:])", globals=globals(), number=1000))
print(f"Sorted list: {merge_sort(count_list)}\n")

count_list = [random.randint(0, 50) for _ in range(100)]
print(f"Random list with 100 elems via count method: {count_list}")
print(timeit.timeit("merge_sort(orig_list[:])", globals=globals(), number=1000))
print(f"Sorted list: {merge_sort(count_list)}\n")

count_list = [random.randint(0, 50) for _ in range(1000)]
print(f"Random list with 1000 elems via count method: {count_list}")
print(timeit.timeit("merge_sort(orig_list[:])", globals=globals(), number=1000))
print(f"Sorted list: {merge_sort(count_list)}\n")

"""
Results: 
3.227633899999999, 3.2055389000000005, 3.1637552999999983
С увеличением количества элементов уменьшается скорость обработки функции. Как можем увидеть производительность у 
 метода подсчета выше, чем у слияния и Шелла
"""