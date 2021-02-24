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
from cProfile import run


def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)


num_100 = randint(10000, 1000000)
num_1000 = randint(1000000, 10000000)
num_10000 = randint(100000000, 10000000000000)

print('Функция revers_1')
print(
    timeit(
        "revers_1(num_100)",
        globals=globals(),
        number=10000))
print(
    timeit(
        "revers_1(num_1000)",
        globals=globals(),
        number=10000))
print(
    timeit(
        "revers_1(num_10000)",
        globals=globals(),
        number=10000))


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


print('Функция revers_2')
print(
    timeit(
        "revers_2(num_100)",
        globals=globals(),
        number=10000))
print(
    timeit(
        "revers_2(num_1000)",
        globals=globals(),
        number=10000))
print(
    timeit(
        "revers_2(num_10000)",
        globals=globals(),
        number=10000))


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


print('Функция revers_3')
print(
    timeit(
        "revers_3(num_100)",
        globals=globals(),
        number=10000))
print(
    timeit(
        "revers_3(num_1000)",
        globals=globals(),
        number=10000))
print(
    timeit(
        "revers_3(num_10000)",
        globals=globals(),
        number=10000))


def revers_4(enter_num):
    enter_num = list(str(enter_num))
    enter_num.reverse()
    return "".join(enter_num)


print('Функция revers_4')
print(
    timeit(
        "revers_4(num_100)",
        globals=globals(),
        number=10000))
print(
    timeit(
        "revers_4(num_1000)",
        globals=globals(),
        number=10000))
print(
    timeit(
        "revers_4(num_10000)",
        globals=globals(),
        number=10000))


def main(number):
    rev_1 = revers_1(number)
    rev_2 = revers_2(number)
    rev_3 = revers_3(number)
    rev_4 = revers_4(number)


run("main(num_100)")
run("main(num_1000)")
run("main(num_10000)")

"""
Добавил свой вариант решения через метод списка reverse (revers_4).
Профилировка через cProfile показала что слабые места во всех 4х функциях отсутствуют, время выполнения
менее 0.000 секунд. Профилировка через timeit показала следующие результаты (рейтинг по времени выполнения):
1. срез строки (0.009)
2. reverse списка (0.016)
3. цикл (0.09)
4. рекурсия (0.11)
Наиболее эффективны срез и реверс ввиду того, что это встроенные функции и выполняются 'под капотом'.
Эти функции реализованны именно для подобного рода задач.
"""
