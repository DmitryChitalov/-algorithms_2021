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

from random import randint
import cProfile
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


def reverse_4(enter_num):
    rest_numb, numeral = divmod(enter_num, 10)
    if rest_numb == 0:
        return str(numeral)
    else:
        return str(numeral) + str(reverse_4(rest_numb))


def reverse_5(enter_num):
    return "".join(reversed(str(enter_num)))


ENTER_NUM = randint(10000, 1000000)
# enter_num = int(input('Введите целов число'))
print(revers_1(ENTER_NUM))
print(revers_2(ENTER_NUM))
print(revers_3(ENTER_NUM))
print(reverse_4(ENTER_NUM))
print(reverse_5(ENTER_NUM))
print("revers_1. Время выполнения:")
print(
    timeit.timeit(
        "revers_1(ENTER_NUM)",
        setup='from __main__ import revers_1, ENTER_NUM',
        number=10000))
cProfile.run('revers_1(ENTER_NUM)')
print("revers_2. Время выполнения:")
print(
    timeit.timeit(
        "revers_2(ENTER_NUM)",
        setup='from __main__ import revers_2, ENTER_NUM',
        number=10000))
cProfile.run('revers_2(ENTER_NUM)')
print("revers_3. Время выполнения:")
print(
    timeit.timeit(
        "revers_3(ENTER_NUM)",
        setup='from __main__ import revers_3, ENTER_NUM',
        number=10000))
cProfile.run('revers_3(ENTER_NUM)')
print("reverse_4. Время выполнения:")
cProfile.run('reverse_4(ENTER_NUM)')
print(
    timeit.timeit(
        "reverse_4(ENTER_NUM)",
        setup='from __main__ import reverse_4, ENTER_NUM',
        number=10000))
print("reverse_5. Время выполнения:")
print(
    timeit.timeit(
        "reverse_5(ENTER_NUM)",
        setup='from __main__ import reverse_5, ENTER_NUM',
        number=10000))
cProfile.run('reverse_5(ENTER_NUM)')

# по итогам профилирования самые эффективные алгоритмы revers_3 (через срез) и reverse_5 (через встроенный модуль),
# вариант выполнения через срез как по времени выполняется быстрее всех, так и с наименьшим количеством вызовов функции
