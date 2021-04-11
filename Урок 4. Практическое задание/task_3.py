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
from random import randint
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


num_1000 = randint(1000000, 10000000)
print(f'{timeit("revers_1(num_1000)", globals=globals(), number=1000)} revers_1')
print(f'{timeit("revers_2(num_1000)", globals=globals(), number=1000)} revers_2')
print(f'{timeit("revers_3(num_1000)", globals=globals(), number=1000)} revers_3')

run("revers_1(num_1000)")
run("revers_2(num_1000)")
run("revers_3(num_1000)")

'''
0.0053092 revers_1
0.0037709999999999966 revers_2
0.0007273000000000002 revers_3
revers_1 самая медленная функция так как используется рекурсия, которая повышает сложность и время выполнения
алгоритма
revers_2 используется цикл, котрый упрощает алгоритм и уменьшает время работы функции по сравнению с рекурсией
revers_3 используеются встроенные функции и срез поэтому это самая эффективная реализация

Поскольку время выполнения функций даже при больших входных числах очень маленькое, то оценить время работы с 
помощью run не получится. Можно только заметить что при выполнении
revers_1 -  11 function calls (4 primitive calls) in 0.000 seconds
revers_2 -  4 function calls in 0.000 seconds
revers_3 -  4 function calls in 0.000 seconds
'''
