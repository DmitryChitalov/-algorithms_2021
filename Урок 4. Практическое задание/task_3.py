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
    enter_num = list(str(enter_num))
    enter_num.reverse()
    return "".join(enter_num)


def main(number):
    revers_1(number)
    revers_2(number)
    revers_3(number)
    revers_4(number)


num_100 = randint(10000, 1000000)
num_1000 = randint(1000000, 10000000)
num_10000 = randint(100000000, 10000000000000)

print('Время выполнения revers_1')
print(timeit("revers_1(num_100)", globals=globals(), number=10000))
print(timeit("revers_1(num_1000)", globals=globals(), number=10000))
print(timeit("revers_1(num_10000)", globals=globals(), number=10000))

print('Время выполнения revers_2')
print(timeit("revers_2(num_100)", globals=globals(), number=10000))
print(timeit("revers_2(num_1000)", globals=globals(), number=10000))
print(timeit("revers_2(num_10000)", globals=globals(), number=10000))
print('Время выполнения revers_3')
print(timeit("revers_3(num_100)", globals=globals(), number=10000))
print(timeit("revers_3(num_1000)", globals=globals(), number=10000))
print(timeit("revers_3(num_10000)", globals=globals(), number=10000))
print('Время выполнения revers_4')
print(timeit("revers_4(num_100)", globals=globals(), number=10000))
print(timeit("revers_4(num_1000)", globals=globals(), number=10000))
print(timeit("revers_4(num_10000)", globals=globals(), number=10000))

run("main(num_100)")
run("main(num_1000)")
run("main(num_10000)")

"""
Мой вариант решения через reverse.
cProfile показала что у всех функций время выполнения менее 0.000 секунд.
Замеры времени через timeit показали что наиболее эффективны функция revers_3 и функция revers_4.
Так как срез и встроенная функция reverse условно говоря для этого и созданы
"""
