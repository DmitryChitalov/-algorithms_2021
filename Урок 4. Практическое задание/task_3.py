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


def revers_1(enter_num, revers_num=0):  # Самая медленная функция, чем больше будет число тем дольше будет выполнение функции
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):  # Средняя по скорости функция
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):  # Самая быстрая функция, потому что срез это стандартная функция и по умолчанию самая оптимизированная
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


enter_num = int(input('Введите число: '))

run('revers_1(enter_num, revers_num=0)')
run('revers_2(enter_num, revers_num=0)')
run('revers_3(enter_num)')