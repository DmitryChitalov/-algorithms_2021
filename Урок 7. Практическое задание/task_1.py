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
from timeit import timeit
from random import randint
# создание исходного списка из 100 целых чисел
my_rand_int_list = [randint(-100, 100) for i in range(100)]


"""
Я использовала 3 различные реализации сортировки пузырьком в виде функции и замерила
данные с помощью модуля time_it.
Чтобы иметь возможность единожды вывести отсортированный результат, я использвала такие
возможности, как setup= и stmt=
Для того, чтоб все три реализации имели один и тот же сортируемый массив, я создала список
псевдослучайных чисел согласно условию задачи и использовала его.

Результаты таковы:
1. Доработка, требуемая в задании, выполнена. Она неэффективна, так как будет использоваться
только в случае, если передаваемый в функцию список был уже отсортирован заранее. При отсутствии
изменений списка в первом же проходе выполняется соответствие условию и завершение функции.
2. Реализация сортировки пузырьком, показанная на занятии (цикл while) - медленнее доработанной,
но это происходит за счет того, что в доработанной использованы циклы for, а не более медленный
while.
3. При поиске информации к ДЗ я нашла идею еще одного варианта реализации сортировки пузырьком
через цикл while и решила его протестировать. Он оказался наиболее медленным изо всех.

Для удобства проверки я привела все перечисленные функции с пузырьковой сортировкой отдельно,
после замеряемых.
"""

setup_code = '''
my_list = [67, 17, -90, 19, -70, 41, 64, -51, 71, -10, 31, -34, -65, -23,
           41, -77, 68, -80, 71, 64, 88, 57, 92, 93, 97, -62, -78, -6, -36,
           -72, 31, -72, 59, -16, -39, -82, -9, -85, 3, -14, -57, -34, -56,
           51, 91, -60, 94, -69, 11, -75, 35, 59, -33, -68, -29, -63, -53,
           55, 25, 25, -30, -29, -3, 56, 72, -21, 46, 67, -13, -36, 55, 35,
           71, 56, -61, 50, 99, -33, -97, -80, -81, -61, -41, -93, 59, 85, 1,
           -32, 56, 6, -21, 36, 98, 43, 45, 37, -33, -93, 17, -7]
print(f"Исходный массив: {my_list}")
def sorting_by_bubble_01(some_list):
    n = 1
    counter = 1
    while n < len(some_list):
        for i in range(len(some_list)-n):
            if some_list[i] < some_list[i+1]:
                some_list[i], some_list[i+1] = some_list[i+1], some_list[i]
            counter += 1
        n += 1
    return counter, some_list
res = sorting_by_bubble_01(my_list[:])
print(f"Количество итераций: {res[0]}, отсортированный список: {res[1]}")
'''
main_block = '''
sorting_by_bubble_01(my_list[:])
'''

print('Лучшее время среди 1000 запусков функции с сортировкой пузырьком Вариант 1:',
      timeit(setup=setup_code, stmt=main_block, number=1000))


setup_code = '''
my_list = [67, 17, -90, 19, -70, 41, 64, -51, 71, -10, 31, -34, -65, -23,
           41, -77, 68, -80, 71, 64, 88, 57, 92, 93, 97, -62, -78, -6, -36,
           -72, 31, -72, 59, -16, -39, -82, -9, -85, 3, -14, -57, -34, -56,
           51, 91, -60, 94, -69, 11, -75, 35, 59, -33, -68, -29, -63, -53,
           55, 25, 25, -30, -29, -3, 56, 72, -21, 46, 67, -13, -36, 55, 35,
           71, 56, -61, 50, 99, -33, -97, -80, -81, -61, -41, -93, 59, 85, 1,
           -32, 56, 6, -21, 36, 98, 43, 45, 37, -33, -93, 17, -7]
print(f"Исходный массив: {my_list}")
def sorting_by_bubble_02(some_list, flag=0):
    for i in range(len(some_list)-1):
        for j in range(len(some_list)-i-1):
            if some_list[j] < some_list[j + 1]:
                some_list[j], some_list[j + 1] = some_list[j + 1], some_list[j]
                flag = 1
        if flag == 0:
            print(f"Список был заранее отсортирован и не был изменен: {some_list}")
            return some_list
    return some_list
res = sorting_by_bubble_02(my_list[:])
print(f"Отсортированный список: {res}")
'''
main_block = '''
sorting_by_bubble_02(my_list[:])
'''

print('Лучшее время среди 1000 запусков функции с сортировкой пузырьком Вариант 2:',
      timeit(setup=setup_code, stmt=main_block, number=1000))


setup_code = '''
my_list = [67, 17, -90, 19, -70, 41, 64, -51, 71, -10, 31, -34, -65, -23,
           41, -77, 68, -80, 71, 64, 88, 57, 92, 93, 97, -62, -78, -6, -36,
           -72, 31, -72, 59, -16, -39, -82, -9, -85, 3, -14, -57, -34, -56,
           51, 91, -60, 94, -69, 11, -75, 35, 59, -33, -68, -29, -63, -53,
           55, 25, 25, -30, -29, -3, 56, 72, -21, 46, 67, -13, -36, 55, 35,
           71, 56, -61, 50, 99, -33, -97, -80, -81, -61, -41, -93, 59, 85, 1,
           -32, 56, 6, -21, 36, 98, 43, 45, 37, -33, -93, 17, -7]
print(f"Исходный массив: {my_list}")
def sorting_by_bubble_03(some_list):
      list_len = len(some_list)
      while True:
            count = 0
            for i in range(list_len - 1):
                  j = list_len - i - 1
                  if some_list[j] > some_list[j - 1]:
                        some_list[j], some_list[j - 1] = some_list[j - 1], some_list[j]
                        count += 1
            if count == 0:
                  break
      return some_list
res = sorting_by_bubble_03(my_list[:])
print(f"Отсортированный список: {res}")
'''
main_block = '''
sorting_by_bubble_03(my_list[:])
'''

print('Лучшее время среди 1000 запусков функции с сортировкой пузырьком Вариант 3:',
      timeit(setup=setup_code, stmt=main_block, number=1000))

print('')
setup_code = '''
my_list = [67, 17, -90, 19, -70, 41, 64, -51, 71, -10, 31, -34, -65, -23,
           41, -77, 68, -80, 71, 64, 88, 57, 92, 93, 97, -62, -78, -6, -36,
           -72, 31, -72, 59, -16, -39, -82, -9, -85, 3, -14, -57, -34, -56,
           51, 91, -60, 94, -69, 11, -75, 35, 59, -33, -68, -29, -63, -53,
           55, 25, 25, -30, -29, -3, 56, 72, -21, 46, 67, -13, -36, 55, 35,
           71, 56, -61, 50, 99, -33, -97, -80, -81, -61, -41, -93, 59, 85, 1,
           -32, 56, 6, -21, 36, 98, 43, 45, 37, -33, -93, 17, -7]
print(f"Исходный массив: {my_list}")
def sorting_by_bubble_02(some_list, flag=0):
    for i in range(len(some_list)-1):
        for j in range(len(some_list)-i-1):
            if some_list[j] < some_list[j + 1]:
                some_list[j], some_list[j + 1] = some_list[j + 1], some_list[j]
                flag = 1
        if flag == 0:
            return some_list
    return some_list
res = sorting_by_bubble_02(my_list)
print(f"Отсортированный список: {res}")
'''
main_block = '''
sorting_by_bubble_02(my_list[:])
'''

print('1000 запусков функции Вариант 2 с отсортированным массивом заняло',
      timeit(setup=setup_code, stmt=main_block, number=1000))


#############################################################################################
def sorting_by_bubble_01(some_list):
    """Usual version of bubble sorting"""
    n = 1
    counter = 1
    while n < len(some_list):
        for i in range(len(some_list)-n):
            if some_list[i] < some_list[i+1]:
                some_list[i], some_list[i+1] = some_list[i+1], some_list[i]
            counter += 1
        n += 1
    return counter, some_list


def sorting_by_bubble_02(some_list, flag=0):
    """Version of bubble sorting with break when already sorted"""
    for i in range(len(some_list)-1):
        for j in range(len(some_list)-i-1):
            if some_list[j] < some_list[j + 1]:
                some_list[j], some_list[j + 1] = some_list[j + 1], some_list[j]
                flag = 1
        if flag == 0:
            print(f"Список был заранее отсортирован и не был изменен: {some_list}")
            return some_list
    return some_list


def sorting_by_bubble_03(some_list):
    """Slow version of bubble sorting"""
    list_len = len(some_list)
    while True:
        count = 0
        for i in range(list_len - 1):
            j = list_len - i - 1
            if some_list[j] > some_list[j - 1]:
                some_list[j], some_list[j - 1] = some_list[j - 1], some_list[j]
                count += 1
        if count == 0:
            break
    return some_list
