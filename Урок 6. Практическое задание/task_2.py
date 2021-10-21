"""
Задание 2.*
Предложить еще какие-либо варианты (механизмы, подходы, библиотеки, идеи)
для оптимизации памяти и
доказать!!! (наглядно, кодом) их эффективность (на примере профилировщика).
С урока ничего не дублир-ть. только новые способы
"""

from more_itertools import islice_extended, ilen
from pympler import asizeof
import memory_profiler



def decorator(func):
    def wrapper(*args, **kwargs):
        mem_1 = memory_profiler.memory_usage()
        res = func(*args, **kwargs)
        mem_2 = memory_profiler.memory_usage()
        mem_diff = mem_2[0] - mem_1[0]
        return res, mem_diff

    return wrapper



@decorator
def fun():
    """
    Подсчет значений кратное 3-м
    """
    print(ilen(x for x in range(1000000) if x % 3 == 0))



@decorator
def fun2():
    """
    Подсчет значений кратное 3-м
    """
    print(len(x for x in range(1000000) if x % 3 == 0))


res, mem_diff = fun()
print(f"Выполнение заняло {mem_diff} Mib")
print(asizeof.asizeof(res))


res, mem_diff = fun2()
print(f"Выполнение заняло {mem_diff} Mib")
print(asizeof.asizeof(res))

"""
333334
Выполнение заняло 0.00390625 Mib
16
333334
Выполнение заняло 1.1796875 Mib
16
Первая функция - fun оказалась намного экономней по памяти, чем первая.
"""

from memory_profiler import profile

dict_evens_odds = {'evens': 0, 'odds': 0}


@profile
def profiled_even_n_odd(*args):
    def even_n_odd(number: int):
        if number // 10 == 0 and number == 0:
            return
        last_digit = number % 10
        if last_digit % 2 == 0:
            dict_evens_odds['evens'] += 1
        else:
            dict_evens_odds['odds'] += 1
        even_n_odd(number // 10)

    return even_n_odd(*args)


def ask_user():
    number = input("Введите целое число! Нажмите 0 для выхода: ")

    try:
        if int(number) <= 0:
            return None
        profiled_even_n_odd(int(number))
        print(dict_evens_odds)
    except ValueError:
        print("Допускаются только целые числа. Попробуйте еще раз.")
    dict_evens_odds['evens'] = 0
    dict_evens_odds['odds'] = 0
    return ask_user()


if __name__ == "__main__":
    ask_user()

"""
Чтобы профилировщик не вызывался при каждом вызове рекурсивной ункции,
нужно завернуть исходную функцию в другую функцию
"""