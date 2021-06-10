from timeit import timeit
from statistics import median
import random

amount = input('Введите количество элементов: ')
while not amount.isdigit() or not int(amount):
    amount = input('Неверный ввод!\n Повторите ввод количества элементов: ')
m = int(amount) * 2 + 1
my_list = [random.randint(0, m * 50) for _ in range(m)]
copy_list = my_list[:]
print('Исходный массив:', my_list)


median(copy_list)


def median_1(lst):
    indicator, remainder = divmod(len(lst), 2)
    if remainder:
        return sorted(lst)[indicator]
    return sum(sorted(lst)[indicator - 1:indicator + 1]) / 2


def median_2(lst):
    sorted_lst = sorted(lst)
    length = len(lst)
    index = (length - 1) // 2
    if length % 2:
        return sorted_lst[index]
    else:
        return (sorted_lst[index] + sorted_lst[index + 1]) / 2.0


def median_3(lst):
    lst.sort()
    mid = len(lst) // 2
    return (lst[mid] + lst[mid]) / 2


print(f"Медиана: {median_1(copy_list)}")
print(f"Медиана: {median_2(copy_list)}")
print(f"Медиана: {median_3(copy_list)}")
