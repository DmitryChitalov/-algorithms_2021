"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы.

Сортировка должна быть реализована в виде функции.

Обязательно доработайте алгоритм (сделайте его умнее).

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение. Обязательно сделайте замеры времени обеих реализаций
и обосновать дала ли оптимизация эффективность

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию.

Сделайте выводы!!!
Опишите в чем была ваша доработка и помогла ли вам доработка??
"""
from random import randint
from timeit import timeit


def bobble(list_2):
    n = 1
    # ending = True
    while n < len(list_2):
        for i in range(len(list_2) - n):
            if list_2[i] < list_2[i + 1]:
                list_2[i], list_2[i + 1] = list_2[i + 1], list_2[i]
        #         ending = False
        # if ending:
        #     break
        n += 1
        # ending = True
    return list_2


def bobble1(list_1):
    n = 1
    ending = True
    while n < len(list_1):
        for i in range(len(list_1) - n):
            if list_1[i] < list_1[i + 1]:
                list_1[i], list_1[i + 1] = list_1[i + 1], list_1[i]
                ending = False
        if ending:
            break
        n += 1
        ending = True
    return list_1


print(bobble([randint(-100, 100) for _ in range(1000)]))
print(bobble1([randint(-100, 100) for _ in range(1000)]))

lst_1 = [randint(-100, 100) for _ in range(10)]
print('Old1:', timeit('bobble(lst_1[:])', globals=globals(), number=1000))
print('New1:', timeit('bobble1(lst_1[:])', globals=globals(), number=1000))
lst_1 = [randint(-100, 100) for _ in range(100)]
print('Old2:', timeit('bobble(lst_1[:])', globals=globals(), number=1000))
print('New2:', timeit('bobble1(lst_1[:])', globals=globals(), number=1000))
lst_1 = [randint(-100, 100) for _ in range(1000)]
print('Old3:', timeit('bobble(lst_1[:])', globals=globals(), number=1000))
print('New3:', timeit('bobble1(lst_1[:])', globals=globals(), number=1000))

# Old1: 0.006981700000000007
# New1: 0.006576100000000001
# Old2: 0.47233899999999995
# New2: 0.4583116999999999
# Old3: 48.9217422
# New3: 52.62251320000001

"""
Вывод: оптимизация не влияет на результат или даже ухудшает при большим количество данных в массивах
"""
