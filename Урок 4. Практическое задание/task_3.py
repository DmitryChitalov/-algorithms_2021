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


def my_revers(enter_num):
    enter_num = list(str(enter_num))
    enter_num.reverse()
    revers_num = int(''.join(enter_num))
    return revers_num


print(timeit('revers_1(enter_num)', 'enter_num=12345', globals=globals()))
print(timeit('revers_2(enter_num)', 'enter_num=12345', globals=globals()))
print(timeit('revers_3(enter_num)', 'enter_num=12345', globals=globals()))
print(timeit('my_revers(enter_num)', 'enter_num=12345', globals=globals()))

run('revers_1(12345)')
print('--' * 50)
run('revers_1(12345)')
print('--' * 50)
run('revers_1(12345)')
print('--' * 50)
run('my_revers(12345)')

"""
Самая быстрая функция оказалась № 3, на мой взгляд, из-за того, что при ее исполнении происходит меньше всего 
вызовов встроенных функций и методов. Но я заметил, что тип данных, полученного результата в этой функции - str, 
а если перевести его в int, то она станет чуть помедленнее из-за дополнительного вызова встроенной функции, 
хотя все равно будет на первом месте.
На втором месте функция написанная мной, полагаю, что из-зи того, что в ней используются только встроенные функции
и методы достаточно простой сложности и не тратится время на математические операции.
Рекурсивная функция - самая медленная, т.к. рекурсия, в принципе, медленная штука из-зи своего уровня сложности.
"""
