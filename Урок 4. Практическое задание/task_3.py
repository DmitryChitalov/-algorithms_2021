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
    simple_list = list(str(enter_num))
    simple_list.reverse()
    revers_num = "".join(simple_list)
    return revers_num


enter_num = 10000

t1 = timeit(f"revers_1({enter_num})", globals=globals(), number= 10000)
print(f'Время замера составило: {t1}')

t2 = timeit(f"revers_2({enter_num})", globals=globals(), number= 10000)
print(f'Время замера составило: {t2}')

t3 = timeit(f"revers_3({enter_num})", globals=globals(), number= 10000)
print(f'Время замера составило: {t3}')

t4 = timeit(f"revers_4({enter_num})", globals=globals(), number= 10000)
print(f'Время замера составило: {t4}')

run('revers_1(10000)')
run('revers_2(10000)')
run('revers_3(10000)')
run('revers_4(10000)')

#Вывод:
#1. Рекурсия - ожидаемо самый медленный вариант
#2. Цикл - более быстрый, чем рекурсия но проигрывает по скорости при использовании среза и встроенной функции reverse()
#3. Срез - самый быстрый вариант, имеющий константную сложность, что бьется с О-нотацией
#4. применение встроенной функции значительно ускоряет работу но проигрывает срезу по времени

#С помощью cprofile мы получили нулевые значения, но при помощи этого модуля видно, какие операции производятся
