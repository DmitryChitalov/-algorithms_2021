"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение!
"""

from memory_profiler import profile

numerical_series = [1]

def numerical_series_sum(user_number, next_number = 1.0):
    """
    Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
    :param user_number: вводимое число
    :param next_number:
    :return:
    """
    if user_number > 0:
        new_number = -next_number / 2
        numerical_series.append(new_number)
        user_number -= 1
        return numerical_series_sum(user_number - 1, new_number)
    else:
        return sum(numerical_series)

# user_number = int(input('Введите количество элементов: '))
user_number = 10

@profile
def sub_num(func):
    return func

func_num = sub_num(user_number)
print(f'Количество элементов: {user_number}, их сумма: {func_num}')

"""
Записал рекурсивную фукцию в другую фукцию (этакий аналог декоратора)
и теперь профилировщик вызывается один раз

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    31     18.2 MiB     18.2 MiB           1   @profile
    32                                         def sub_num(func):
    33     18.2 MiB      0.0 MiB           1       return func
"""