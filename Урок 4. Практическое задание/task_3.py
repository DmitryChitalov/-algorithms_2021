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
from random import randint
from timeit import timeit
import cProfile

enter_num = randint(100000000, 10000000000000)


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


print(timeit("revers_1(enter_num)", number=100000, globals=globals()))
print(timeit("revers_2(enter_num)", number=100000, globals=globals()))
print(timeit("revers_3(enter_num)", number=100000, globals=globals()))

cProfile.run("revers_1(enter_num)")
cProfile.run("revers_2(enter_num)")
cProfile.run("revers_3(enter_num)")

"""
revers_1(enter_num) - 0.2937345
revers_2(enter_num) - 0.19276349999999998
revers_3(enter_num) - 0.0397748

Через cProfile не видно время выполнения функций, т.к она отсекает малые значения.

Самая эффективная функция revers_3, т.к преобразует число в строку и с помощью среза переворачиваем строку,
в других случаях у нас рекурсия самая долгая и цикл второй по скорости выполнения.
"""