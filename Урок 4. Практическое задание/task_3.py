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
from cProfile import run
from timeit import timeit


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


def revers_my(enter_num):
    enter_num = ''.join(list(reversed(str(enter_num))))
    return enter_num


print('ЗАМЕРЫ С ПОМОЩЬЮ TIMEIT')
print('Время рекурсивного реверса')
print(timeit('revers_1(2345678)', globals=globals(), number=100000))
print('Время  реверса с циклом')
print(timeit('revers_2(2345678)', globals=globals(), number=100000))
print('Время  реверса со срезом')
print(timeit('revers_3(2345678)', globals=globals(), number=100000))
print('Время  реверса с функцией reversed')
print(timeit('revers_my(2345678)', globals=globals(), number=100000))

print('ЗАМЕРЫ С ПОМОЩЬЮ cPROFILE')
print('Время рекурсивного реверса')
run('revers_1(2345678)')
print('Время  реверса с циклом')
run('revers_2(2345678)')
print('Время  реверса со срезом')
run('revers_3(2345678)')
print('Время  реверса с функцией reversed')
run('revers_my(2345678)')
'''
TIMEIT
1. Быстрее всего реверс со срезом - 0.028402800000000006 - простая операция. 
2. Чуть медленнее с функцией reversed - 0.057526999999999995 - встроенная 
функция для реверса.
3. Еще медленнее реверс с циклом - 0.09532279999999999 - перебор значений.
4. Самый медленный рекурсивный реверс - 0.14377099999999998 - каждый вызов 
порождает еще вызовы функций.
cPROFILE
Все замеры показали, что проблем с задержкой времени нет, но:
1. Реверс с циклом и реверс со срезом - по 4 вызова функций.
2. Реверс с функцией reversed - 5 вызовов.
3. Рекурсивный реверс - 11 вызовов функций.
'''
