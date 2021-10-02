from cProfile import run
from timeit import timeit
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


def revers_4(num):
    return str(num) if num < 10 else str(num % 10) + revers_4(num // 10)


run('revers_1(1000000000)')
run('revers_2(1000000000)')
run('revers_3(1000000000)')
run('revers_4(1000000000)')

print(timeit('revers_1(1000000000)', globals=globals(), number=1000))
print(timeit('revers_2(1000000000)', globals=globals(), number=1000))
print(timeit('revers_3(1000000000)', globals=globals(), number=1000))
print(timeit('revers_4(1000000000)', globals=globals(), number=1000))

"""
1)функция 3 сработала быстрее всех, ак как используется срез строк;
2)Неплохой результуат у функции 2 с циклами;
3)Рекурсия на последнем месте.
"""