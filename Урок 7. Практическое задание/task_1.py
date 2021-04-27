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
import timeit
import random


def benchmark(func):
    def wrapper(*args, **kwargs):
        n = 100
        time = 0
        for _ in range(n):
            start_timer = timeit.default_timer()
            result = func(*args, **kwargs)
            time += timeit.default_timer() - start_timer
        print(f' *** Общее время выполнения {func} - {time} сек.')
        return result
    return wrapper


def bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        n += 1

    return lst_obj, n - 1


def bubble_sort_opt(lst_obj):
    n = 1
    while n < len(lst_obj):
        stop = True
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
                stop = False
        if stop:
            break
        n += 1
    return lst_obj, n


orig_list = [random.randint(-100, 100) for _ in range(10)]

print('\n\n*** Сортировка списка из 10 элементов ***\n')

result_10 = bubble_sort(orig_list[:])
print(f'bubble_sort: {result_10[0]},\n  Количество проходов: {result_10[1]}')

print('  Время выполнения bubble_sort (10 элементов): ',
      timeit.timeit(
          "bubble_sort(orig_list[:])",
          globals=globals(),
          number=100))

result_10 = bubble_sort_opt(orig_list[:])
print(f'bubble_sort_opt: {result_10[0]},\n  Количество проходов: {result_10[1]}')

print('  Время выполнения bubble_sort_opt (10 элементов): ',
      timeit.timeit(
          "bubble_sort_opt(orig_list[:])",
          globals=globals(),
          number=100))

orig_list = [random.randint(-100, 100) for _ in range(100)]

print('\n\n*** Сортировка списка из 100 элементов ***\n')

result_100 = bubble_sort(orig_list[:])
print(f'bubble_sort: {result_100[0]},\n  Количество проходов: {result_100[1]}')

print('  Время выполнения bubble_sort (100): ',
      timeit.timeit(
          "bubble_sort(orig_list[:])",
          globals=globals(),
          number=100))

result_100 = bubble_sort_opt(orig_list[:])
print(f'bubble_sort_opt: {result_100[0]}\n  Количество проходов: {result_100[1]}')

print('  Время выполнения bubble_sort_opt (100): ',
      timeit.timeit(
          "bubble_sort_opt(orig_list[:])",
          globals=globals(),
          number=100))

orig_list = [random.randint(-100, 100) for _ in range(1000)]

print('\n\n*** Сортировка списка из 1000 элементов ***\n')

result_1000 = bubble_sort(orig_list[:])
print(f'bubble_sort: {result_1000[0]}\n  Количество проходов: {result_1000[1]}')

print('  Время выполнения bubble_sort (1000): ',
      timeit.timeit(
          "bubble_sort(orig_list[:])",
          globals=globals(),
          number=100))

result_1000 = bubble_sort_opt(orig_list[:])
print(f'bubble_sort_opt: {result_1000[0]}\n  Количество проходов: {result_1000[1]}')

print('  Время выполнения bubble_sort_opt (1000): ',
      timeit.timeit(
          "bubble_sort_opt(orig_list[:])",
          globals=globals(),
          number=100))

bubble_sort_opt(orig_list)

print('Отсортированный массив:\n')
result_1000 = bubble_sort_opt(orig_list[:])
print(f'bubble_sort_opt: {result_1000[0]}\n  Количество проходов: {result_1000[1]}')

print('  Время выполнения bubble_sort_opt (1000): ',
      timeit.timeit(
          "bubble_sort_opt(orig_list[:])",
          globals=globals(),
          number=100))

"""

Результаты замеров:

*** Сортировка списка из 10 элементов ***

bubble_sort: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
  Количество проходов: 9
  Время выполнения bubble_sort (10 элементов):  0.000986464999999992
bubble_sort_opt: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
  Количество проходов: 10
  Время выполнения bubble_sort_opt (10 элементов):  0.0010143750000000118


*** Сортировка списка из 100 элементов ***

bubble_sort: [100, 99, 97, 96, 96, 96, 92, 91, 89, 88, 84, 84, 82, 79, 75, 72, 71, 69, 64, 64, 62, 62, 61, 60, 60, ...]
  Количество проходов: 99
  Время выполнения bubble_sort (100):  0.05863901199999999
bubble_sort_opt: [100, 99, 97, 96, 96, 96, 92, 91, 89, 88, 84, 84, 82, 79, 75, 72, 71, 69, 64, 64, 62, 62, 61, 60, ...]
  Количество проходов: 83
  Время выполнения bubble_sort_opt (100):  0.058181228


*** Сортировка списка из 1000 элементов ***

bubble_sort: [100, 100, 100, 99, 99, 99, 99, 98, 98, 98, 98, 98, 98, 98, 97, 97, 97, 97, 97, 97, 97, 97, 97, 96, ...] 
  Количество проходов: 999
  Время выполнения bubble_sort (1000):  6.451883122
bubble_sort_opt: [100, 100, 100, 99, 99, 99, 99, 98, 98, 98, 98, 98, 98, 98, 97, 97, 97, 97, 97, 97, 97, 97, 97, ...]
  Количество проходов: 966
  Время выполнения bubble_sort_opt (1000):  6.410790677


*** Отсортированный массив: ***

bubble_sort_opt:
[100, 100, 100, 99, 99, 99, 99, 98, 98, 98, 98, 98, 98, 98, 97, 97, 97, 97, 97, 97, 97, 97, 97, 96, 96, 96, 96, ...]
 Количество проходов: 1
Время выполнения bubble_sort_opt (1000):  0.006638668999999098


Выводы: 

В основе алгоритма сортировки пузырьковым методом лежит многократный проход по массиву.
Для оптимизации алгоритма добавлена возможность досрочного завершения функции, если для массива не требуется 
дальнейшая сортировка. В том случае, когда за один проход не было выполнено ни одной перестановки элементов, 
массив считается отсортированным и функция возвращает результат. 

Это позволяет сократить количество проходов при досрочном выполнении сортировки, а также
сразу вернуть результат, если в функцию передается уже отсортированный массив.

"""
