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
num = 741757224127


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


# Моя функция:
def revers_4(numb, rev_num=''):
    return rev_num if numb == 0 else revers_4(numb // 10, rev_num + str(numb % 10))


print(revers_1(num))
print(revers_2(num))
print(revers_3(num))
print(revers_4(num))
print('-' * 100)
run('revers_1(num)')
run('revers_2(num)')
run('revers_3(num)')
run('revers_4(num)')
print('-' * 100)
print(timeit('revers_1(num)', globals=globals(), number=1000))
print(timeit('revers_2(num)', globals=globals(), number=1000))
print(timeit('revers_3(num)', globals=globals(), number=1000))
print(timeit('revers_4(num)', globals=globals(), number=1000))
"""
Выводы:
1. Использование профилировки через cProfile целесообразно только на "тяжелых" алгоритмах с большим объемом данных,
так как в ином случае, мы получаем бесполезную статистику с одними нулями,
следовательно, для простых функций необходимо использовать модуль timeit для замеров времени выполнения.
2. Быстрее всех у нас отработает функция revers_3, потому как в данной функции, в отличии от остальных, нет
ни циклов (как в revers_2), ни рекурсивных вызовов (как в revers_1 и revers_4). Реализация данной функции
выполнена через встроенные функции, которые заточены на быстрое выполенние.
"""
