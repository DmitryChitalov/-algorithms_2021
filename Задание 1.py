"""
Задание 1.
Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива
Сделайте замеры времени выполнения кода с помощью модуля timeit
Оптимизируйте, чтобы снизить время выполнения
Проведите повторные замеры.
Добавьте аналитику: что вы сделали и почему!!!
Без аналитики задание не принимается
И прошу вас обратить внимание, что то, что часто ошибочно называют генераторами списков,
на самом деле к генераторам отношения не имеет. Это называется "списковое включение" - list comprehension.
"""

from timeit import Timer
from timeit import timeit

# с функцией append
def func_1(nums):
    new_arr = []
    for i in range(len(nums)): # Генератор. O(n) - сложность
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr

# с функцией insert
def func_2(nums):
    new_arr = []
    for i in range(len(nums)): # Генератор. O(n) - сложность
        if nums[i] % 2 == 0:
            new_arr.insert(i)
    return new_arr

# с функцией enumerate (счетчик эл-тов)
def func_3(nums):
    return [i for i, el in enumerate(nums) if el % 2 ==0] # Списковое включение. O(n) - сложность

# nums = [2, 5, 7, 4, 8, 10, 12, 11]
nums = [el for el in range(1000)]

# 1-ЫЙ замер:
# Создаем таймер t = Timer("function т. е. stmt", "setup"). Кавычки - это не обозначение СТРОКИ, это синтаксис Timer
# Т. е. t = Timer("stmt - что мы замеряем", "setup - какие импорты (настройки) необходимо сделать перед запуском")
# t1 = Timer(stmt = 'func"_1()", setup = "fro"m__main__import func_1")# Здесь именованные арг-ты

t1 = Timer('func_1', "from __main__ import func_1")  # А здесь позиционные арг-ты
print("list append", t1.timeit(number=1000), "sec")

# ОДНОЙ строкой (append)
print(f'Одной строкой append', timeit("func_1", globals=globals(), number=1000))
# print(timeit("func_1", setup="from __main__ import func_1", number=1000)) # Аналог предыдущего

# 2-ОЙ замер:
print(f'Одной строкой insert', timeit("func_2", globals=globals(), number=1000))

# 3-ИЙ замер:
print(f'Одной строкой enumerate', timeit("func_3", globals=globals(), number=1000))

"""
В отличие от вебинара особой разницы не заметил. Или что то не так сделал?
Но запомню, что списковое включение работает чуть (10-15 процентов) быстрее

И ПОЧЕМУ, когда я обозначаю аргумент (nums) при ф-ии func_1:
print(f'Одной строкой append', timeit("func_1(nums)", globals=globals(), number=1000))
то программа ругается?

list append 1.1900000000002187e-05 sec
Одной строкой append 1.9999999999999185e-05
Одной строкой insert 1.739999999999728e-05
Одной строкой enumerate 1.6300000000000342e-05
"""
