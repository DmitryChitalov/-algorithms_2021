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
from time import time
from timeit import timeit
from datetime import timedelta
import random

# профилирование через timeit
def bubble_sort_origin(lst_obj):
    n = 1
    # при сортировки пузырьком по убываюнию, пузырек "тонет", те
    while n < len(lst_obj):
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        n += 1
    return lst_obj


def bubble_sort_tom(lst_obj):
    n = 1
    while n < len(lst_obj):
        flag_change = False
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                flag_change = True
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        if flag_change == False:
            break
        else:
            n += 1
    return lst_obj


list_for_sort = [random.randint(-100, 99) for _ in range(100)]
print("Исходный массив: ", list_for_sort)

# замеры 100 эллементов массива
print("замеры сортировки массива из 100 рандомных эллементов ")
print(
    timeit(
        "bubble_sort_origin(list_for_sort[:])",
        globals=globals(),
        number=500))
print(
    timeit(
        "bubble_sort_tom(list_for_sort[:])",
        globals=globals(),
        number=500))

print("Отсортированный массив: ", bubble_sort_origin(list_for_sort[:]))
print("Отсортированный массив: ", bubble_sort_tom(list_for_sort[:]))



list_almost_sorted = [1, 10, 9, 8, 7, 6, 5, 4, 3, 2]
list_for_sort = list_almost_sorted

# замеры 100 эллементов массива
print("\nзамеры сортировки отстортированного по убыванию массива из 10 эллементов ")
print(
    timeit(
        "bubble_sort_origin(list_for_sort[:])",
        globals=globals(),
        number=500))
print(
    timeit(
        "bubble_sort_tom(list_for_sort[:])",
        globals=globals(),
        number=500))
'''
оригинальный алгоритм быстрее
0.363110168
0.36942495000000003

но иногда, чуть быстрее улучшенный алгоритм
0.358108719
0.35085638

при рассмотрении сортирвки почти отсортированного массива видно, что улучшенный алгоритм быстрее
0.003973444999999964
0.0016734069999999601
'''



list_for_sort = [random.randint(-100, 99) for _ in range(400)]

print("замеры 1000 эллементов массива")
print(
    timeit(
        "bubble_sort_origin(list_for_sort[:])",
        globals=globals(),
        number=100))
print(
    timeit(
        "bubble_sort_tom(list_for_sort[:])",
        globals=globals(),
        number=100))
'''
замеры 1000 эллементов массива
1.141367211
1.1528312250000001

    Вывод: оптимизация дала улучшения только на уже практически отсортированных массивах, 
    на рандомных массивах - нет улучшения по времени.
     улчешение алогоритма сортировки пузырьком немного увеличило время сортировки.

       Доработка заключается в установлении флага = True, если сделана замена, 
    если флаг не был установлен, те не было сделано замен, то цикл сортировки прекращается
    и его "обнулении", при выборе нового эелемента массива для сортировки
'''

# print("Отсортированный массив: ", bubble_sort_origin(list_for_sort[:]))
# print("Отсортированный массив: ", bubble_sort_tom(list_for_sort[:]))

# bubble_sort_origin(list_for_sort[:])
# sorted_list = bubble_sort_tom(list_for_sort[:])

'''
#               замер через time и @log_time

def log_time(func):  # O(1)
    def wrapper(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        print(f"Время выполнения ф-ции {func.__name__} составило: {timedelta(seconds=end_time - start_time)}")
        return result

    return wrapper


@log_time
def bubble_sort_origin(lst_obj):
    n = 1
    # при сортировки пузырьком по убываюнию, пузырек "тонет", те
    while n < len(lst_obj):
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        n += 1
    return lst_obj


@log_time
def bubble_sort_tom(lst_obj):
    n = 1
    while n < len(lst_obj):
        flag_change = False
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                flag_change = True
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        if flag_change == False:
            break
        else:
            n += 1
    return lst_obj


list_for_sort = [random.randint(-100, 99) for _ in range(3000)]
# print("Исходный массив: ", list_for_sort)

# print("Отсортированный массив: ", bubble_sort_origin(list_for_sort[:]))
# print("Отсортированный массив: ", bubble_sort_tom(list_for_sort[:]))

bubble_sort_origin(list_for_sort[:])
sorted_list = bubble_sort_tom(list_for_sort[:])

при N = 2200
Время выполнения ф-ции bubble_sort_origin составило: 0:00:00.390000
Время выполнения ф-ции bubble_sort_tom составило: 0:00:00.410000

Улучшение не помогло

list_almost_sorted = [-101, -1010, -800, -700, -600, -101, -1010, -800, -700, -600, -101, -1010, -800, -700, -600]
list_almost_sorted.extend(sorted_list)
# print("list_almost_sorted", list_almost_sorted)
# print("Отсортированный массив: ", bubble_sort_origin(list_almost_sorted[:]))
# print("Отсортированный массив: ", bubble_sort_tom(list_almost_sorted[:]))

print("Сортировка почти полностью отсортированного массива:")
bubble_sort_origin(list_for_sort[:])
sorted_list = bubble_sort_tom(list_for_sort[:])


# при N = 3000
Время выполнения ф-ции bubble_sort_origin составило: 0:00:00.750000
Время выполнения ф-ции bubble_sort_tom составило: 0:00:00.780000
Сортировка почти полностью отсортированного массива:
Время выполнения ф-ции bubble_sort_origin составило: 0:00:00.740000
Время выполнения ф-ции bubble_sort_tom составило: 0:00:00.760000

Улучшение также не помогло

    Вывод: оптимизация не дала улучшения.
     улчешение алогоритма сортировки пузырьком немного увеличило время сортировки

       Доработка заключается в установлении флага = True, если сделана замена, 
    если флаг не был установлен, те не было сделано замен, то цикл сортировки прекращается
    и его "обнулении", при выборе нового эелемента массива для сортировки

'''
