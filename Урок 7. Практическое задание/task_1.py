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
from random import randint
from timeit import default_timer
from memory_profiler import memory_usage


def decor(func):
    def wrapper(*args, **kwargs):
        start = default_timer()
        result = func(*args, **kwargs)
        print(f'Время выполнения: {default_timer() - start}')
        return result

    return wrapper


def is_sorted(lst, key=lambda x: x):
    for i, el in enumerate(lst[1:]):
        if key(el) > key(lst[i]):
            return False
    return True


@decor
def buble_sort(list):
    if is_sorted(list):
        return list
    for i in range(len(list) - 1):
        for j in range(i + 1, len(list)):
            if list[j] > list[i]:
                list[j], list[i] = list[i], list[j]
    return list

# Создаем не отсортированный список
my_list = [randint(-100,100) for i in range(1000)]

# Создаем отсортированный список
my_sort_list = list(range(1000, 0, -1))


print(my_list)
print(buble_sort(my_list[:]))

print(my_sort_list)
print(buble_sort(my_sort_list[:]))

"""
Вывод: я написал функцию (is_sorted), которая проверяет отсортирован ли список.
Далее функцию сортировки пузырьком с проверкой, отсортирован ли список.
Как и ожидалось доработка очень полезная, т.к. при отсорированном списке будет O(n) вместо O(n**2).
"""