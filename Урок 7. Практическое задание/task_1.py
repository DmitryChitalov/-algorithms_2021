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

import random
from memory_profiler import profile, memory_usage
from timeit import default_timer


def decor(func):
    """Функция декортатор для замеров времени и памяти"""

    def wrapper(*args, **kwargs):
        t1 = default_timer()
        m1 = memory_usage()
        res = func(args[0])
        m2 = memory_usage()
        t2 = default_timer()
        mem_diff = m2[0] - m1[0]
        time_dif = t2 - t1
        print(f'Функция - {func.__name__}\n Время заняло: {time_dif}\n Памяти заняло:{mem_diff}\n\n')
        return res

    return wrapper


@decor
def bubble(rand_list):
    n = 1
    while n < len(rand_list):
        for i in range(len(rand_list) - n):
            if rand_list[i] > rand_list[i + 1]:
                rand_list[i], rand_list[i + 1] = rand_list[i + 1], rand_list[i]
        n += 1
    return rand_list


@decor
def bubble_revert(rand_list):
    n = len(rand_list)
    while n > 1:
        for i in range(len(rand_list) - 1, len(rand_list) - n, -1):
            if rand_list[i] < rand_list[i - 1]:
                rand_list[i], rand_list[i - 1] = rand_list[i - 1], rand_list[i]
        n -= 1
    return rand_list


@decor
def bubble_revert_mod(rand_list):
    n = len(rand_list)
    while n > 1:
        flag = 0
        for i in range(n - 1):
            if rand_list[i] > rand_list[i + 1]:  # Проверка необходимости сортировки
                flag = 1
        if flag == 0:
            break
        for i in range(len(rand_list) - 1, len(rand_list) - n, -1):
            if rand_list[i] < rand_list[i - 1]:
                rand_list[i], rand_list[i - 1] = rand_list[i - 1], rand_list[i]
        n -= 1
    return rand_list


print('Замеры 10\n')
rand_list = [random.randint(-100, 100) for _ in range(10)]
bubble(rand_list[:])
bubble_revert(rand_list[:])
bubble_revert_mod(rand_list)[:]
print('/*'*30+'\n')
print('Замеры 100\n')
rand_list2 = [random.randint(-100, 100) for _ in range(100)]
bubble(rand_list2[:])
bubble_revert(rand_list2[:])
bubble_revert_mod(rand_list2[:])
print('/*'*30+'\n')
print('Замеры 1000\n')
rand_list3 = [random.randint(-100, 100) for _ in range(1000)]
bubble(rand_list3[:])
bubble_revert(rand_list3[:])
bubble_revert_mod(rand_list3[:])


"""
Замеры 10

Функция - bubble
 Время заняло: 0.2010592
 Памяти заняло:0.0078125

Функция - bubble_revert
 Время заняло: 0.20093179999999994
 Памяти заняло:0.0

Функция - bubble_revert_mod
 Время заняло: 0.2010599999999999
 Памяти заняло:0.0

/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*
Замеры 100

Функция - bubble
 Время заняло: 0.20092140000000014
 Памяти заняло:0.0

Функция - bubble_revert
 Время заняло: 0.20112490000000016
 Памяти заняло:0.0

Функция - bubble_revert_mod
 Время заняло: 0.20200180000000012
 Памяти заняло:0.0


/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*

Замеры 1000

Функция - bubble
 Время заняло: 0.27440549999999986
 Памяти заняло:0.0

Функция - bubble_revert
 Время заняло: 0.29199149999999974
 Памяти заняло:0.0

Функция - bubble_revert_mod
 Время заняло: 0.3024701999999997
 Памяти заняло:0.0
 
 Доработка - добавление флага, который принимает значение 1, в случае, если необходима сортировка 
 и значение 0 если в сортировке нет необходимости.
 В модицикации нет особого смыла, т.к. быстрее модийицированная функция будет отрабатывать только в 
 случае уже отсортированного словаря
"""