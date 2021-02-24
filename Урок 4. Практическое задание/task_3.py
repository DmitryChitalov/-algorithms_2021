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


usr_num = 12345678901234


def main():
    revers_1(usr_num)
    revers_2(usr_num)
    revers_3(usr_num)


print("Revers_1:", timeit("revers_1(usr_num)", globals=globals()))
print("Revers_2:", timeit("revers_2(usr_num)", globals=globals()))
print("Revers_3:", timeit("revers_3(usr_num)", globals=globals()))

run("main()")


"""
Аналитика:
Revers_1 выделяется как в cProfile - много вызовов, так и в timeit - самое продолжительное выполнение, в связи
с рекурсией.
Revers_2 в cProfile не выделился - 1 вызов и быстрое выполнение, в timeit выделился- немногим быстрее рекурсии
из-за отсутствия многочисленных, одинаковых вызовов.
Revers_3 в cProfile не отличается от предыдущего. В timeit значительно различи от второго, так как используется
встроенная инструкция реверса.
"""