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


def revers_4(enter_num):
    lst = list(str(enter_num))
    lst.reverse()
    number = "".join(lst)
    return number


num = 123456789

print(f'cProfile')
run('revers_1(num)')
run('revers_2(num)')
run('revers_3(num)')
run('revers_4(num)')

print('"timeit"')
print(f'{timeit.timeit("revers_1(num)", number=10000, globals=globals())}')
print(f'{timeit.timeit("revers_2(num)", number=10000, globals=globals())}')
print(f'{timeit.timeit("revers_3(num)", number=10000, globals=globals())}')
print(f'{timeit.timeit("revers_4(num)", number=10000, globals=globals())}')


# Самая быстрая функция revers_3 так, как она не использует рекурсию, циклы и дополнительные преобразования,
# а использует срез (внутреннюю функцию), которая использует наименьшее количество операций
