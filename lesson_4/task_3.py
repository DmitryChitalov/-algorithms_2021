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


# Рекурсия
def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)


# Цикл
def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


# Срез
def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


# reversed()
def revers_4(enter_num):
    return int(''.join(reversed(str(enter_num))))


numb = 123456789

print(timeit('revers_1(numb)', number=10000, globals=globals()))
print(timeit('revers_2(numb)', number=10000, globals=globals()))
print(timeit('revers_3(numb)', number=10000, globals=globals()))
print(timeit('revers_4(numb)', number=10000, globals=globals()))
print()

run('revers_1(numb)')
run('revers_2(numb)')
run('revers_3(numb)')
run('revers_4(numb)')

# В revers_1 используется рекурсия, что замедляет работу функции
# В revers_2 используется цикл, средняя скорость работы
# В revers_3 используется срез, максимальная скорость работы
# В revers_4 используется встроенные метод join и функция reversed, время работы близко к revers_3
