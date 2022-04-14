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

from timeit import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


print(timeit("func_1([1, 2, 3, 5, 25, 22, 43, 44])", globals=globals(), number=10000000))


def func_2(nums):
    return [i for i in range(len(nums)) if nums[i] % 2 == 0]


print(timeit("func_2([1, 2, 3, 5, 25, 22, 43, 44])", globals=globals(), number=10000000))

"""Аналитика: Чтобы функция выполнялась, добавим вызов с элементарным списком, ну и конечно же
профилирование во времени. Сразу сделал списковключение так как это просто,
но результат был интересным, списковключение показало то же самое по времени выполнения чем простые операции
и цикл. Сложность обоих алгоритмов одинаковая - линейная.
========func_1==========
11.0127453
========================
========func_2==========
11.6880606
========================
Вывод: Списковключения - синтаксический сахар.

Теперь попробуем оптимизировать убрав пару лишних встроенных функций типо range() и len()
"""


def func_3(nums):
    return [i for i in nums if i % 2 == 0]


print(timeit("func_3([1, 2, 3, 5, 25, 22, 43, 44])", globals=globals(), number=10000000))

"""
Результат, как говорится, "на лицо".
========func_1==========
11.128353299999999
========================
========func_2==========
11.902091699999998
========================
========func_3==========
7.986915
========================
И кстати, списковключения опять незначительно медленнее, но это у меня влияют разные факторы.
На самом деле должно быть бытрее, думаю это будет видно при большем количестве элементов списка.
"""