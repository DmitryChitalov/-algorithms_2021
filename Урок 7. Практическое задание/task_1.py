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

MIN_NUMBER = -100
MAX_NUMBER = 100
LIST_LENGHT = 100

def time_decor(func):
    def wrapper(*args, **kwargs):
        start_time = default_timer()
        result = func(*args, **kwargs)
        print(f'Время выполнения: {default_timer() - start_time}')
        return result
    return wrapper

def is_sorted(lst, key=lambda x: x):
    """
    Проверка отсортирован ли список
    :param lst: несортированный список
    :return:
    """
    for i, el in enumerate(lst[1:]):
        if key(el) > key(lst[i]):
            return False
    return True


@time_decor
def buble_sorting(list):
    if is_sorted(list):
        return list
    for i in range(len(list) - 1):
        for j in range(i + 1, len(list)):
            if list[j] > list[i]:
                list[j], list[i] = list[i], list[j]
    return list

my_list = [randint(MIN_NUMBER, MAX_NUMBER) for _ in range(LIST_LENGHT)]

my_sorted_list = list(range(LIST_LENGHT, 0, -1))


print(f'Случайно сгенерированный список: {my_list}')
print(f'Список отсортированный "пузырьком": {buble_sorting(my_list[:])}')

print(f'Список сгенерированный отсортированным: {my_sorted_list}')
print(f'Отсортированный список подвергшийся сортировке: {buble_sorting(my_sorted_list[:])}')

"""
Функция is_sorted проверяет отсортирован ли список. Если да, buble_sorting не выполняется
is_sorted имеет смысл только на очень маленьких значениях длины списка (где и оптимизировать смысла нет), 
т.к. при увеличении длины, вероятность получить несортированный список вырастает по экспоненте,
т.е. шанс получения уже отсортированного списка ничтожно мал.
"""
