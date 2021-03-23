from timeit import timeit
import cProfile
"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему!!!

И можете предложить еще свой вариант решения!
Без аналитики задание считается не принятым
"""


def revers_1(enter_num, revers_num=0):  # Самая медленная, так как используется рекурсия
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):  # Работает быстрее, так как перешли к обычному циклу, но медленнее срезов
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):  # Самый быстрый вариает кода, так как используются срезы
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


number = 321

print("revers_1:", timeit("revers_1(number)", globals=globals()))
print("revers_2:", timeit("revers_2(number)", globals=globals()))
print("revers_3:", timeit("revers_3(number)", globals=globals()))

cProfile.run('revers_1(number)')
cProfile.run('revers_2(number)')
cProfile.run('revers_3(number)')


#  Из таблиц видно, что оптимизация не нужна

def simple_var_1(numbers):
    text = ''.join(reversed(str(numbers)))
    return text


my_number = 321

# Мой вариант, используется встроенная функция, что ускоряет код, но это не лучший вариант.

print("simple_var_1:", timeit("simple_var_1(my_number)", globals=globals()))

