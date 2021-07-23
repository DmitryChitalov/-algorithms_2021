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
from random import randint


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


def revers_4(enter_num):  # Ничего не сказано о строках, поэтому с удовольствем воспользуюсь
    return int(str(abs(enter_num))[::-1]) * (-1 if enter_num < 0 else 1)


def revers_5(enter_num):  # Еще вариант, тоже строка, то же самое, чуть иначе записано
    return int('-' * (enter_num < 0) + str(abs(enter_num))[::-1])


def revers_6(enter_num):  # Тоже красиво, тут создаем лист, который затем снова в строку складываем
    return int('-' * (enter_num < 0) + ''.join(list(map(str, str(abs(enter_num))[::-1]))))


if __name__ == '__main__':
    a = randint(1000000000, 10000000000000000)
    print(f'revers_1 отработала за {timeit("revers_1(a)", globals=globals())}')
    run("revers_1(a)")  # revers_1 отработала за 3.0384119999999997
    # 20 function calls (4 primitive calls) in 0.000 seconds
    print('##################################################################')
    print(f'revers_2 отработала за {timeit("revers_2(a)", globals=globals())}')
    run("revers_2(a)")  # revers_2 отработала за 1.9866570000000001
    #  4 function calls in 0.000 seconds
    print('##################################################################')
    print(f'revers_3 отработала за {timeit("revers_3(a)", globals=globals())}')
    run("revers_3(a)")  # revers_3 отработала за 0.2687531999999999
    # 4 function calls in 0.000 seconds
    print('##################################################################')
    print(f'revers_4 отработала за {timeit("revers_4(a)", globals=globals())}')
    run("revers_4(a)")  # revers_4 отработала за 0.4191457999999999
    #  5 function calls in 0.000 seconds
    print('##################################################################')
    print(f'revers_5 отработала за {timeit("revers_5(a)", globals=globals())}')
    run("revers_5(a)")  # revers_5 отработала за 0.4062657000000005
    #  5 function calls in 0.000 seconds
    print('##################################################################')
    print(f'revers_6 отработала за {timeit("revers_6(a)", globals=globals())}')
    run("revers_6(a)")  # revers_6 отработала за 1.7177764999999994
    #  6 function calls in 0.000 seconds
    print('##################################################################')

# Наилучшим образом себя показал алгоритм функции 3, хотя результат не совсем честный. Дело в том, что 1-3 алгоритмы
# не учитывают отрицательные числа и работать корректно с ними не будут, а все остальные - будут. Самый быстрый
# алгоритм - тот, где просто переворачивается строка, без каких-либо вычислений. Второй результат показывает алгоритм
# 5, он медленнее, так как там добавляется модуль числа и умножение на знак, а также условие(для отрицательных). чуть
# хуже 4 с тернарным оператором. Далее куча преобразований в 6 и первые два(они последние, поскольку используют
# вычисления)
