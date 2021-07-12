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
def bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] > lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        n += 1
    return lst_obj

orig_list = [random.randint(-100, 100) for _ in range(100)]

def bubble_sort_1(lst_obj):
   n = len(lst_obj)
   b = False
   for j in range(n):
      for i in range(0, n-j-1):
         if lst_obj[i] < lst_obj[i + 1]:
            lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
            b = True
      if b == False:
         return lst_obj
   return lst_obj

def get_nums_1(end_num):
    res_list = [i for i in range(end_num + 1) if i % 10 == 0 or i % 10 == 0]
    return res_list

print(f'Исходный массив: {orig_list}\n'
      f'Без оптимизации. Отсортированный массив: {bubble_sort(orig_list)}\n'
      f'С оптимизацией. Отсортированный массив: {bubble_sort_1(orig_list)}')

print(f'Время выполнения массива без оптимизации',
    timeit.timeit(
        "bubble_sort(orig_list[:])",
        globals=globals(),
        number=1000))

print(f'Время выполнения массива c оптимизацией',
    timeit.timeit(
        "bubble_sort_1(orig_list[:])",
        globals=globals(),
        number=1000))

# Вывод: Идея оптимизации - завершение в случае если за проход по списку не совершается ни одной сортировки. При ее реализации
# время на выполнение кода значительно меньше, чем кода без этой оптимизации за счет сокращения бессмысленных итераций.