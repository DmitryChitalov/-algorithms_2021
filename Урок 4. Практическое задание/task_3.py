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
from random import randint


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
    revers_num = ""
    enter_num = str(enter_num)
    for i in enter_num:
        revers_num = i + revers_num
    return revers_num


my_num = randint(1, 1000000000)

print("\nФункция revers_1()")
print(timeit("revers_1(my_num)", globals=globals(), number=100000))
run('revers_1(my_num)')

print("\nФункция revers_2()")
print(timeit("revers_2(my_num)", globals=globals(), number=100000))
run('revers_2(my_num)')

print("\nФункция revers_3()")
print(timeit("revers_3(my_num)", globals=globals(), number=100000))
run('revers_3(my_num)')

print("\nФункция revers_4()")
print(timeit("revers_4(my_num)", globals=globals(), number=100000))
run('revers_4(my_num)')

"""
Время выполнения при 1000 повторах:
revers_1()          0.36135397900000005
revers_2()          0.30233625799999997        
revers_3()          0.05664146999999997
revers_4()          0.16760675700000005

Наилучшее время у алгоритма revers_3() - за счет того, что применяется срез строки, имеющий константную сложность.

Алгоритм revers_4() - второй по скорости, т.к. также использует строковые методы вместо последовательного деления 
исходного числа при помощи рекурсии и цикла (revers_1() и revers_2(), соответственно. 


"""
