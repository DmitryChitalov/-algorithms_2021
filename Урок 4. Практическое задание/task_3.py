"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему!!!

И можете предложить еще свой вариант решения!
Без аналитики задание считается не принятым

ВЫВОД ПО ЗАДАНИЮ: Функция revers_1 самая медленная поскольку она рекурсивная, функция revers_2 делается медленее
поскольку содержит внутри цикл и вычисления, третья функция самая простая и при этом самая эффективная поскольку
в ней меньше действий аргумент который принимается переводится
в строковое значение и присваивается другой переменой с параметром [::-1].
я решил написать свою реализацию через lambda в return, по сути это схоже с 3 функцией, но не много быстрее.

cProfile: всего показало 12 запусков 5 из которых были в функции с рекурсией revers_1, в столбце cumtime 0.000
по всем функциям что означает что оптимизации не требует. Хотя через timeit цыфры разнятся.
"""
from timeit import timeit
from cProfile import run


def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def revers_4(enter_num):
    return lambda revers_num: str(enter_num)[::-1]


def main():
    revers_1(1000)
    revers_2(1000)
    revers_3(1000)
    revers_4(1000)


run("main()")
print(timeit("revers_1(1000)", globals=globals()))
print(timeit("revers_2(1000)", globals=globals()))
print(timeit("revers_3(1000)", globals=globals()))
print(timeit("revers_4(1000)", globals=globals()))
