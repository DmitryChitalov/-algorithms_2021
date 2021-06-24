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
    return int(''.join(list(reversed(list(str(enter_num))))))

def revers_5(enter_num):
    return ''.join(list(str(enter_num))[::-1])

def revers_6(enter_num):
    return str(enter_num)[::-1]

def revers_7(enter_num):
    l = list(str(enter_num))
    l.reverse()
    return ''.join(l)


enter_num = int(input('enter a number: '))

print(revers_1(enter_num))
print(revers_2(enter_num))
print(revers_3(enter_num))
print(revers_4(enter_num))
print(revers_5(enter_num))
print(revers_6(enter_num))
print(revers_7(enter_num))
print()

print(timeit("revers_1(enter_num)", setup="from __main__ import revers_1, enter_num", number=1000000))
print(timeit("revers_2(enter_num)", globals=globals(), number=1000000))
print(timeit("revers_3(enter_num)", globals=globals(), number=1000000))
print(timeit("revers_4(enter_num)", globals=globals(), number=1000000))
print(timeit("revers_5(enter_num)", globals=globals(), number=1000000))
print(timeit("revers_6(enter_num)", globals=globals(), number=1000000))
print(timeit("revers_7(enter_num)", globals=globals(), number=1000000))
print()


run('revers_1(enter_num)')
run('revers_2(enter_num)')
run('revers_3(enter_num)')
run('revers_4(enter_num)')
run('revers_5(enter_num)')
run('revers_6(enter_num)')
run('revers_7(enter_num)')

# Вариант функции №1 через рекурсию имеет экспоненциальную сложность, поэтому время его выполнения
# в 6 раз превышает минимальное (вариант 3 и 6),
# вариант 2 с циклом, тремя вводимыми переменными и расчетами также далек от минимального.
# вариант 3 и 6 без использования циклов основаны на использовании среза в обратном порядке - самые простые
# и эффективные по затратам времени и сложности.
# варианты 4,5,7 используют встроенные методы, функции, и хоть код лаконичен, он несет большие затраты
# по ресурсам и времени

# 3.6214113
# 2.500988099999999
# 0.6784856999999995
# 1.8996774999999992
# 1.3005237999999988
# 0.6663718999999979
# 1.1874029999999998

# профилировка каждого алгоритма через cProfile также подтверждает наш вывод про
# необходимость оптимизации варианта 1 (рекурсия) -
# 11 function calls (4 primitive calls) in 0.011 seconds. есть проблемные места, повторяющиеся вызовы

