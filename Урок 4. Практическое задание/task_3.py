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

rand_num = randint(100000, 1000000)


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
    return ''.join(reversed(str(enter_num)))

print(revers_1(100))
print(revers_2(100))
print(revers_3(100))
print(revers_4(100))
print(f'Время revers_1(rand_num): {timeit("revers_1(rand_num)", globals=globals())}')
print(f'Время revers_2(rand_num): {timeit("revers_2(rand_num)", globals=globals())}')
print(f'Время revers_3(rand_num): {timeit("revers_3(rand_num)", globals=globals())}')
print(f'Время revers_4(rand_num): {timeit("revers_4(rand_num)", globals=globals())}')

# def main():
#     run_1 = revers_1(rand_num)
#     run_2 = revers_2(rand_num)
#     run_3 = revers_3(rand_num)
#     run_4 = revers_4(rand_num)
#
# run('main()') # годится только для разового запуска
run_1 = """
for i in range(1000000):
    revers_1(rand_num)
"""
run_2 = """
for i in range(1000000):
    revers_2(rand_num)
"""
run_3 = """
for i in range(1000000):
    revers_3(rand_num)
"""
run_4 = """
for i in range(1000000):
    revers_4(rand_num)
"""

run(run_1)
run(run_2)
run(run_3)
run(run_4)

"""
Функция revers_1 самая медленная(огромное кол-во ncalls) т.к. рекурсия и не работает с числами оканчивающимися на 0 
как и revers_2.
revers_3 самая быстрая т.к срез, нет циклов.
revers_4 на втором месте из-за дополнительных вызовов .join
 """