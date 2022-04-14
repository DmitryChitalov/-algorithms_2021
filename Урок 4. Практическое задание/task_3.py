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

enter_num = 123


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
    revers_num = [el for el in str(num)]
    revers_num.reverse()
    return ''.join(revers_num)


def main():
    revers_1(num)
    revers_2(num)
    revers_3(num)
    revers_4(num)


num = 123

print(revers_1(num))
print(revers_2(num))
print(revers_3(num))
print(revers_4(num))


print(timeit('revers_1(num)', globals=globals(), number=1))
print(timeit('revers_2(num)', globals=globals(), number=1))
print(timeit('revers_3(num)', globals=globals(), number=1))
print(timeit('revers_4(num)', globals=globals(), number=1))

run('main()')

"""
Результат выполнения:
7.79999999999878e-06
2.999999999999531e-06
2.7000000000013125e-06
5.700000000000843e-06

revers_1() выполняется хуже всех, т.к. это рекурсия.
revers_2() цикл значительно быстрее рекусии
revers_3() самая быстрая, т.к используются встроенная функция str и срез строки
revers_4() проигрывает 2,3 варианту, т.к используется преобразавание числа в список через ЛС, а затем
            преобразование реверсивного списка в строку

"""