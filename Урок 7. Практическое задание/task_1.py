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
import random
import timeit


# скрипт без доработки
def bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        n += 1
    return lst_obj


orig_list = [random.randint(-100, 100) for _ in range(10)]
print(f'Исходный список bubble_sort - {orig_list}')
print(f'Отсортированный список bubble_sort - {bubble_sort(orig_list)}')


# скрипт с доработкой
def bubble_sort_2(lst_obj):
    n = 1
    while n < len(lst_obj):
        flag = True
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
                flag = False
        if flag:
            break
        n += 1
    return lst_obj


orig_list = [random.randint(-100, 100) for _ in range(10)]
print(f'Исходный список bubble_sort_2 - {orig_list}')
print(f'Отсортированный список bubble_sort_2 - {bubble_sort_2(orig_list)}')

"""
ЗАМЕРЫ
"""
orig_list_10 = [random.randint(-100, 100) for _ in range(10)]
print(f'10 элементов bubble_sort - '
      f'{timeit.timeit("bubble_sort(orig_list_10[:])",globals=globals(), number=1000)}')
print(f'10 элементов bubble_sort_2 - '
      f'{timeit.timeit("bubble_sort_2(orig_list_10[:])",globals=globals(), number=1000)}')

orig_list_100 = [random.randint(-100, 100) for _ in range(100)]
print(f'100 элементов bubble_sort - '
      f'{timeit.timeit("bubble_sort(orig_list_100[:])",globals=globals(), number=1000)}')
print(f'100 элементов bubble_sort_2 - '
      f'{timeit.timeit("bubble_sort_2(orig_list_100[:])",globals=globals(), number=1000)}')

orig_list_1000 = [random.randint(-100, 100) for _ in range(1000)]
print(f'1000 элементов bubble_sort - '
      f'{timeit.timeit("bubble_sort(orig_list_1000[:])",globals=globals(), number=1000)}')
print(f'1000 элементов bubble_sort_2 - '
      f'{timeit.timeit("bubble_sort_2(orig_list_1000[:])",globals=globals(), number=1000)}')

"""
10 элементов bubble_sort - 0.007412000000000002
10 элементов bubble_sort_2 - 0.0057853
100 элементов bubble_sort - 0.6612747000000001
100 элементов bubble_sort_2 - 0.7773409000000001
1000 элементов bubble_sort - 73.46996779999999
1000 элементов bubble_sort_2 - 80.60540069999999

Моя доработка заключалась в том, что я добавил флаг, с помощью которого цикл будет досрочно прерываться,
если список изначально был отсортирован,что сэкономит время выполнения функции. Однако, вероятность получения
заранее отсортированного списка крайне мала, а время выполнения обоих функций примерно равно (в случае с 
длинными списками доработанная функция отработала даже медленее), то практического смысла в данной доработке не было.
"""
