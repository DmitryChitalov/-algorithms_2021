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


if __name__ == '__main__':

    enter_num = 10 ** 700
    str_label = "=" * 20

    print(f'{str_label} ЧИСЛО-ПЕРЕВЕРТЫШ timeit {str_label}')
    print(f'Рекурсия: {timeit("revers_1(enter_num)", globals=globals(), number=10000)}')
    print(f'Цикл    : {timeit("revers_2(enter_num)", globals=globals(), number=10000)}')
    print(f'Срез    : {timeit("revers_3(enter_num)", globals=globals(), number=10000)}')

    print(f'{str_label} ЧИСЛО-ПЕРЕВЕРТЫШ cProfile {str_label}')
    run('revers_1(enter_num)')
    run('revers_2(enter_num)')
    run('revers_3(enter_num)')


"""
Из результата полученных значений видно, что выполнение функции на основе рекурсии 
происходит медленнее цикла и значительно медленнее среза.

Рекурсия - исходя из данных cProfile функция со сложностью O(n) была вызвана n-раз (702 !)
с выполнением математических вычислений константной сложности, вышла на уровень cumtime = 0.001

Цикл - функция со сложностью O(n) с выполнением математических вычислений константной сложности
внутри цикла была вызвана 1 раз. 

Срез - функция получения обратного среза со сложностью O(n) вызвана 1 раз.

Предпологаю, что увеличение времени выполнения функций с одинаковой сложностью происходит:
    в первую очередь из-за многократности выполнения;
    во вторую очередь из-за выполнения дополнительных математических вычислений.
"""