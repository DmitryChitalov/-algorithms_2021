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
import timeit
import random

# с прерыванием, поменял знак(направление) перебора, плюс с помощью счетчика делаем отсечку,
# если счетчик не срабатывает, прерываем.
# подобный вариант не ускоряет процесс сортировки, что показывает его ненужность
# 99.4848441

def bubble_sort_while(lst_obj):
    n = 1
    counter = 0
    while n < len(lst_obj):
        for el in range(len(lst_obj) - n):
            if lst_obj[el] < lst_obj[el + 1]:
                lst_obj[el], lst_obj[el + 1] = lst_obj[el + 1], lst_obj[el]
            counter += 1
        if not counter:
            break
        else:
            n += 1
    return lst_obj


orig_list1 = [random.randint(-100, 100) for _ in range(1000)]

# замеры 1000
print(
    timeit.timeit(
        "bubble_sort_while(orig_list1[:])",
        globals=globals(),
        number=1000))

print(orig_list1)
print(bubble_sort_while(orig_list1))
"""
вот такой еще вариант сделал, еще одно условие добавил
(предположил, что данным условием смогу прервать пробег по массиву),
был еще вариант тестовый, но удалил, после каунтера и забыл, что написал там, вроде работал((
и вот этот доработанный товарищ так же не ускоряет процесс, смысла в нем тоже нет.
100.3172292
"""
def bubble_sort_upgrade(lst_obj):
    i = 1
    while i < len(lst_obj):
        for el in range(len(lst_obj) - i):
            if lst_obj[el] < lst_obj[el + 1]:  # знак
                lst_obj[el], lst_obj[el + 1] = lst_obj[el + 1], lst_obj[el]
                if lst_obj[el] == lst_obj[el + 1]:  # предположил, что данным условием смогу прервать пробег по массиву
                    break
        else:
            i += 1
    return lst_obj


orig_list = [random.randint(-100, 100) for _ in range(1000)]


# замеры 1000
print(
    timeit.timeit(
        "bubble_sort_upgrade(orig_list[:])",
        globals=globals(),
        number=1000))

print(orig_list)
print(bubble_sort_upgrade(orig_list))
