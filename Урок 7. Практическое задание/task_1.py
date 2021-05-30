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


from timeit import timeit
from memory_profiler import profile
from random import randint


def bubble_sort(nums):
    i = 1
    while i < len(nums):
        for j in range(len(nums) - i):
            if nums[j] < nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

        i += 1
    return nums


def upgrade_bubble_sort(nums):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True
    return nums


random_list_of_nums = [randint(-100, 99) for _ in range(100)]
print(f'Исходный: {random_list_of_nums}')
print(f'Пузырек: {bubble_sort(random_list_of_nums[:])}')
print(f'Upgrade: {upgrade_bubble_sort(random_list_of_nums[:])}\n')


@profile
def bubble_sort_profile(list_obj):
    bubble_sort(list_obj)


@profile
def upgrade_bubble_sort_profile(list_obj):
    upgrade_bubble_sort(list_obj)


print('Профилировка памяти:')
print('Пузырек')
bubble_sort_profile(random_list_of_nums[:])

print('Upgrade')
upgrade_bubble_sort_profile(random_list_of_nums[:])

print('\nЗамеры времени:')
print(f"Пузырек: {timeit('bubble_sort(random_list_of_nums[:])', number=1000, globals=globals())}")
print(f"Upgrade: {timeit('upgrade_bubble_sort(random_list_of_nums[:])', number=1000, globals=globals())}")

'''
Замеры показывают, что добавление условия не привело к оптимизации.
Ускорение может быть только в единственном случае, когда на вход алгоритму дается уже отсортированный список.
'''
