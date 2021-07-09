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

import timeit
from cProfile import run

def revers_1(enter_num, revers_num=0): # рекурсия
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)


def revers_2(enter_num, revers_num=0): # цикл
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num): # срез
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num

def revers_4(enter_num): # встроенная функция reversed()
    enter_num = str(enter_num)
    revers_num = (list(reversed(enter_num)))
    return revers_num

print('Замер revers_1 через cProfile:')
run('revers_1')
print('Замер revers_2 через cProfile:')
run('revers_2')
print('Замер revers_3 через cProfile:')
run('revers_3')
print('Замер revers_4 через cProfile:')
run('revers_4')

# cProfile не даёт нам ответа что лучше: пишет, что все хороши одинаково.

print('Замер revers_1 через timeit')
print(timeit.timeit("""def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)""", number=20000))

print('Замер revers_2 через timeit')
print(timeit.timeit("""def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num""", number=20000))

print('Замер revers_3 через timeit')
print(timeit.timeit("""def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num""", number=20000))

print('Замер revers_4 через timeit')
print(timeit.timeit("""def revers_4(enter_num):
    enter_num = str(enter_num)
    revers_num = (list(reversed(enter_num)))
    return revers_num""", number=20000))

"""
ОТВЕТ: лучший результат - срез, худший - рекурсия.
При выборе четвёртого варианта я исходил из того, что скорее всего
быстрым должна быть встроенная функция - есть reversed(). Однако, как 
я понимаю, в любом случае быстрее всех будет срез.

Рекурсия всегда очень медленная, так как "когда программа вызывает функцию, 
создается новый фрейм стека, в котором, помимо прочего, хранятся все 
локальные переменные".

Срез преобразовал данные на месте - in place, не создавая новый объект.
"""