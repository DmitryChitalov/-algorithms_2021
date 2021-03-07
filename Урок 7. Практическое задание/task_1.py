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
from timeit import timeit


def bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj) - n):
            if lst_obj[i] > lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        n += 1
    return lst_obj


def bubble_rev_sort(lst_obj):
    n = 0
    while n < len(lst_obj):
        sort = True
        for i in range(len(lst_obj) - 1, n, -1):
            if lst_obj[i] > lst_obj[i - 1]:
                lst_obj[i], lst_obj[i - 1] = lst_obj[i - 1], lst_obj[i]
                sort = False
        n += 1
        if sort:
            break
    return lst_obj


a = [random.randint(-100, 100) for _ in range(100)]
print('Выполнение без оптимизации', timeit('bubble_sort(a[:])', globals=globals(), number=100))
print('Выполнение c оптимизацией', timeit('bubble_rev_sort(a[:])', globals=globals(), number=100))

"""
Моя дороботка данного алгоритма заключается в проверке менялись ли хоть раз за проход числа в списке
если нет цикл прерывается, и сортировка идет по убыванию. Данная реализация в худшем варианте не дает ни какого 
прироста т.к. ей так же как и в обычном случае надо будет проделать столько же операций как и без дороботки
и она  выполняться даже чуть дольше. Но если допустим в какой-то из начальных проходов проходов по списку он уже 
является отсортировоным тогда цикл прекротится и не будет лишних проходов по уже отсортированому списку. Данное 
улучшение как может дать небольшой прирост скорости так и замедлить. Если брать худший вариант то данное улучшение 
не нужно т.к. вероятность лучшего варианта очень мала
"""
