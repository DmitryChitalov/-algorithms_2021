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
    """ Моя реализация через итерратор """
    enter_num = str(enter_num)
    revers_num = ''
    for i in range(1, len(enter_num) + 1):
        revers_num = str(revers_num) + str(enter_num[-i])
    return int(revers_num)

def main(enter_num):
    revers_1(enter_num, revers_num=0)
    revers_2(enter_num, revers_num=0)
    revers_3(enter_num)
    revers_4(enter_num)

print(timeit("revers_1(65231, revers_num=0)", globals=globals(), number=1000000))
print(timeit("revers_2(65231, revers_num=0)", globals=globals(), number=1000000))
print(timeit("revers_3(65231)", globals=globals(), number=1000000))
print(timeit("revers_4(65231)", globals=globals(), number=1000000))

run('main(65231)')
"""
Результат: 
2.01804162
1.3532066870000001
0.5112060710000002
3.194305315
Самая долгая по времени рекурсия, т.к. имеет сложность 2^n
Цикл работает быстрее, далее я реализовал свою ф-ю на основе итерратора, у него сложность 
и он оказался самым времязатратным. Самая быстрая ф-я - срез 
"""
