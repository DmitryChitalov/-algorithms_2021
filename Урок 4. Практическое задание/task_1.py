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

from random import randint
from timeit import repeat


def func_for(nums: list) -> list:
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr

# С вашего разрешения, добавлю сразу 3 наиболее очевидных решения этой задачи и посмотрим время их выполнения


def fun_while(nums: list) -> list:
    new_arr = []
    i = 0
    l = len(nums)
    while i < l:
        if nums[i] % 2 == 0:
            new_arr.append(i)
        i += 1
    return new_arr


def func_lc(nums: list) -> list:
    return [i for i in range(len(nums)) if nums[i] % 2 == 0]


def func_recursion(nums: list, i: int = 0) -> list:
    if i == len(nums) - 1:
        return [i] if nums[i] % 2 == 0 else []

    return [i] + func_recursion(nums, i+1) if nums[i] % 2 == 0 else func_recursion(nums, i+1)


if __name__ == '__main__':
    arr = [randint(0, 100000) for _ in range(990)]
    print(f"func_for: {min(repeat('func_for(arr)', repeat=5, number=1000, globals=globals()))}")
    # func_for: 0.06948139999999997
    print(f"fun_while: {min(repeat('fun_while(arr)', repeat=5, number=1000, globals=globals()))}")
    # fun_while: 0.09548999999999996
    print(f"func_lc: {min(repeat('func_lc(arr)', repeat=5, number=1000, globals=globals()))}")
    # func_lc: 0.05871080000000006
    print(f"func_recursion: {min(repeat('func_recursion(arr)', repeat=5, number=1000, globals=globals()))}")
    # func_recursion: 0.5256349

    """
    Списковое включение, как и ожидалось, оказалось несколько быстрее цикла for, который, в свою очередь, показал более 
    лучший результат, чем while. Рекурсия, тоже вполне ожидаемо, проявила себя хуже всех: помимо на порядок худшего 
    времени, она ещё и ограничила допустимый размер массива за счёт ограничения стека вызовов (понятно, что можно 
    увеличить размер стека, но, очевидно, это не самое лучшее решение). Списковое включение же быстрее цикла for, по 
    некоторым сведениям с одного уважаемого ресурса, за счёт отсутствия вызова функции addend, вместо которой 
    выполняется специальная ассемблерная команда (к сожалению, не понял, специально ли эта команда для этого инструмента
     создана, или была всегда).
    """
