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


def revers_1(num, rev=0):
    if num == 0:
        return rev
    else:
        numb = num % 10
        rev = (num + numb / 10) * 10
        num //= 10
        return revers_1(num, rev)


def revers_2(num, rev=0):
    while num != 0:
        numb = num % 10
        rev = (rev + numb / 10) * 10
        num //= 10
    return rev


def revers_3(num):
    num = str(num)
    rev = num[::-1]
    return rev


def revers_4(enter_num):
    return int(''.join(reversed(str(enter_num))))


numb = 12345

print(timeit('revers_1(numb)', number=10000, globals=globals()))
print(timeit('revers_2(numb)', number=10000, globals=globals()))
print(timeit('revers_3(numb)', number=10000, globals=globals()))
print(timeit('revers_4(numb)', number=10000, globals=globals()))


run('revers_1(numb)')
run('revers_2(numb)')
run('revers_3(numb)')
run('revers_4(numb)')
