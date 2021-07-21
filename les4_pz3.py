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
    return str(enter_num) if enter_num < 10 else str(enter_num % 10) + revers_4(enter_num // 10)


def all_func(enter_num):
    for i in range(1000000):
        revers_1(enter_num)
        revers_2(enter_num)
        revers_3(enter_num)
        revers_4(enter_num)

print(f'рекурсия {timeit("revers_1(12345)",globals=globals())}')
print(f'цикл {timeit("revers_2(12345)",globals=globals())}')
print(f'срез {timeit("revers_3(12345)",globals=globals())}')
print(f'терн.оператор + рекурсия {timeit("revers_4(12345)",globals=globals())}')
run('all_func(12345)')


# Замеры timeit и cProfile показывают, что эффективнее всего реализация со срезами.
# Встроенные функции и возможности Python ожидаемо победили)
# Зато решение в одну строку с тернарным оператором оказалось самым медленным
# Измерения timeit и cProfile в целом совпадают, хотя небольшая разница в измерениях прослеживается
