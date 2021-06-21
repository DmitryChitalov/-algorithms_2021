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

enter_num = 1000


def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)


print(timeit("revers_1(enter_num)", number=2500000, globals=globals()))
run('revers_1(enter_num)')


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


print(timeit("revers_2(enter_num)", number=2500000, globals=globals()))
run('revers_2(enter_num)')


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


print(timeit("revers_3(enter_num)", number=2500000, globals=globals()))
run('revers_3(enter_num)')


def revers_4(enter_num):
    revers_num = list(str(enter_num))
    revers_num.reverse()
    result = int(''.join(revers_num))
    return result


print(timeit("revers_4(enter_num)", number=2500000, globals=globals()))
run('revers_4(enter_num)')

# Вывод: Сделал свой вариант с использованием нескольких встроенных методов строк и списков,
# не самый красивый и быстрый вариант, работает чуть быстрее функции с рекурсией,
# самый быстрый вариант - это функция со срезом, так как используется встроенный механизм,
# а как известно они обычно встроенные механизмы самые быстрые.
