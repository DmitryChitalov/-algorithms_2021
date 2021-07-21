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
    a = []
    for i in str(enter_num):
        a.append(i)
    a.reverse()
    my_str = ''
    for i in a:
        my_str += i
    return my_str


print(timeit.timeit(
    'revers_1(num_10000)',
    globals=globals(),
    number=10000
))

print(timeit.timeit(
    'revers_2(num_10000)',
    globals=globals(),
    number=10000
))

print(timeit.timeit(
    'revers_3(num_10000)',
    globals=globals(),
    number=10000
))

print(timeit.timeit(
    'revers_4(num_10000)',
    globals=globals(),
    number=10000
))

run('revers_1(num_10000)')
run('revers_2(num_10000)')
run('revers_3(num_10000)')
run('revers_4(num_10000)')

# Т.к мы используем рекурсию в 1 функции, то она будет самой медленной
# Во 2 функции используем цикл, следовательно она быстрее первой
# Моя 4 функция быстрее чем 2 функция с циклом while, так как используется for, который в таких задач в принципе быстрее, чем while
# 3 функция самая быстрая из-за использующихся в ней встроенных функций
