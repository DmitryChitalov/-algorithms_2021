"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Обязательно предложите еще свой вариант решения и также запрофилируйте!

Сделайте вывод, какая из четырех реализаций эффективнее и почему!!!

Без аналитики задание считается не принятым
"""
#Опираясь на время выполнения каждой из функции, можно сделать вывод о том, что функция revers_4 - самая эффективная,
#ведь мы передаем 1 аргумент и как такового, тела функции у нас нет, у нас функция возвращает  перевернутый, при
#помощи среза строковый тип числа.
#cProfile нам выдает везде 0, так как функции в cProfile вызывается 1 раз, ведь cProfile создан для - объемных функции.


from random import randint
from timeit import timeit
from cProfile import run
from time import sleep


def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return int(revers_num)
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
    return (str(enter_num))[::-1]


def revers_5(enter_num):
    str_e = ''
    for i in str(enter_num):
        str_e = i + str_e

    return str_e


number = randint(10000, 1000000)

print(
    timeit(
        "revers_1(number)",
        globals=globals()
        ), revers_1(number))
print(
    timeit(
        "revers_2(number)",
        globals=globals()
        ), revers_2(number))
print(
    timeit(
        "revers_3(number)",
        globals=globals()
        ), revers_3(number))
print(
    timeit(
        "revers_4(number)",
        globals=globals()
        ), revers_4(number))
print(
    timeit(
        "revers_5(number)",
        globals=globals(),
        ), revers_5(number))


#Чтобы в cProfile cumtime != 0,000, добавим через модуль time метод sleep, и просто его добавим в каждую функцию
#Работа функции = cumtime - ncalls * 2(так как sleep(2)) через cProfile.


def slower():
    sleep(2)


def revers_1(enter_num, revers_num=0):
    slower()
    if enter_num == 0:
        return int(revers_num)
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    slower()
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    slower()
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def revers_4(enter_num):
    slower()
    return (str(enter_num))[::-1]


def revers_5(enter_num):
    slower()
    str_e = ''
    for i in str(enter_num):
        str_e = i + str_e

    return str_e


print(run('revers_1(number)'))
print(run('revers_2(number)'))
print(run('revers_3(number)'))
print(run('revers_4(number)'))
print(run('revers_5(number)'))