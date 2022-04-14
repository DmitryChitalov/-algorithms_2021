# Пузырьковая сортировка
from random import randint
from timeit import timeit





def bubble_sort(arr):
    """
        Сортировка по убыванию методом "пузырька"
    """
    n = len(arr)

    # Проходим через весь массив
    for i in range(n):

        # последний i-й элемент уже на своем месте
        for j in range(0, n - i - 1):

            # проходим массив от 0 до n-i-1
            # меняем местами если элемент
            # меньше слеудующего
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# Python3 Optimized implementation
# of Bubble sort

# An optimized version of Bubble Sort
def bubble_sort2(arr):
    n = len(arr)

    # Проходим через весь массив
    for i in range(n):
        swapped = False

        # Последние i элементы - уже на своих местах
        for j in range(0, n - i - 1):

            # проходим массив от 0 до n-i-1
            # меняем местами если элемент
            # меньше слеудующего
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # Если небыло обмена 2 соседних элементов
        # выходим из цикла
        if not swapped:
            break
    return arr


# Исходный массив
arr = [randint(-100, 100) for _ in range(100)]


print("Исходный массив:")
print(arr)

print("Отсортированный по убыванию:")
print(bubble_sort(arr[:]))
print("Выполнение функции bubble_sort занимает: ",timeit("bubble_sort(arr[:])", globals=globals(), number=100)," сек.")

print("Отсортированный по убыванию, модифицированный:")
print(bubble_sort2(arr[:]))
print("Выполнение функции bubble_sort2 занимает: ",timeit("bubble_sort2(arr[:])", globals=globals(), number=100)," сек.")

"""
Выполнение функции bubble_sort занимает:  0.3957794  сек.
Выполнение функции bubble_sort2 занимает:  0.3982362  сек.

Доработка функции не дала роста производительности.
Она состояла в прерывании циклаб в том месте где элементы уже отсортированы 
"""