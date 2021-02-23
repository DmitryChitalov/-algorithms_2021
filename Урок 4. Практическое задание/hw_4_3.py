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
from timeit import timeit
from cProfile import run


def revers_1(enter_num, revers_num=0):  # в целом работает не корректно, т к если число например 3210, возвращает 123.0
    if enter_num == 0:  # работает медленно из-за множественного вызова функции (рекурсия)
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):  # работает быстрее рекурсии, т к это просто цикл и нет повторных вызовов
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):  # операции со срезами самые быстрые, из трех реализацие единственная верно работает с нулями
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def revers_4(enter_num):  # работает медленнее среза, но быстрее всего остального, т к нет циклов
    enter_num = list(str(enter_num))
    enter_num.reverse()
    revers_num = ''.join(enter_num)
    return revers_num


def main():
    revers_1(num)
    revers_2(num)
    revers_3(num)
    revers_4(num)


num = 3210

run('main()')  # как я поняла, слабых мест нет
print(timeit("revers_1(num)", globals=globals()))
print(timeit("revers_2(num)", globals=globals()))
print(timeit("revers_3(num)", globals=globals()))
print(timeit("revers_4(num)", globals=globals()))
