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
    return ''.join(list(reversed(str(1234))))


print('Вариант 1:', timeit("revers_1(1234)", globals=globals()))
print('Вариант 2:', timeit("revers_2(1234)", globals=globals()))
print('Вариант 3:', timeit("revers_3(1234)", globals=globals()))
print('Вариант 4:', timeit("revers_4(1234)", globals=globals()))


def main():
    revers_1(1234)
    revers_2(1234)
    revers_3(1234)
    revers_4(1234)

help(str)
run("revers_1(1234)")
run("revers_2(1234)")
run("revers_3(1234)")
run("revers_4(1234)")

"""
Первый вариант самый медленный из-за рекурсии, очень много вызовов.
Второй вариант побыстрее благодаря использованию цикла, но третий самый быстрый, потому что 
выполняется встроенная функция.
"""