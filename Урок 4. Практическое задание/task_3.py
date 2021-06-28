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

number = 123456789


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
    enter_num = str(enter_num)
    revers_num = ''.join(reversed(list(enter_num)))
    return revers_num


run('revers_1(number)')
run('revers_2(number)')
run('revers_3(number)')
run('revers_4(number)')
print('revers_1 - ', timeit('revers_1(number)', globals=globals(), number=100000))
print('revers_2 - ', timeit('revers_2(number)', globals=globals(), number=100000))
print('revers_3 - ', timeit('revers_3(number)', globals=globals(), number=100000))
print('revers_4 - ', timeit('revers_4(number)', globals=globals(), number=100000))

# Пока не понятен смысл работы модуля cProfile с небольшим набором простых данных (revers_1 - revers_4). Получается
# что все наборы дают замечательные нулевые результаты. А вот модуль timeit дал более интересную информацию:
# revers_1 - через рекурсию. Я уже знаю, что рекурсия самая медленная;
# revers_2 - через while цикл. Всегда использовал почти всегда этот метод;
# revers_3 - через срезы получается самый лучший результат, когда это возможно;
# revers_4 - через reversed, но он чуть медленнее, потому что используются в вычислении две функции, это не плохо.
