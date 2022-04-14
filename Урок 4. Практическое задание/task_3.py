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


import timeit


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


enter_num = int(input("Number: "))

revers_1(enter_num, revers_num=0)
revers_2(enter_num, revers_num=0)
revers_3(enter_num)


print(
    timeit.timeit(
        f'revers_1({enter_num})',
        globals=globals(),
        number=1000)
)

print(
    timeit.timeit(
        f'revers_2({enter_num})',
        globals=globals(),
        number=1000)
)


print(
    timeit.timeit(
        f'revers_3({enter_num})',
        globals=globals(),
        number=1000)
)


"""
Number: 100
0.001018699999999928
0.000684800000000152
0.0004338999999999871

Вывод: реализация через срез является самой эффективной.
"""