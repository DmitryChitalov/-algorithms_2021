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
    temp_list = list(str(enter_num))
    temp_list.reverse()
    temp = ''.join(temp_list)
    return int(temp)

if __name__ == '__main__':
    enter_num = 123456789
    revers_num = 5
    print(timeit("revers_1(enter_num, revers_num)", globals=globals(), number=10000)) # 0.0281225
    print(timeit("revers_2(enter_num, revers_num)", globals=globals(), number=10000)) # 0.017520900000000006
    print(timeit("revers_3(enter_num)", globals=globals(), number=10000)) # 0.003629199999999999
    print(timeit("revers_4(enter_num)", globals=globals(), number=10000)) # 0.008472099999999996
    run("revers_1(enter_num, revers_num)")
    run("revers_2(enter_num, revers_num)")
    run("revers_3(enter_num)")
    run("revers_4(enter_num)")

'''
Профилировка через timeit гораздо информативнее, т.к. позволяет указать количество замеров.

Третий вариант самый эффективный, т.к. мы получаем реверс путем среза.
'''