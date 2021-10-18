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
import timeit
from cProfile import run
import time


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


def my_function(number, result=''):
    if number == 0:
        return result
    x = str(number % 10)
    result = result + x
    return my_function(number // 10, result)


enter_num = 17850


def main():
    enter_num = 17850
    one = revers_1(enter_num)
    two = revers_2(enter_num)
    three = revers_3(enter_num)
    four = my_function(enter_num)


print("revers_1 time with timeit: ", timeit.timeit("revers_1(enter_num, revers_num=0)", globals=globals()), "secs")
print("revers_2 time with timeit: ", timeit.timeit("revers_2(enter_num, revers_num=0)", globals=globals()), "secs")
print("revers_3 time with timeit: ", timeit.timeit("revers_3(enter_num)", globals=globals()), "secs")
print("my_function time with timeit: ", timeit.timeit("my_function(enter_num, result='')", globals=globals()), "secs")
run("main()")
run("revers_1(enter_num, revers_num=0)")
run("revers_2(enter_num, revers_num=0)")
run("revers_3(enter_num)")
run("my_function(enter_num, result='')")
# с функциец run() получаются другие резултаты, везде 0 не понимаю почему, я что-то не так делаю?...

# функция revers_3 эффективнее, так как она быстрее работает и также она более локаничная
