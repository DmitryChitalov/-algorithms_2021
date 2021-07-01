"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему!!!

И можете предложить еще свой вариант решения!
Без аналитики задание считается не принятым
"""

from timeit import timeit
from random import randint
import cProfile

def revers_1(enter_num, revers_num=0):
    '''Функция переворота числа через рекурсию O(log n)'''
    if enter_num == 0:
        return revers_num
    num = enter_num % 10
    revers_num = (revers_num + num / 10) * 10
    enter_num //= 10
    return revers_1 (enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    '''Функция переворота числа через цикл O(n)'''
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    '''Функция переворота числа через срез O(n)'''
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num

def revers_4(enter_num):
    '''Функция переворота числа через reverse() O(n)'''
    n_list = list(str(enter_num))
    n_list.reverse()
    return "".join(n_list)

if __name__ == '__main__':
    num_100 = randint (10000, 1000000)
    num_1000 = randint (1000000, 10000000)
    num_10000 = randint (100000000, 10000000000000)
    print (num_100, num_1000, num_10000)
    for statement in ["revers_1(num_100)", "revers_1(num_1000)", "revers_1(num_10000)",
                      "revers_2(num_100)", "revers_2(num_1000)", "revers_2(num_10000)",
                      "revers_3(num_100)", "revers_3(num_1000)", "revers_3(num_10000)",
                      "revers_4(num_100)", "revers_4(num_1000)", "revers_4(num_10000)"]:
        print(statement)
        print (
            timeit (
                statement,
                globals = globals(),
                number = 10000))

    cProfile.run ('revers_1(1000000000000000000000000000000000000000000000000000000000000000000)')
    cProfile.run ("revers_2(1000000000000000000000000000000000000000000000000000000000000000000)")
    cProfile.run ("revers_3(1000000000000000000000000000000000000000000000000000000000000000000)")
    cProfile.run ("revers_4(1000000000000000000000000000000000000000000000000000000000000000000)")
"""
Результаты работы timeit
--- Рекурсия ---
revers_1(num_100)
0.020064699999999998 худшее время
revers_1(num_1000)
0.013709600000000002 худшее время
revers_1(num_10000)
0.02523389999999999 худшее время
--- Цикл ---
revers_2(num_100)
0.007830099999999993
revers_2(num_1000)
0.009087800000000007
revers_2(num_10000)
0.01671679999999999
--- Срез ---
revers_3(num_100)
0.002471100000000004 лучшее время
revers_3(num_1000)
0.002540399999999998 лучшее время
revers_3(num_10000)
0.0027134000000000047 лучшее время
---- Результаты ----
лучше время показывает функция разворота через срез, хотя сложность одинаковая с циклом

Сделана функция через реверс - она показала результат похожий со срезом, но время в два раза хуже

"""
