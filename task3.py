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
from random import randint
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


number = randint(100000000, 1000000000000)
print(number)
print(timeit('revers_1(number)', number=1000, globals=globals()))
print(timeit('revers_2(number)', number=1000, globals=globals()))
print(timeit('revers_3(number)', number=1000, globals=globals()))

run('revers_1(number)')
run('revers_2(number)')
run('revers_3(number)')
# слишком малое время
'''
Первый вариант является самым долгим , так как в нём мы используем рекурсию.
Второй вариант быстрее , так как там  мы используем цикл while.
В третьем варианте нет ни рекурсии , ни цикла , соответственно он быстрее
'''