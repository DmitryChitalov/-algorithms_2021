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
    revers_num = list(str(enter_num))
    revers_num.reverse()  # O(N)
    revers_num = "".join(revers_num)
    return revers_num


enter_num = 12345670

print('Вариант №1: ', timeit('revers_1(enter_num)', globals=globals()))
print('Вариант №2: ', timeit('revers_2(enter_num)', globals=globals()))
print('Вариант №3: ', timeit('revers_3(enter_num)', globals=globals()))
print('Вариант №4: ', timeit('revers_4(enter_num)', globals=globals()))


def main():
    revers_1(enter_num)
    revers_2(enter_num)
    revers_3(enter_num)
    revers_4(enter_num)


run('main()')

"""
Вариант №1:  1.4049418999999999
Вариант №2:  1.3231497
Вариант №3:  0.23859299999999983
Вариант №4:  0.31796729999999984

Вывод: Вариант со срезами самый быстрый.
1-ый вариант - рекурсия, сложность n!
2-ой вариант - сложность n, благодаря циклу while
3-ий вариант - срез, самый быстрый
4-ый вариант - проигрывает по быстроте 3-му варианту благодаря методам reverse и join

"""