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
# Первый способ это рекурсия, которая здесь в принципе бесполезна т.к. результат каждой итерации не зависит от
# предыдущей, просто вызываем фукцию еще раз и откусываем от числа по цифре с хвоста и кладем в стек. Простой
# цикл будет быстрее т.к. результат получим сразу и целиком из переменной, что видно по времени втрого примера
# третий вариант с помощью быстрых и встроенных функций перевода числа в строку и получения среза наоборот -
# идеальное решение. Четвертый вариант похож на третий, тоже используем быстрые и встроенные функции, но уже
# не строки, а листа, но приходится сначала перегнать строку в список, потом применить встроенный reverse, а
# потом обратно из списка join-ом получить строку. В итоге чуть дольше предыдущего варианта. Profile по таким
# функциям дает 0-ли т.к. все операции простые и быстрые. Даже рекурсия для этой задачи не долгая. Сделал
# для запуска x раз, но смысл и так понятен в рекурсии в несколько раз больше вызовов функций за счет вызова
# самой себя

from cProfile import run
from random import randint
from timeit import timeit

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
    revers_num = list(enter_num)
    revers_num.reverse()
    return ''.join(revers_num)


def x_times_run(func, x, *args):
    for i in range(1, x):
        func(*args)

num = randint(1, 1000000000)

print(timeit("revers_1(num)", globals=globals(), number=1000000))
print(timeit("revers_2(num)", globals=globals(), number=1000000))
print(timeit("revers_3(num)", globals=globals(), number=1000000))
print(timeit("revers_4(num)", globals=globals(), number=1000000))

run('x_times_run(revers_1, 1000000, num)')
run('x_times_run(revers_2, 1000000, num)')
run('x_times_run(revers_3, 1000000, num)')
run('x_times_run(revers_4, 1000000, num)')

