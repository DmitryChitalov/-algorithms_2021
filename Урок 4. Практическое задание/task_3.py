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
    num_list = list(f'{enter_num}')
    num_list.reverse()
    revers_num_str = ''
    for el in num_list:
        revers_num_str += el
    return revers_num_str


enter_num = 1234567890

print(timeit("revers_1(enter_num, revers_num=0)", setup="from __main__ import revers_1, enter_num", number=10000))
print(timeit("revers_2(enter_num, revers_num=0)", setup="from __main__ import revers_2, enter_num", number=10000))
print(timeit("revers_3(enter_num)", setup="from __main__ import revers_3, enter_num", number=10000))
print(timeit("revers_4(enter_num)", setup="from __main__ import revers_4, enter_num", number=10000))

run('revers_1(enter_num, revers_num=0)')
run('revers_2(enter_num, revers_num=0)')
run('revers_3(enter_num)')
run('revers_4(enter_num)')

"""
Цикл while работает медленнее, чем for, но в функции без цикла меньшая сложность поэтому она самая быстрая.
Рекурсия накапливает вызовы стеком и потом происходит обратный процесс получунии значений, это занимает много времени.
"""
