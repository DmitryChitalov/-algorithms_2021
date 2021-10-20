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
from memory_profiler import profile
from random import randint
from numpy import array

# В классическом решении был обычный список, который я искуственно увеличил
print('*' * 100, 'Задача 1', '*' * 100)
print('Старое решение через список')


@profile
def func_old():
    prices = [randint(1, 100) for i in range(1000000)]
    format_prices = []
    for i in prices:
        i = str(i)
        if '.' in i:
            a = i.split('.')
            format_prices.append(f'{a[0]} руб. {int(a[1]):02} коп.')
        else:
            format_prices.append(f'{i} руб. 00 коп.')
    return ', '.join(format_prices)


func_old()

print('Новое решение через генератор')


# Создаем генератор для экономии памяти
def fill(numb):
    for i in numb:
        yield randint(1, 100)


@profile
def func_new():
    my_gen = fill(range(1000000))
    format_prices = []
    for i in my_gen:
        i = str(i)
        if '.' in i:
            a = i.split('.')
            format_prices.append(f'{a[0]} руб. {int(a[1]):02} коп.')
        else:
            format_prices.append(f'{i} руб. 00 коп.')
    format_prices_numpy = array(format_prices)
    del format_prices
    return ', '.join(format_prices_numpy)


func_new()

"""
Для освобождении памяти применил генератор вместо списка, так же из полученного списка сделал numpy-объект 
и удалил сам список. По замерам получили выгоду около 50 Mib.
"""

print('*' * 100, 'Задача 2', '*' * 100)

print('Старое решение через рекурсию')


@profile
def sum_el(*args):
    return recur_sum_el(*args)


def recur_sum_el(num, one):
    if num == 1:
        return one
    return recur_sum_el(num - 1, one / -2) + one


user_number = int(input('Введите число: '))
print(f'Количество элементов: {user_number}, их сумма: {sum_el(user_number, 1)}')


@profile
def sum_el_new(num):
    res = 1
    a = res / -2
    for i in range(num - 1):
        res = res + a
        a = a / -2
    return res


user_number = int(input('Введите число: '))
print(f'Количество элементов: {user_number}, их сумма: {sum_el_new(user_number)}')

"""
Корректировка ДЗ согласно замечаниям. Для замера рекурсивной функции добавил функцию-обертку, в которую вложил 
рекурсивную функцию.
Само профилирование памяти заключается в замене рекурсии на цикл.
"""
