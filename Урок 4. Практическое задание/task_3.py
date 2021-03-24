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


num = 123456789987654321123456789
run("revers_1(num)")
run("revers_2(num)")
run("revers_3(num)")

# Сравнивая эти 3 вызова через cProfile, можно увидеть, что первая функция делает много вызовов:
# 31 function calls (4 primitive calls) in 0.000 seconds

print('Выполнение первой функции составило', timeit("revers_1(num)", globals=globals()))
print('Выполнение второй функции составило', timeit("revers_2(num)", globals=globals()))
print('Выполнение третьей функции составило', timeit("revers_3(num)", globals=globals()))

# А при сравнении времени выполнения наглядно видно, что срез является самым быстрым.
# Рекурсия же показывает наихудший результат.
# Это связано с количеством вычислений, производимых внутри функции.
