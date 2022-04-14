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

from cProfile import run
from timeit import timeit

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

def reverse_4(enter_num):
    if enter_num < 10:
        return str(enter_num)
    return str(enter_num % 10) + reverse_4(enter_num//10)

def main(num):
    for _ in range(1000000):
        revers_1(num)
        revers_2(num)
        revers_3(num)
        reverse_4(num)
num = 1234567890

print(timeit('revers_1(num)', globals=globals()))
print(timeit('revers_2(num)', globals=globals()))
print(timeit('revers_3(num)', globals=globals()))
print(timeit('reverse_4(num)', globals=globals()))
run('main(num)')
"""
Почти все значения совпадают, однако есть вопросы к 1 и 4 функции
Значения cumtime в два раза больше чем измерения в timeit
в принципе результаты ожидаемы, самой быстрой оказалась та функция, в которой
мы проигрываем за счет потери памяти. Авторская оказалась самой долгой,
потому что реализована с помощью рекурсии и конкатенации строк
Функция через цикл показала неплохой 2 результат, но все равно он хуже лучшего
почти в 10 раз
"""