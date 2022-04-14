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
    revers_num = ''
    for n in str(enter_num):
        revers_num = n + revers_num
    return revers_num


num = 3467890

print(revers_1(num))
print(timeit("revers_1(num)", globals=globals()))
print(revers_2(num))
print(timeit("revers_2(num)", globals=globals()))
print(revers_3(num))
print(timeit("revers_3(num)", globals=globals()))
print(revers_4(num))
print(timeit("revers_4(num)", globals=globals()))


run('revers_1(num)')
run('revers_2(num)')
run('revers_3(num)')
run('revers_4(num)')

"""
Аналитика:
Функция revers_1 самая долгая и неэффективная из-за использования рекурсии, а также потому что результат получается 
не совсем верный, тип результата float и ноль остаётся в конце. 
Функция revers_2 также возвращает некорректный 
результат и выполняется долго из-за наличия цикла. 
Функция revers_3 самая удачная так как берется срез по  обратной индексации и нет никаких 
промежуточных переменных для сохранения результата.
В функции revers_4 также используется цикл и промежуточная переменная, поэтому скорость значительно ниже.

"""