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
# СДЕЛАТЬ 3 РЕАЛИЗАЦИИ:
# 1. сделать Пузырек по убыванию
# 2. сделать его умнее. если за проход по массиву не
# сове+ршается ни одной сортировки, то наш массив уже отсортирован, делаем break
# 3.убрать одну итерацию, когда последний элемент на своем месте (в конце списка справа).
# потом предпоследний, предпредпоследний...- по ним уже идти не нужно.
# КОГДПА ОЧЕРЕДНОЙ ЭЛЕМЕНТ ЗАНИМАЕТСВОЕ МЕСТО, НУЖНО ДЕЛАТЬ НА ОДНУ ИТЕРАЦИЮ МЕНЬШЕ
#  ПРОПИСАТЬ ЗДЕСЬ  -----       for i in range(len(lst_obj)-n):
#                                     if lst_obj[i] > lst_obj[i+1]:
#                                         lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
# 4. сделать замеры обоих реализаций и указать, получилась ли оптимизация -АНАЛИТИКА
import random
import timeit

# ORIGINAL_BUBBLE
orig_list = [random.randint(-100, 100) for _ in range(10)]
print(f'Исходный массив ', orig_list[:])


def original_bubble(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj) - n):
            if lst_obj[i] > lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        n += 1
    return lst_obj


print(f'Оригигальный пузырек', original_bubble(orig_list)[:])
print(f'Время его выполнения составило ',
      timeit.timeit(
          "original_bubble(orig_list[:])",
          globals=globals(),
          number=1000))


# ПУЗЫРЕК ПО УБЫВАНИЮ

def descending_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        n += 1
    return lst_obj


print(f'Пузырек по убыванию ', descending_sort(orig_list)[:])
print(f'Время его выполнения составило ',
      timeit.timeit(
          "descending_sort(orig_list[:])",
          globals=globals(),
          number=1000))


# ЕСЛИ ПУЗЫРЕК ОТСОРТИРОВАН

def is_sorted(lst_obj):
    n = 1
    while n < len(lst_obj):
        base_lst = lst_obj[:]
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        if lst_obj == sorted(base_lst, reverse=True):
            break
        n += 1
    return lst_obj


print(f'Если пузырек пузырек отсортирован', is_sorted(orig_list)[:])
print(f'Время его выполнения составило ',
      timeit.timeit(
          "is_sorted(orig_list[:])",
          globals=globals(),
          number=1000))


# МИНУС ЦИКЛ

def minus_iter(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj) - n):
            if i == len(lst_obj) - n:
                break
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        n += 1
    return lst_obj


print(f'Минус итерация', minus_iter(orig_list)[:])
print(f'Время его выполнения составило ',
      timeit.timeit(
          "is_sorted(orig_list[:])",
          globals=globals(),
          number=1000))

'''
РЕЗУЛЬТАТ:
1. Сортировка пузырька оригиральная от сортировки пузырька по убыванию не 
отличается ничем. Фактически, в условии if lst_obj[i] > lst_obj[i + 1] я всего 
лишь поменял знак сравнения '>' на '<'. 
2. В случае проверки на отсортированность списка в помощью встроенной 
функции сортировки на каждой итерации цикла while, в 4 раза уменьшилось время 
выполнения пузырька, т.к. уменьшилось количество ненужных действий, если объект 
уже отсортирован.
3. Уменьшение сортируемых элементов на один при каждом проходе цикла while
в 4 раза уменьшило время выполнения пузырька, т.к. уменьшилось количество 
сортируемых элементов.
ВЫВОД: Доработка на оптимизацию пузырька помогла, о чем говорят замеры времени.
'''
