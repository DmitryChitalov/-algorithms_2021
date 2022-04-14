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
    n_list = list(str(enter_num))
    n_list.reverse()
    return "".join(n_list)


number = randint(100, 10000)

print(f'Время выполнения revers_1: {timeit("revers_1(number)", globals=globals())}')
print(f'Время выполнения revers_2: {timeit("revers_2(number)", globals=globals())}')
print(f'Время выполнения revers_3: {timeit("revers_3(number)", globals=globals())}')
print(f'Время выполнения revers_4: {timeit("revers_4(number)", globals=globals())}')
run('revers_1(number)')
run('revers_2(number)')
run('revers_3(number)')
run('revers_4(number)')

'''
Время выполнения revers_1: 0.9827496620000001
Время выполнения revers_2: 0.6553947869999999
Время выполнения revers_3: 0.3351348850000002
Время выполнения revers_4: 0.5250366260000003
Выводы:
1) в функции revers_1 используется рекурсия и эта функция является самой медленной из представленных;
2) в функции revers_2 используется цикл и она быстрее чем revers_1;
3) в функции revers_3 просто переворачивается число с помощью среза и эта функция самая быстрая из данных изначально;
4) в функции revers_4 использовался метод списка .reverse() и этот способ оказался быстрее рекурсии и цикла, 
но уступил в скорости срезу;
5) профилировщик cProfile показал следующие результаты:
для функции revers_1 время запуска составило 0.0 секунд, количество вызовов зависит от передаваемого числа;
функция revers_2 содержит 4 вызова функции, время запуска составило 0.0 секунд;
функция revers_3 содержит 4 вызова функции, время запуска составило 0.0 секунд;
функция revers_4 содержит 6 вызовов функции, время запуска составило 0.0 секунд;
6) финальный итог: для получения реверса числа эффективнее и экономнее по времени использовать срезы.
'''
