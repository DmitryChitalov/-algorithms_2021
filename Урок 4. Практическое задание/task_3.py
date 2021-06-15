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
from random import randint



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
    revers_num = list(str(enter_num))
    revers_num.reverse()
    revers_num = ''.join(revers_num)
    return revers_num


enter_num = randint(0, 1000000)
print(timeit("revers_1(enter_num)", globals=globals(), number=100000))
print(timeit("revers_2(enter_num)", globals=globals(), number=100000))
print(timeit("revers_3(enter_num)", globals=globals(), number=100000))
print(timeit("revers_4(enter_num)", globals=globals(), number=100000))
run("revers_1(enter_num)")
run("revers_2(enter_num)")
run("revers_3(enter_num)")
run("revers_4(enter_num)")
print(revers_1(enter_num))
print(revers_2(enter_num))
print(revers_3(enter_num))
print(revers_4(enter_num))
print(enter_num)

'''
Третий вариант самый быстрый так как используеться смещение которое гораздо быстрее чем целочисленое деление, рекурсия и цыклы. 
Мой вариант похож на вариант №3, но используеться фукция reverse, что чуть медленнее чем вариант №3 из за того что надо 
дополнительно перобразовывать строку в список
'''
