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
    num = []
    for i in str(enter_num):
        num.insert(0, i)
    return ''.join(num)


number = 18561 * 1234


def func():
    revers_1(number)
    revers_2(number)
    revers_3(number)
    revers_4(number)


run('func()')
print('Рекурсия', timeit('revers_1(number)', globals=globals()))
print('Цикл', timeit('revers_2(number)', globals=globals()))
print('Срез', timeit('revers_3(number)', globals=globals()))
print('Вставка', timeit('revers_4(number)', globals=globals()))

# №1 Срез выполняется быстрее так как сложность O(b-a)
# №2 Вставка через insert  имеет сложность O(n)
# №3 Цикл while  имеет сложность O(n) но выполняется медленнее чем вставка
# №4 рекурсия имеет сложность O(n**2) и она самая медленная

# Рекурсия 1.9772253
# Цикл 1.1695951999999998
# Срез 0.2995068000000001
# Вставка 0.9359130999999996
