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

number_of_rev = 10000000

def main_rev():
    revers_1(number_of_rev)
    revers_2(number_of_rev)
    revers_3(number_of_rev)

run('main_rev()')

print(timeit("revers_1(number_of_rev)", setup='from __main__ import revers_1, number_of_rev', number=100000))
print(timeit("revers_2(number_of_rev)", setup='from __main__ import revers_2, number_of_rev', number=100000))
print(timeit("revers_3(number_of_rev)", setup='from __main__ import revers_3, number_of_rev', number=100000))

# На запуск всех функций ушло 0секунд. Слабых мест нет.
# Как видно из результата, дольше всего работает первая функция (рекурсивная).
# Быстрее всего работает 3 функция, так как в ней используются среды.

