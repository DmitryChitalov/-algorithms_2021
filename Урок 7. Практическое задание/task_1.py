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
from random import randint
import time


def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        if 'log_time' in kw:
            name = kw.get('log_name', method.__name__.upper())
            kw['log_time'][name] = int((te - ts) * 1000)
        else:
            print('%r  %2.2f ms' % \
                  (method.__name__, (te - ts) * 1000))
        return result

    return timed


@timeit
def bubble_sort(my_list_1):
    print(my_list_1)
    n = 1
    my_list = my_list_1[:]
    while n < len(my_list):
        for i in range(len(my_list) - n):
            if my_list[i] < my_list[i + 1]:
                my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
        n += 1
    return my_list


@timeit
def bubble_sort_2(my_list_1):
    print(my_list_1)
    n = 1
    my_list = my_list_1[:]
    while n < len(my_list):
        my_list_2 = my_list[:]
        for i in range(len(my_list) - n):
            if my_list[i] < my_list[i + 1]:
                my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
        if my_list_2 == my_list:
            return my_list
        n += 1
    return my_list


my_list = [randint(-100, 100) for i in range(1000)]
print(bubble_sort(my_list))
print(bubble_sort_2(my_list))
"""
Я доработал код допольнительной проверкой if и создавал копии массива, чтобы сравнить до итерации и после, чтобы понять
было изменение или нет.Моя дороботка не помогла, так как вероятность очень мала.
"""