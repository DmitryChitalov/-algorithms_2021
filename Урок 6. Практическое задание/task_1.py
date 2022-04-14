"""
Задание 1.

Выполните профилирование памяти в скриптах.
Проанализируйте результат и определите программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 3-5 ваших РАЗНЫХ скриптов!
(хотя бы 3 разных для получения оценки отл).
На каждый скрипт вы должны сделать как минимум по две реализации.

Можно взять только домашние задания с курса Основ
или с текущего курса Алгоритмов

Результаты профилирования добавьте в виде комментариев к коду.
Обязательно сделайте аналитику (что с памятью в ваших скриптах, в чем ваша оптимизация и т.д.)

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО

Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!
"""

# ТЯЖЕЛО БЫЛО НАЙТИ ЗАДАЧИ "не модифицированные"

import time
import collections
from pympler import asizeof
from recordclass import recordclass
from numpy import array
import memory_profiler


def time_count(callback):
    def wrapper(*object_):
        start_in = time.perf_counter()
        callback(*object_)
        end_in = time.perf_counter() - start_in
        print(f'{end_in:.10f}')
        return object_
    return wrapper

# ДЕКОРАТОР ПО ПАМЯТИ И ВРЕМЕНИ
# def time_count_and_memory(callback):
#     def wrapper(*object_):
#         start_in = time.perf_counter()
#         callback(*object_)
#         end_in = time.perf_counter() - start_in
#         print(f'{end_in:.10f}')
#         m1 = memory_profiler.memory_usage()
#         m2 = memory_profiler.memory_usage()
#         mem_diff = m2[0] - m1[0]
#         print(mem_diff)
#         return object_, mem_diff
#     return wrapper


# Скрипт из основ Python'а
@time_count
def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    print(asizeof.asizeof(new_arr))


lst = [3457475, 246236, 235, 2, 426, 0]

func_1(lst)

# ПРОФИЛИРОВАНИЕ
# Здесь мы сделали профилирование по памяти - воспользовшись модулем numpy функцией array, не использовали лишние пере-
# менные + из-за использование list comprehensions получили уменьшенное время работы функции.


@time_count
def func_1(nums):
    print(asizeof.asizeof(array(i for i in range(len(nums)) if nums[i] % 2 == 0)))


lst = [3457475, 246236, 235, 2, 426, 0]

func_1(lst)

# Скрипт из основ Python'а


@time_count
def multiplication(numbers):
    for i in range(len(numbers)):
        if numbers[i] % 2 == 0:
            return numbers[i] ** 2


lst_ex = [3457475, 246236, 235, 2, 426, 0]

print(asizeof.asizeof(multiplication(lst_ex)))


# ПРОФИЛИРОВАНИЕ
# Здесь мы сделали профилирование при помощи функции yield, ну и цикл сделали лучше.

@time_count
def multiplication(numbers):
    for num in numbers:
        if num % 2 == 0:
            yield num * num


lst_ex = [3457475, 246236, 235, 2, 426, 0]

print(asizeof.asizeof(multiplication(lst_ex)))

# Скрипт из основ Python'а


@time_count
def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return print(asizeof.asizeof(new_arr))


lst = [3457475, 246236, 235, 2, 426, 0]

func_1(lst)

# ПРОФИЛИРОВАНИЕ
# Здесь мы сделали профилирование по памяти - воспользовшись модулем numpy функцией array, не использовали лишние пере-
# менные + из-за использование list comprehensions получили уменьшенное время работы функции.


@time_count
def func_1(nums):
    return print(asizeof.asizeof(array(i for i in range(len(nums)) if nums[i] % 2 == 0)))


lst = [3457475, 246236, 235, 2, 426, 0]

func_1(lst)

# Скрипт из основ Python'а

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
res = set()
repeated_in_numbers = set()

for name in src:
    if name in repeated_in_numbers:
        continue
    if name in res:
        repeated_in_numbers.add(name)
        res.discard(name)
        continue
    res.add(name)

result = [el for el in src if el in res]

print(asizeof.asizeof(result))

# ПРОФИЛИРОВАНИЕ
# Здесь мы сделали профилирование по памяти - воспользовшись модулем numpy функцией array, получим очень сжатый массив
# больше в 2 раза.

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
res = set()
repeated_in_numbers = set()

for name in src:
    if name in repeated_in_numbers:
        continue
    if name in res:
        repeated_in_numbers.add(name)
        res.discard(name)
        continue
    res.add(name)

result = array([el for el in src if el in res])

print(asizeof.asizeof(result))

# СДАНА

# Скрипт из основ Python'а
#
# @time_count
# def game(player, enemy):
#
#     player = {
#         'name': player,
#         'health': 100,
#         'damage': 50,
#         'armor': 1.2
#     }
#
#     enemy = {
#         'name': enemy,
#         'health': 70,
#         'damage': 35,
#         'armor': 1.2
#     }
#
#     def attack(person1, person2):
#         person1['health'] = person1['health'] - defence(person1, person2)
#         return person1['health']
#
#     def defence(personwithdefence1, personwithdefence2):
#         raznicadefence = (personwithdefence2['damage'] // personwithdefence1['armor'])
#         return raznicadefence
#
#     attack(player, enemy)
#     return print(asizeof.asizeof(player), asizeof.asizeof(enemy))
#
#
# # name_player = input("Vvedite Imya Igroka: ")
# name_player = 'Egor'
# # name_enemy = input("Vvedite Imya Vraga: ")
# name_enemy = 'Makar'
#
# game(name_player, name_enemy)
#
#
# # ПРОФИЛИРОВАНИЕ
# # Здесь мы сделали профилирование по памяти - воспользовшись модулем recordclass словарем recordclass,
# # он лучше смотрится по памяти, но к сожалению по времени уступает обычному словарю.
#
# @time_count
# def game(player, enemy):
#
#     dic_1 = recordclass('player', ('name', 'health', 'damage', 'armor'))
#
#     dic_player = dic_1(name=player, health=100, damage=50, armor=1.2)
#
#     dic_2 = recordclass('enemy', ('name', 'health', 'damage', 'armor'))
#
#     dic_enemy = dic_2(name=enemy, health=70, damage=35, armor=1.3)
#
#     def attack(person1, person2):
#         person1.health = person1.health - defence(person1.armor, person2.damage)
#         return person1
#
#     def defence(personwithdefence1, personwithdefence2):
#         raznicadefence = (personwithdefence2 // personwithdefence1)
#         return raznicadefence
#
#     attack(dic_player, dic_enemy)
#     return print(asizeof.asizeof(dic_1), asizeof.asizeof(dic_2))
#
#
# # name_player = input("Vvedite Imya Igroka: ")
# name_player = 'Egor'
# # name_enemy = input("Vvedite Imya Vraga: ")
# name_enemy = 'Makar'
#
# game(name_player, name_enemy)