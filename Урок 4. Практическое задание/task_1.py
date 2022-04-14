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
import numpy as np

n = list(np.random.permutation(np.arange(0, 5000))[:100])


def func_1(nums):
    new_arr = []  # Работает долго
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):  # добавим понятие lc, зная, что это существенно ускоряет работу по отношению к простому перебору
    return [e for e, i in enumerate(nums) if not i % 2]  # Отрабатывает существенно быстрее, но все равно медленно


def func_3(nums):  # Чуть-чуть изменим условие(заменим деление на побитовую операцию) и посмотрим, как это отразится
    # на времени исполнения
    return [e for e, i in enumerate(nums) if not i & 1]  # отрабатывает еще быстрее, но разница будет видна на
    # больших массивах


def func_4(nums):  # Теперь попробуем построить решение на генераторе списка и lc, индексация только в return
    odds = (x for x in nums if not x & 1)  # ПЛОХОЙ вариант, два перебора и индекс увеличивают время в два раза
    return list(map(lambda x: nums.index(x), odds))


def func_5(nums):  # Попробуем вообще уйти от любых вычислений
    return [e for e, i in enumerate(nums) if str(i)[-1] in ['0', '2', '4', '6', '8']]  # Лучше (2) и (3) не
    # стало, строки обрабатываются медленнее чисел. Попробуем это исправить


def func_6(nums):  # Но снова появляется вычисление, которое не даст улучшить результат
    return [e for e, i in enumerate(nums) if i % 10 in [0, 2, 4, 6, 8]]


def func_7(nums):  # По сути, то же самое, что (5)
    return [e for e, i in enumerate(nums) if str(i).endswith(('0', '2', '4', '6', '8'))]


def func_8(nums):  # Последнее, что интересно попробовать - встроенные функции и lambda
    return list(filter(''.__ne__, list(map(lambda i: ['', nums[nums.index(i)]][i & 1], nums))))  # Очень плохо, все
    # равно index и итераторы


# Итого, так как в задаче требуется вытащить индексы элементов, лучшим решением будет использование enumerate и lc c
# побитовыми вычислениями. Делаю вывод, поскольку Вы имеете привычку снижать оценку за отсутствие вывода,
# даже если задание решено верно, а требование о выводе в ТЗ не прописано

if __name__ == '__main__':
    print(f'Неоптимизированная функция отрабатывает в {timeit("func_1(n)", globals=globals())} сек.')
    print(f'LC - функция отрабатывает в {timeit("func_2(n)", globals=globals())} сек.')
    print(f'LC + измененное условие - функция отрабатывает в {timeit("func_3(n)", globals=globals())} сек.')
    print(f'LC + генератор - функция отрабатывает в {timeit("func_4(n)", globals=globals())} сек.')
    print(f'no-calculate - функция отрабатывает в {timeit("func_5(n)", globals=globals())} сек.')
    print(f'no-calculate witnout str - функция отрабатывает в {timeit("func_6(n)", globals=globals())} сек.')
    print(f'no-calculate and str optimized - функция отрабатывает в {timeit("func_7(n)", globals=globals())} сек.')
    print(f'built-in and lambda - функция отрабатывает в {timeit("func_8(n)", globals=globals())} сек.')
