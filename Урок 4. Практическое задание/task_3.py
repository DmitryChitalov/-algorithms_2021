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


""" Первый алгоритм выполнен через рекурсию, самый требовательный к ресурсам из за рекурсии, время выполнения O(n) """


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


""" Второй по сути тоже самое, но выполнено через цикл время выполнения Линейная O(n) """


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


""" Третий способ самый эффективный и лаконичный константное время выполнения """


def revers_4(enter_num):
    return reversed(str(enter_num))


""" Долго думал, но ни чего умней не придумал, по сути это тот же 3 способ написанный подругому, константное время """

num = 123456789123456789
print("Проверка через timeit")
print(f'Время выполнения алгоритма revers_1 = {timeit("revers_1(num)", globals=globals())}')
print(f'Время выполнения алгоритма revers_2 = {timeit("revers_2(num)", globals=globals())}')
print(f'Время выполнения алгоритма revers_3 = {timeit("revers_3(num)", globals=globals())}')
print(f'Время выполнения алгоритма revers_4 = {timeit("revers_4(num)", globals=globals())}')

print("\nПроверка через cProfile")
print(f'Время выполнения алгоритма revers_1 = {run("revers_1(num)")}')
print(f'Время выполнения алгоритма revers_2 = {run("revers_2(num)")}')
print(f'Время выполнения алгоритма revers_3 = {run("revers_3(num)")}')
print(f'Время выполнения алгоритма revers_4 = {run("revers_4(num)")}')

""" Однозначно лучшаяя функция это revers_3 и 4, т.к. с ростом входящих данных они будет выполняться быстрее
    Из двух замерщиков в данном примере явно нагляденее timeit
"""
